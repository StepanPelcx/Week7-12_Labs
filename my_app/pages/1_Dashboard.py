import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Dashboard", page_icon="📋", layout="wide")

# Ensure state keys exist (in case user opens this page first)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# Guard: if not logged in, send user back
if not st.session_state.logged_in:
    st.error("You must be logged in to view the dashboard.")
    if st.button("Go to login page"):
        st.switch_page("Home.py") # back to the first page
    st.stop()

# If logged in, show dashboard content
st.title("📋 Dashboard")
#Showing success login only once
if st.session_state.show_login_success:
    st.success(f"Hello, **{st.session_state.username}**! You are logged in.")
    #making sure success login message shows only once
    st.session_state.show_login_success = False


# Sidebar logout button
with st.sidebar:
    if st.button("Log out   ➜]"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.info("You have been logged out.")
        st.switch_page("Home.py")

    if not st.session_state.logged_in:
        st.error("You must be logged in...")
        st.switch_page("Home.py")
        st.stop()

# Sidebar filters
with st.sidebar:
    st.header("Data")
    data = st.selectbox("Select the data", ["❓", "🚨Cyber incidents", "📁Datasets", "🎟️Tickets"])

#Dashboard layout if no data were selected
if data == "❓":
    st.caption("**Please select data to continue.**")

