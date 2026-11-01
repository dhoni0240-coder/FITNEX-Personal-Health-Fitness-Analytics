import streamlit as st


def render_sidebar():
    menu_items = [
        ("🏠", "Dashboard"),
        ("📝", "Health Tracking"),
        ("📊", "Statistics"),
        ("🏃", "Activities"),
        ("🎯", "Goals"),
        ("💡", "Health Insights"),
        ("📄", "Reports"),
        ("👤", "Profile")
    ]

    if "current_page" not in st.session_state:
        st.session_state.current_page = "Dashboard"

    with st.sidebar:
        st.markdown("# FITNEX")
        st.caption("PERSONAL FITNESS ANALYTICS")

        st.markdown("---")
        st.markdown("### MENU")

        for icon, title in menu_items:
            if st.button(
                f"{icon}  {title}",
                key=f"nav_{title}",
                use_container_width=True
            ):
                st.session_state.current_page = title
                st.rerun()

        st.markdown("---")
        st.caption("FITNEX v1.0")
        st.caption("Stay Healthy. Stay Strong. 💪")

    return st.session_state.current_page