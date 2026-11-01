import streamlit as st
from html import escape


def render_metric_card(title, value, delta, icon):
    st.html(f"""
        <div class="metric-card">
            <div class="metric-title">
                {icon} {escape(str(title))}
            </div>

            <div class="metric-value">
                {escape(str(value))}
            </div>

            <div class="metric-delta">
                {escape(str(delta))}
            </div>
        </div>
    """)