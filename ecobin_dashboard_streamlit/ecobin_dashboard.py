import streamlit as st
import pandas as pd
import numpy as np

# Dummy data for the dashboard
users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "cleaner1": {"password": "clean123", "role": "Cleaner"}
}

# Session state to track login status
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None

# Styled Login with center alignment
def login():
    st.markdown("""
        <style>
        .stApp {
            background-color: #d4edda;
            background-image: url('https://cdn.pixabay.com/photo/2017/09/01/21/47/background-2706023_1280.jpg');
            background-size: cover;
            background-position: center;
            padding-left: 0px;
            padding-right: 0px;
        }
        .login-box {
            background: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 12px;
            width: 100%;
            max-width: 400px;
            margin: 5rem auto;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.title("🌿 EcoBin Login")

    username = st.text_input("Username")
    role = st.selectbox("Login as", ["Admin", "Cleaner"])
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username]["password"] == password and users[username]["role"] == role:
            st.session_state.logged_in = True
            st.session_state.role = role
        else:
            st.error("Invalid credentials or role")

    st.markdown('</div>', unsafe_allow_html=True)

# Logout
def logout():
    st.session_state.logged_in = False
    st.session_state.role = None

# Admin Dashboard
def admin_dashboard():
    st.title("Admin Dashboard")

    # Tabs for Admin Dashboard
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "Overview", "Graphs", "Cleaner Performance", "Bin Status & Alerts", "User Management", "Reports", "Settings"
    ])

    with tab1:
        st.title("Overview")

        # Layout: Three columns for the metrics and images
        col1, col2, col3 = st.columns(3)

        # First column: Smart Bins metric and image
        with col1:
            st.metric("Total Smart Bins", 150)
            st.image("ecobin_dashboard_streamlit/Screenshot 2025-04-25 190433.png", width=150, caption="Smart Bin")

        # Second column: Bins Full Today metric and image
        with col2:
            st.metric("Bins Full Today", 25)
            st.image("ecobin_dashboard_streamlit/Screenshot 2025-04-25 185629.png", width=150, caption="Bin Full")

        # Third column: Cleaners On-Duty metric and image
        with col3:
            st.metric("Cleaners On-Duty", 12)
            st.image("ecobin_dashboard_streamlit/Screenshot 2025-04-25 190623.png", width=150, caption="Cleaner")

        # Optionally, add some additional information or charts below
        st.write("The following metrics represent the current state of our Smart Bin system.")


    with tab2:
        # Graphs tab content
        data = pd.DataFrame({
            "Hours": list(range(24)),
            "Bin Usage (%)": np.random.randint(40, 100, 24)
        })
        st.line_chart(data.set_index("Hours"))

    with tab3:
        # Cleaner Performance tab content
        cleaner_data = pd.DataFrame({
            "Cleaner": ["Cleaner 1", "Cleaner 2", "Cleaner 3", "Cleaner 4"],
            "Tasks Completed": np.random.randint(5, 15, 4)
        })
        st.bar_chart(cleaner_data.set_index("Cleaner"))

    with tab4:
        # Bin Status & Alerts tab content
        st.map(pd.DataFrame({
            "lat": [12.9716, 12.9352, 12.9081],
            "lon": [77.5946, 77.6141, 77.6476]
        }))
        st.warning("⚠️ Bin 18 has been full for over 3 hours.")

    with tab5:
        # User Management tab content
        st.subheader("Manage Users")
        st.write("Add or modify user roles and permissions here.")
        # Placeholder for adding/editing users
        st.text_input("New User Name")
        st.selectbox("Role", ["Admin", "Cleaner"])
        st.text_input("Password")
        st.button("Add User")

    with tab6:
        # Reports tab content
        st.subheader("Generate Reports")
        st.write("Download detailed reports for performance and system activities.")
        st.button("Generate Report")

    with tab7:
        # Settings tab content
        st.subheader("Dashboard Settings")
        st.write("Change dashboard preferences such as theme or notification settings.")
        # Placeholder for setting customization
        st.selectbox("Theme", ["Light", "Dark"])
        st.checkbox("Enable Email Notifications")

    # Logout button
    st.button("Logout", on_click=logout)

# Cleaner Dashboard (as placeholder, modify as needed)
def cleaner_dashboard():
    st.title("Cleaner Dashboard")
    st.write("Cleaner dashboard content here.")
    st.button("Logout", on_click=logout)

# Main Logic
if not st.session_state.logged_in:
    login()
else:
    if st.session_state.role == "Admin":
        admin_dashboard()
    elif st.session_state.role == "Cleaner":
        cleaner_dashboard()
