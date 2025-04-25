import streamlit as st
import pandas as pd
import numpy as np

# Dummy user data
users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "cleaner1": {"password": "clean123", "role": "Cleaner"}
}

# Session state initialization
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None

# Styled Login and Admin Background
def set_background():
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(to right, #A2C2E9, #77A4D4);
            height: 100vh;
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .main-container {
            width: 100%;
            padding: 20px;
        }
        .logout-button {
            position: absolute;
            top: 10px;
            right: 10px;
            background-color: #FFBC00;
            color: #ffffff;
            border: none;
            padding: 10px 20px;
            font-size: 14px;
            cursor: pointer;
            border-radius: 5px;
        }
        .logout-button:hover {
            background-color: #FF9F00;
        }
        </style>
    """, unsafe_allow_html=True)

def logout():
    st.session_state.logged_in = False
    st.session_state.role = None
    # Do not rerun here; instead, just clear the session data

# Login function
def login():
    st.title("EcoBin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in users and users[username]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.role = users[username]["role"]
            st.experimental_set_query_params(logged_in=True)  # Update URL with query params
            st.session_state.logged_in = True
        else:
            st.error("Invalid credentials")

# Admin Dashboard with styled background
def admin_dashboard():
    set_background()  # Apply background style

    st.title("Admin Dashboard")

    # Add Logout Button in top-right corner
    st.markdown('<button class="logout-button" onclick="window.location.reload();">Logout</button>', unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs([  # Create tabs for different sections
        "Overview", "Graphs", "Images", "Cleaner Performance", "Smart Bin Map & Alerts"
    ])

    # Tab 1: Overview
    with tab1:
        st.metric("Total Smart Bins", 150)
        st.metric("Bins Full Today", 25)
        st.metric("Cleaners On-Duty", 12)

    # Tab 2: Graphs
    with tab2:
        data = pd.DataFrame({
            "Hours": list(range(24)),
            "Bin Usage (%)": np.random.randint(40, 100, 24)
        })
        st.line_chart(data.set_index("Hours"))

    # Tab 3: Images
    with tab3:
        st.image("https://cdn.pixabay.com/photo/2016/02/19/11/53/recycling-1206674_1280.jpg", caption="Smart Bin Monitor")
        st.image("https://cdn.pixabay.com/photo/2014/04/02/10/55/bin-306448_1280.png", caption="Bin Levels")

    # Tab 4: Cleaner Performance
    with tab4:
        st.subheader("Cleaner Task Completion")
        cleaner_data = pd.DataFrame({
            "Cleaner": ["Cleaner 1", "Cleaner 2", "Cleaner 3", "Cleaner 4"],
            "Tasks Completed": np.random.randint(5, 15, 4)
        })
        st.bar_chart(cleaner_data.set_index("Cleaner"))

    # Tab 5: Smart Bin Map & Alerts
    with tab5:
        st.subheader("Bin Status Map")
        st.map(pd.DataFrame({
            "lat": [12.9716, 12.9352, 12.9081, 12.9200],
            "lon": [77.5946, 77.6141, 77.6476, 77.6200]
        }))
        st.warning("⚠️ Bin 18 has been full for over 3 hours.")
        st.warning("⚠️ Bin 27 is nearing capacity. Dispatch a cleaner soon.")

# Cleaner Dashboard
def cleaner_dashboard():
    st.title("Cleaner Dashboard")

    tab1, tab2 = st.tabs(["Assigned Tasks", "Route & Bins"])

    # Tab 1: Assigned Tasks
    with tab1:
        st.success("You are assigned to: Bin 12, Bin 18, Bin 27")
        st.progress(65)

    # Tab 2: Route & Bins
    with tab2:
        st.map(pd.DataFrame({
            "lat": [12.9716, 12.9352, 12.9081],
            "lon": [77.5946, 77.6141, 77.6476]
        }))
        st.image("https://cdn.pixabay.com/photo/2017/07/12/15/58/recycle-2492039_1280.png", caption="Bin Locations")

    st.button("Logout", on_click=logout)  # Logout button for cleaner

# Main Logic
if not st.session_state.logged_in:
    login()  # Display the login page if not logged in
else:
    if st.session_state.role == "Admin":
        admin_dashboard()  # Display the Admin dashboard
    elif st.session_state.role == "Cleaner":
        cleaner_dashboard()  # Display the Cleaner dashboard
