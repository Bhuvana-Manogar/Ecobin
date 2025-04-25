
import streamlit as st
import pandas as pd
import numpy as np
import time

# Dummy user data
users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "cleaner1": {"password": "clean123", "role": "Cleaner"}
}

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None

def login():
    st.title("EcoBin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in users and users[username]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.role = users[username]["role"]
        else:
            st.error("Invalid credentials")

def logout():
    st.session_state.logged_in = False
    st.session_state.role = None

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

# Main logic
if not st.session_state.logged_in:
    login()
else:
    if st.session_state.role == "Admin":
        admin_dashboard()
    elif st.session_state.role == "Cleaner":
        cleaner_dashboard()
