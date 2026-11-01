import plotly.express as px
import pandas as pd
import streamlit as st


def render_activity_chart():
    data = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Steps": [6500, 8200, 7500, 9000, 7800, 10500, 8500]
    })

    fig = px.bar(
        data,
        x="Day",
        y="Steps",
        title="Weekly Step Activity",
        color="Steps",
        color_continuous_scale=["#353535", "#9eff00"]
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#1d1d1d",
        plot_bgcolor="#1d1d1d",
        font_color="white",
        coloraxis_showscale=False,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    st.plotly_chart(fig, use_container_width=True)


def render_sleep_chart():
    data = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Sleep Hours": [6.5, 7, 8, 6, 7.5, 8.5, 7.5]
    })

    fig = px.line(
        data,
        x="Day",
        y="Sleep Hours",
        title="Weekly Sleep Analysis",
        markers=True
    )

    fig.update_traces(
        line=dict(color="#9eff00", width=3),
        marker=dict(size=9)
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#1d1d1d",
        plot_bgcolor="#1d1d1d",
        font_color="white",
        margin=dict(l=20, r=20, t=50, b=20)
    )

    st.plotly_chart(fig, use_container_width=True)