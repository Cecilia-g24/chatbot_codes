#!/bin/bash

# check if we're in the right branch

git_branch=$(git rev-parse --abbrev-ref HEAD)
case $git_branch in
  main)
    ST_SLUG=study
    ST_PORT=8501
    ;;
  testing)
    ST_SLUG=test
    ST_PORT=8502
    ;;
  *)
    echo "******** WRONG BRANCH! Expected main or testing, but got: $git_branch ********"
    exit 1
esac

# --- Configuration ---
# Set the time to wait between checks (in seconds)
SLEEP_INTERVAL=60

# --- Initial Start-up ---
echo "🚀 Starting initial Streamlit process on /$ST_SLUG:$ST_PORT..."
streamlit run interview.py --server.port $ST_PORT --server.baseUrlPath $ST_SLUG &
PID=$!
echo "✅ Streamlit started with PID: $PID"

# --- Monitoring Loop ---
while true; do
  echo "🔄 Checking for updates..."

  # Get the current HEAD commit hash
  OLD_HEAD=$(git rev-parse HEAD)

  # Fetch the latest changes from the git repository
  git pull

  # Get the new HEAD commit hash
  NEW_HEAD=$(git rev-parse HEAD)

  # Check if the HEAD commit has changed
  if [ "$OLD_HEAD" != "$NEW_HEAD" ]; then
    echo "✨ New commit detected! Restarting Streamlit..."

    # Stop the old Streamlit process
    kill $PID
    wait $PID 2>/dev/null
    echo "🛑 Stopped old process with PID: $PID"

    # Start the new Streamlit process
    streamlit run interview.py --server.port $ST_PORT --server.baseUrlPath $ST_SLUG &
    PID=$!
    echo "🚀 New Streamlit process started with PID: $PID"
  else
    echo "👍 No changes. Continuing to run process $PID."
  fi

  # Wait for the defined interval before checking again
  echo "😴 Sleeping for $SLEEP_INTERVAL seconds..."
  sleep $SLEEP_INTERVAL
done
