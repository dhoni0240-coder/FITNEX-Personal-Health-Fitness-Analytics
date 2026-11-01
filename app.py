from pathlib import Path

import streamlit as st

from components.sidebar import render_sidebar
from components.metric_cards import render_metric_card
from components.charts import (
    render_activity_chart,
    render_sleep_chart
)


# PAGE CONFIGURATION
st.set_page_config(
    page_title="FITNEX | Fitness Analytics",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)


# LOAD CSS
def load_css():
    css_path = Path(__file__).parent / "assets" / "style.css"

    with open(css_path, "r", encoding="utf-8") as file:
        css = file.read()

    st.html(f"<style>{css}</style>")


load_css()


# SESSION STATE
if "user_name" not in st.session_state:
    st.session_state.user_name = "Ashirvad"


# SIDEBAR
current_page = render_sidebar()


# DASHBOARD PAGE
def dashboard_page():

    # HERO SECTION
    st.html(f"""
        <div class="hero">
            <h1>Welcome Back, <span>{st.session_state.user_name}!</span></h1>
            <p>Your fitness journey continues. Keep pushing your limits!</p>
            <p>Consistency is the key to a healthier lifestyle.</p>
        </div>
    """)

    # METRICS
    st.markdown('<div class="section-title">Your Daily Overview</div>',
                unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        render_metric_card(
            "Steps Today",
            "8,500",
            "↑ 12% from yesterday",
            "👟"
        )

    with col2:
        render_metric_card(
            "Sleep Duration",
            "7.5 hrs",
            "Good sleep progress",
            "😴"
        )

    with col3:
        render_metric_card(
            "Calories Burned",
            "350 kcal",
            "↑ 8% from yesterday",
            "🔥"
        )

    with col4:
        render_metric_card(
            "Water Intake",
            "2.5 L",
            "Goal almost completed",
            "💧"
        )

    st.markdown("")

    # CHARTS
    st.markdown(
        '<div class="section-title">Fitness Analytics</div>',
        unsafe_allow_html=True
    )

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        with st.container(border=True):
            render_activity_chart()

    with chart_col2:
        with st.container(border=True):
            render_sleep_chart()

    # FITNESS GOALS
    st.markdown(
        '<div class="section-title">Daily Fitness Goals</div>',
        unsafe_allow_html=True
    )

    goal_col1, goal_col2, goal_col3, goal_col4 = st.columns(4)

    goals = [
        ("Steps", 8500, 10000, "👟"),
        ("Sleep", 7.5, 8, "😴"),
        ("Water", 2.5, 3, "💧"),
        ("Exercise", 35, 45, "🏋️")
    ]

    for column, (name, current, target, icon) in zip(
        [goal_col1, goal_col2, goal_col3, goal_col4],
        goals
    ):
        with column:
            progress = min(current / target, 1.0)

            st.markdown(
                f"### {icon} {name}",
                unsafe_allow_html=True
            )

            st.progress(progress)

            st.caption(
                f"{current} / {target}"
            )

    # RECENT ACTIVITIES
    st.markdown(
        '<div class="section-title">Recent Activities</div>',
        unsafe_allow_html=True
    )

    activities = [
        ("🏃 Morning Running", "30 minutes", "Completed"),
        ("🚶 Evening Walking", "20 minutes", "Completed"),
        ("🏋️ Strength Training", "25 minutes", "Completed")
    ]

    for activity, duration, status in activities:
        st.html(f"""
            <div class="activity-card">
                <span>{activity}</span>
                <span style="margin-left: 20px; color: #aaaaaa;">
                    {duration}
                </span>
                <span class="activity-status">{status}</span>
            </div>
        """)


# OTHER PAGES
def placeholder_page(page_name):

    st.title(page_name)

    st.info(
        f"The {page_name} module is under development."
    )


# PAGE ROUTING
if current_page == "Dashboard":
    dashboard_page()

else:
    placeholder_page(current_page)


# FOOTER
st.markdown("---")

st.markdown(
    "<center style='color: #888888;'>"
    "FITNEX © 2026 | Personal Health & Fitness Analytics"
    "</center>",
    unsafe_allow_html=True
)