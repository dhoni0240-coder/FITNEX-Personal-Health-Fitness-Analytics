import streamlit as st

from services.auth_service import register_user, authenticate_user


def render_authentication():

    st.html("""
        <div class="auth-hero">
            <div class="auth-overlay">
                <h1>FIT<span>NEX</span></h1>
                <h3>YOUR FITNESS. YOUR PROGRESS. YOUR JOURNEY.</h3>
                <p>Build healthier habits. Track your progress. Become stronger.</p>
            </div>
        </div>
    """)

    left, center, right = st.columns([1, 1.5, 1])

    with center:

        login_tab, register_tab = st.tabs(
            ["LOGIN", "CREATE ACCOUNT"]
        )

        with login_tab:

            st.markdown("### Welcome Back!")
            st.caption("Login to access your fitness dashboard.")

            with st.form("login_form"):

                email = st.text_input(
                    "Email Address",
                    placeholder="Enter your email"
                )

                password = st.text_input(
                    "Password",
                    type="password",
                    placeholder="Enter your password"
                )

                submitted = st.form_submit_button(
                    "LOGIN",
                    use_container_width=True
                )

                if submitted:

                    if not email.strip() or not password:
                        st.warning("Please enter your email and password.")

                    else:
                        success, user = authenticate_user(
                            email.strip().lower(),
                            password
                        )

                        if success:
                            st.session_state.authenticated = True
                            st.session_state.user = user
                            st.session_state.user_name = user["full_name"]
                            st.session_state.current_page = "Dashboard"
                            st.rerun()

                        else:
                            st.error("Invalid email or password.")

        with register_tab:

            st.markdown("### Create Your Account")
            st.caption("Start your personal fitness journey today.")

            with st.form("registration_form"):

                full_name = st.text_input(
                    "Full Name",
                    placeholder="Enter your full name"
                )

                email = st.text_input(
                    "Email Address",
                    placeholder="Enter your email"
                )

                password = st.text_input(
                    "Password",
                    type="password",
                    placeholder="Create a password"
                )

                confirm_password = st.text_input(
                    "Confirm Password",
                    type="password",
                    placeholder="Confirm your password"
                )

                submitted = st.form_submit_button(
                    "CREATE ACCOUNT",
                    use_container_width=True
                )

                if submitted:

                    if not all([
                        full_name.strip(),
                        email.strip(),
                        password,
                        confirm_password
                    ]):
                        st.warning("Please complete all fields.")

                    elif "@" not in email or "." not in email.split("@")[-1]:
                        st.warning("Enter a valid email address.")

                    elif len(password) < 8:
                        st.warning("Password must contain at least 8 characters.")

                    elif password != confirm_password:
                        st.error("Passwords do not match.")

                    else:
                        success, message = register_user(
                            full_name.strip(),
                            email.strip().lower(),
                            password
                        )

                        if success:
                            st.success(message)
                            st.info("Your account has been created. Please login.")

                        else:
                            st.error(message)

    st.markdown(
        """
        <div class="auth-footer">
            FITNEX © 2026 | PERSONAL HEALTH & FITNESS ANALYTICS
        </div>
        """,
        unsafe_allow_html=True
    )