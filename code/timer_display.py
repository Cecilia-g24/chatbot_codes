import streamlit as st
from streamlit.components.v1 import html
import time

def show_countdown_timer_js(timer_seconds=300, timer_key="timer_start"):
    # saves initial time
    if timer_key not in st.session_state:
        st.session_state[timer_key] = time.time()

    # calculates remaining time (re-calculates at every refresh)
    time_left = max(0, int(timer_seconds - (time.time() - st.session_state[timer_key])))
    start_minutes = time_left // 60
    start_seconds = time_left % 60
    timer_text = f"{start_minutes:02d}:{start_seconds:02d}"

    my_html = f"""
    <script>
    function startTimer(duration, display) {{
        var timer = duration, minutes, seconds;
        var countdown = setInterval(function () {{
            minutes = parseInt(timer / 60, 10)
            seconds = parseInt(timer % 60, 10);

            minutes = minutes < 10 ? "0" + minutes : minutes;
            seconds = seconds < 10 ? "0" + seconds : seconds;

            display.textContent = minutes + ":" + seconds;

            if (--timer < 0) {{
                display.textContent = "00:00";
                clearInterval(countdown);
            }}
        }}, 1000);
    }}

    window.onload = function () {{
        var seconds = {time_left};
        var display = document.querySelector('#time');
        startTimer(seconds, display);
    }};
    </script>

    <div style="font-size: 1.0em; font-weight: bold; color: #FFB800;">
      ⏳ Remaining Time: <span id="time">{timer_text}</span>
    </div>
    """
    html(my_html, height=50)
