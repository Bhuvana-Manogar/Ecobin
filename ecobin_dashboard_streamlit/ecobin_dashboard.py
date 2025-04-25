import streamlit as st
import pandas as pd
import numpy as np

# Dummy user data
users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "cleaner1": {"password": "clean123", "role": "Cleaner"}
    "cleaner2": {"password": "clean123", "role": "Cleaner"}
    "cleaner3": {"password": "clean123", "role": "Cleaner"}
    "cleaner4": {"password": "clean123", "role": "Cleaner"}
}

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None

# Styled Login
def login():
    st.markdown("""
        <style>
        .stApp {
            background-color: #d4edda;
            background-image: url('https://cdn.pixabay.com/photo/2017/09/01/21/47/background-2706023_1280.jpg');
            background-size: cover;
            background-position: center;
        }
        .login-box {
            background: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 12px;
            width: 350px;
            margin: 5rem auto;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }
        </style>
    """, unsafe_allow_html=True)

    
    st.title("🌿 EcoBin ")

    username = st.text_input("Name")
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

    tab1, tab2, tab3 = st.tabs(["Overview", "Graphs", "Images"])

    with tab1:
        st.metric("Total Smart Bins", 150)
        st.metric("Bins Full Today", 25)
        st.metric("Cleaners On-Duty", 12)

    with tab2:
        data = pd.DataFrame({
            "Hours": list(range(24)),
            "Bin Usage (%)": np.random.randint(40, 100, 24)
        })
        st.line_chart(data.set_index("Hours"))

    with tab3:
        st.image("https://cdn.pixabay.com/photo/2016/02/19/11/53/recycling-1206674_1280.jpg", caption="Smart Bin Monitor")
        st.image("https://cdn.pixabay.com/photo/2014/04/02/10/55/bin-306448_1280.png", caption="Bin Levels")

    st.button("Logout", on_click=logout)

# Cleaner Dashboard
def cleaner_dashboard():
    st.title("Cleaner Dashboard")

    tab1, tab2 = st.tabs(["Assigned Tasks", "Route & Bins"])

    with tab1:
        st.success("You are assigned to: Bin 12, Bin 18, Bin 27")
        st.progress(65)

    with tab2:
        st.map(pd.DataFrame({
            "lat": [12.9716, 12.9352, 12.9081],
            "lon": [77.5946, 77.6141, 77.6476]
        }))

        st.image("https://cdn.pixabay.com/photo/2017/07/12/15/58/recycle-2492039_1280.png", caption="Bin Locations")

    st.button("Logout", on_click=logout)

# Main Logic
if not st.session_state.logged_in:
    login()
else:
    if st.session_state.role == "Admin":
        admin_dashboard()
    elif st.session_state.role == "Cleaner":
        cleaner_dashboard()
