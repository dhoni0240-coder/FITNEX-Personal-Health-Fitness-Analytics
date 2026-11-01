import streamlit as st
import plotly.express as px
import pandas as pd

from pathlib import Path
import streamlit as st

def load_css():
    css_path = Path(__file__).parent / "assets" / "style.css"

    with open(css_path, "r", encoding="utf-8") as file:
        css = file.read()

    st.html(f"<style>{css}</style>")


st.set_page_config(
    page_title="FITNEX | Fitness Analytics",
    page_icon="💪",
    layout="wide"
)

load_css()

st.set_page_config(
    page_title="FITNEX | Fitness Analytics",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background-color: #101010;
    color: #ffffff;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stDecoration"] {
    display: none;
}

[data-testid="stSidebar"] {
    background-color: #171717;
    border-right: 1px solid #292929;
}

[data-testid="stSidebar"] h1 {
    color: #9EFF00;
    font-weight: 800;
}

[data-testid="stSidebar"] p {
    color: #bdbdbd;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 100%;
}

/* SIDEBAR BUTTONS */

div[data-testid="stSidebar"] div.stButton > button {
    background-color: #222222;
    color: #eeeeee;
    border: 1px solid #333333;
    border-radius: 10px;
    text-align: left;
    padding: 12px;
    transition: 0.3s;
}

div[data-testid="stSidebar"] div.stButton > button:hover {
    background-color: #9EFF00;
    color: #101010;
    border-color: #9EFF00;
}

/* HERO SECTION */

.hero {
    background:
        linear-gradient(
            90deg,
            rgba(0,0,0,0.94),
            rgba(0,0,0,0.65),
            rgba(0,0,0,0.20)
        ),
        url("https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1600");

    background-size: cover;
    background-position: center;
    min-height: 260px;
    padding: 45px;
    border-radius: 20px;
    border: 1px solid #383838;
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin-bottom: 30px;
}

.hero h1 {
    color: white;
    font-size: 36px;
    font-weight: 800;
    margin-bottom: 8px;
}

.hero h1 span {
    color: #9EFF00;
}

.hero p {
    color: #dddddd;
    font-size: 17px;
    margin-bottom: 8px;
}

/* SECTION HEADINGS */

.section-title {
    font-size: 21px;
    font-weight: 700;
    color: white;
    margin-top: 25px;
    margin-bottom: 18px;
}

/* METRIC CARDS */

.metric-card {
    background: linear-gradient(145deg, #262626, #191919);
    border: 1px solid #383838;
    border-radius: 17px;
    padding: 22px;
    min-height: 135px;
    transition: 0.3s;
}

.metric-card:hover {
    border-color: #9EFF00;
    transform: translateY(-3px);
}

.metric-title {
    color: #bdbdbd;
    font-size: 14px;
    font-weight: 500;
}

.metric-value {
    color: white;
    font-size: 27px;
    font-weight: 700;
    margin-top: 10px;
}

.metric-delta {
    color: #9EFF00;
    font-size: 13px;
    margin-top: 5px;
}

/* DASHBOARD PANELS */

.panel {
    background: #1b1b1b;
    border: 1px solid #333333;
    border-radius: 17px;
    padding: 20px;
}

/* FITNESS GOALS */

.goal-card {
    background: #222222;
    border: 1px solid #383838;
    border-radius: 15px;
    padding: 18px;
    text-align: center;
}

/* RECENT ACTIVITIES */

.activity-card {
    background: #222222;
    padding: 17px;
    border-radius: 12px;
    margin-bottom: 12px;
    border: 1px solid #333333;
    color: white;
    font-size: 14px;
}

.activity-status {
    float: right;
    color: #9EFF00;
    font-weight: 600;
}

/* GENERAL */

h1, h2, h3 {
    color: white;
}

.stProgress > div > div > div > div {
    background-color: #9EFF00;
}

</style>
""", unsafe_allow_html=True)


if "user_name" not in st.session_state:
    st.session_state.user_name = "Ashirvad"

if "current_page" not in st.session_state:
    st.session_state.current_page = "Dashboard"


with st.sidebar:

    st.markdown("""
    <h1 style="color:#9EFF00; font-size:35px;">
        💪 FITNEX
    </h1>
    <p style="font-size:12px; letter-spacing:1px;">
        PERSONAL HEALTH & FITNESS ANALYTICS
    </p>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("### MAIN MENU")

    navigation = {
        "Dashboard": "🏠",
        "Health Tracking": "❤️",
        "Statistics": "📊",
        "Activities": "🏃",
        "Goals": "🎯",
        "Health Insights": "💡",
        "Reports": "📄",
        "Profile": "👤"
    }

    for page, icon in navigation.items():

        if st.button(
            f"{icon}   {page}",
            key=f"nav_{page}",
            use_container_width=True
        ):
            st.session_state.current_page = page

    st.divider()

    st.markdown("""
    <div style="
        background:#222222;
        padding:18px;
        border-radius:15px;
        border:1px solid #383838;
        text-align:center;
    ">
        <h2 style="color:#9EFF00;">💚</h2>
        <h4>Your Health.</h4>
        <h4>Your Progress.</h4>
        <p style="font-size:12px;color:#999999;">
            Stay Healthy, Stay Strong.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.caption("FITNEX VERSION 1.0")


if st.session_state.current_page == "Dashboard":


    st.html(f"""
    <div class="hero">

        <h1>
            Welcome Back,
            <span>{st.session_state.user_name}!</span> 👋
        </h1>

        <p>Your fitness journey starts here.</p>

        <p><i>Stay Healthy, Stay Strong.</i></p>

    </div>
    """)

    st.html("""
    <div class="section-title">
        TODAY'S OVERVIEW
    </div>
    """)

    col1, col2, col3, col4 = st.columns(4)

    metrics = [
        ("👟 Daily Steps", "8,500", "↑ 12% vs yesterday"),
        ("😴 Sleep Duration", "7.5 hrs", "↑ 0.5 hrs"),
        ("🔥 Calories Burned", "350 kcal", "↑ 8%"),
        ("💧 Water Intake", "2.5 L", "↑ 0.3 L")
    ]

    for col, metric in zip([col1, col2, col3, col4], metrics):

        with col:

            st.html(f"""
            <div class="metric-card">

                <div class="metric-title">
                    {metric[0]}
                </div>

                <div class="metric-value">
                    {metric[1]}
                </div>

                <div class="metric-delta">
                    {metric[2]}
                </div>

            </div>
            """)


    st.html("""
    <div class="section-title">
        FITNESS PROGRESS
    </div>
    """)

    left, right = st.columns(2)

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    steps = [6500, 7200, 8100, 7800, 8500, 7900, 8500]

    sleep = [6, 5.5, 7, 6.7, 8.2, 7.2, 8.3]


    with left:

        st.markdown("""
        <div class="panel">
            <h3>📊 Weekly Activity</h3>
        </div>
        """, unsafe_allow_html=True)

        activity_df = pd.DataFrame({
            "Day": days,
            "Steps": steps
        })

        fig = px.bar(
            activity_df,
            x="Day",
            y="Steps"
        )

        fig.update_traces(
            marker_color="#9EFF00",
            marker_line_width=0
        )

        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="#1b1b1b",
            plot_bgcolor="#1b1b1b",
            font_color="white",
            margin=dict(l=20, r=20, t=20, b=20),
            height=300,
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displayModeBar": False}
        )

    with right:

        st.markdown("""
        <div class="panel">
            <h3>😴 Sleep Analysis</h3>
        </div>
        """, unsafe_allow_html=True)

        sleep_df = pd.DataFrame({
            "Day": days,
            "Hours": sleep
        })

        fig = px.line(
            sleep_df,
            x="Day",
            y="Hours",
            markers=True
        )

        fig.update_traces(
            line_color="#A970FF",
            line_width=3,
            marker_size=9
        )

        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="#1b1b1b",
            plot_bgcolor="#1b1b1b",
            font_color="white",
            margin=dict(l=20, r=20, t=20, b=20),
            height=300,
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displayModeBar": False}
        )


    st.html("""
    <div class="section-title">
        FITNESS GOALS
    </div>
    """)

    goal1, goal2, goal3, goal4 = st.columns(4)

    goals = [
        (goal1, "👟 Steps", 85),
        (goal2, "😴 Sleep", 94),
        (goal3, "🏋️ Workout", 70),
        (goal4, "💧 Water", 80)
    ]

    for col, title, percentage in goals:

        with col:

            st.markdown('<div class="goal-card">', unsafe_allow_html=True)

            st.subheader(title)

            st.progress(percentage / 100)

            st.markdown(f"### {percentage}%")

            st.caption("Daily Goal Progress")

            st.markdown('</div>', unsafe_allow_html=True)


    st.html("""
    <div class="section-title">
        RECENT ACTIVITIES
    </div>
    """)

    activities = [
        ("🏃", "Morning Walk — 45 minutes", "Today, 7:30 AM"),
        ("🏋️", "Strength Training — 60 minutes", "Yesterday, 6:00 PM"),
        ("💧", "Water Intake — 2.5 Litres", "Yesterday, 10:00 AM")
    ]

    for icon, activity, time in activities:

        st.html(f"""
        <div class="activity-card">

            {icon}
            <strong>{activity}</strong>

            <span class="activity-status">
                Completed
            </span>

            <br>

            <span style="color:#999999;font-size:12px;">
                {time}
            </span>

        </div>
        """)

elif st.session_state.current_page == "Health Tracking":

    st.title("❤️ Health Tracking")
    st.write("Record and monitor your daily health habits.")

elif st.session_state.current_page == "Statistics":

    st.title("📊 Fitness Statistics")
    st.write("Explore your health and fitness data.")

elif st.session_state.current_page == "Activities":

    st.title("🏃 Activities")
    st.write("Manage your daily physical activities.")

elif st.session_state.current_page == "Goals":

    st.title("🎯 Fitness Goals")
    st.write("Set and monitor your fitness targets.")

elif st.session_state.current_page == "Health Insights":

    st.title("💡 Health Insights")
    st.write("Discover insights from your health records.")

elif st.session_state.current_page == "Reports":

    st.title("📄 Reports")
    st.write("Generate daily, weekly and monthly reports.")

elif st.session_state.current_page == "Profile":

    st.title("👤 My Profile")
    st.write("Manage your personal information.")