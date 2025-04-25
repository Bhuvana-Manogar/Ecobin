import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Dummy data for the dashboard
users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "cleaner1": {"password": "clean123", "role": "Cleaner"},
}
cleaner_data = pd.DataFrame({
    "Cleaner": ["Cleaner 1", "Cleaner 2", "Cleaner 3", "Cleaner 4"],
    "Tasks Completed": np.random.randint(5, 15, 4)
})

# Dummy data for Bin Locations
bin_data = pd.DataFrame({
    "Bin ID": [101, 102, 103],
    "Location": ["Location A", "Location B", "Location C"],
    "Status": ["Full", "Empty", "Full"]
})

# Dummy data for Reports
report_data = pd.DataFrame({
    "Report ID": [1, 2, 3],
    "Date": ["2025-04-20", "2025-04-21", "2025-04-22"],
    "Details": ["Bin usage details", "Cleaner performance", "Bin status"]
})

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
        .logout-button {
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 10;
            background-color: #FF6347;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
        }
        .logout-button:hover {
            background-color: #FF4500;
        }
        </style>
    """, unsafe_allow_html=True)

    
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

# Logout
def logout():
    st.session_state.logged_in = False
    st.session_state.role = None

# Admin Dashboard
def admin_dashboard():
    st.title("Admin Dashboard")
    st.write("Here you can view the status and analytics of the EcoBin system.")
    # Tabs for Admin Dashboard
    tabs = st.tabs([ "Overview", "Graphs", "Cleaner Performance", "Bin Status & Alerts", "User Management", "Reports"])
    tab1, tab2, tab3, tab4, tab5, tab6 = tabs

    with tab1:
        st.title("Overview")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Smart Bins", 150)
            st.image("ecobin_dashboard_streamlit/Screenshot 2025-04-25 191748.png", width=130, caption="Smart Bin")
        with col2:
            st.metric("Bins Full Today", 25)
            st.image("ecobin_dashboard_streamlit/Screenshot 2025-04-25 191718.png", width=130, caption="Bin Full")
        with col3:
            st.metric("Cleaners On-Duty", 12)
            st.image("ecobin_dashboard_streamlit/Screenshot 2025-04-25 191740.png", width=130, caption="Cleaner")

    with tab2:
        st.title("Bin Usage Over the Day")
        data = pd.DataFrame({
            "Hours": list(range(24)),
            "Bin Usage (%)": np.random.randint(40, 100, 24)
        })
        st.line_chart(data.set_index("Hours"))

    with tab3:
        st.title("Cleaner Performance")
        cleaner_data = pd.DataFrame({
            "Cleaner": ["Cleaner 1", "Cleaner 2", "Cleaner 3", "Cleaner 4"],
            "Tasks Completed": np.random.randint(5, 15, 4)
        })
        st.bar_chart(cleaner_data.set_index("Cleaner"))

    with tab4:
        st.title("Bin Status & Alerts")
        st.map(pd.DataFrame({
            "lat": [12.9716, 12.9352, 12.9081],
            "lon": [77.5946, 77.6141, 77.6476]
        }))
        st.warning("⚠️ Bin 18 has been full for over 3 hours.")

    with tab5:
        st.subheader("Manage Users")
        st.write("Add or modify user roles and permissions here.")
        st.text_input("New User Name")
        st.selectbox("Role", ["Admin", "Cleaner"])
        st.text_input("Password")
        st.button("Add User")

    with tab6:
        st.subheader("Generate Reports")
        st.write("Download detailed reports for performance and system activities.")
        st.button("Generate Report")

# Function to display Cleaner Dashboard
def cleaner_dashboard():
    st.title("Cleaner Dashboard")
    
    # Tabs for Cleaner Dashboard
    tabs = st.tabs([ "Overview", "Tasks", "Bin Locations", "Reports", "Logout"])
    tab1, tab2, tab3, tab4, tab5 = tabs
    
    with tab1:
        st.title("Overview")
        st.write("Welcome to your Cleaner Dashboard. Here you can view your tasks, bin locations, and generate reports.")
        
# In the Cleaner Dashboard, under the Tasks tab
   with tab2:
       st.title("Tasks")
       st.write("Track the tasks completed by the cleaners.")
    
       # Task distribution data for donut chart
       task_distribution = cleaner_data.set_index("Cleaner")["Tasks Completed"]
    
       # Calculate the total tasks and completed tasks
       total_tasks = task_distribution.sum()
       completed_tasks = task_distribution.sum()  # You can modify this if you have separate data for completed/incomplete tasks
    
       # Calculate the percentage completed
       completed_percentage = (completed_tasks / total_tasks) * 100
       incomplete_percentage = 100 - completed_percentage
    
       # Donut chart
       fig, ax = plt.subplots(figsize=(6, 6))
       ax.pie([completed_percentage, incomplete_percentage], labels=['Completed', 'Incomplete'], autopct='%1.1f%%', startangle=90, colors=['#4CAF50', '#FFC107'], wedgeprops={'width': 0.3})
       ax.set_title("Task Completion Percentage")
       st.pyplot(fig)
        
    with tab3:
        st.title("Bin Locations")
        st.write("View bin status and location.")
        st.table(bin_data)
        
    with tab4:
        st.title("Reports")
        st.write("Download reports for your tasks and bin status.")
        st.table(report_data)
        
    with tab5:
        st.button("Logout", on_click=logout)

# Main Logic for Cleaner Dashboard
if st.session_state.logged_in and st.session_state.role == "Cleaner":
    cleaner_dashboard()
else:
    st.write("Please log in to access the cleaner dashboard.")

if not st.session_state.logged_in:
    login()
else:
    if st.session_state.role == "Admin":
        admin_dashboard()
    elif st.session_state.role == "Cleaner":
        cleaner_dashboard()
