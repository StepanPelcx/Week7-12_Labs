import streamlit as st
import pandas as pd
import numpy as np
from user_handling.verification import change_password, verify_password, validate_password

st.set_page_config(page_title="Settings", page_icon="⚙️", layout="wide")

# Ensure state keys exist (in case user opens this page first)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "show_password_change" not in st.session_state:
    st.session_state.show_password_change = False
if "confirm_password_change" not in st.session_state:
    st.session_state.confirm_password_change = False


# Guard: if not logged in, send user back
if not st.session_state.logged_in:
    st.error("You must be logged in to view the dashboard.")
    if st.button("Go to login page"):
        st.switch_page("Home.py") # back to the first page
    st.stop()

# If logged in, show dashboard content
st.title("⚙️ Settings")

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



#button for changing password
if st.button("🔐Change password"):
    st.session_state.show_password_change = True

#password change logic
if st.session_state.show_password_change:
    st.subheader("*Change password*")
    #getting info from the user
    password = st.text_input("🔑Enter your current password", type="password", key="current_password")
    new_password = st.text_input("🔒Enter your new password", type="password", key="changed_password")
    confirmation = st.text_input("🔒Confirm your new password", type="password", key="confirmation_password")

    if st.button("Change password"):
        if password == new_password:
            st.error("❌New password is the same as the old one.❌")
            st.stop()
        #verifying the current password from user
        if not verify_password(st.session_state.username, password):
            st.error("❌Incorrect current password.❌")
            st.stop()
        #checking the user input
        if new_password != confirmation:
            st.error("❌Your new password does not match❌")
            st.stop()
        #checking if the password satisfy required conditions
        if not validate_password(new_password):
            st.error("Your password must satisfy those conditions: password must have from 8 to 24 characters long.\nIt must contain at least one upper letter, one lower letter, one number, and one special character.")
            st.stop()

        #after validation confirm the user wants to change password
        st.session_state.confirm_password_change = True

    if st.session_state.confirm_password_change:
        #asking the user to confirm the change
        st.caption("⚠️Are you sure you want to change your password?⚠️")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Yes, confirm change"):
                if change_password(st.session_state.username, new_password):
                    st.success("✅Your password changed successfuly!✅")
                    st.session_state.show_password_change = False
                    del st.session_state.confirm_password_change
                    st.stop()
                else:
                    st.error("❌Failed to update the password in database.❌")
            if st.button("Cancel"):
                st.session_state.show_password_change = False
                del st.session_state.confirm_password_change
                st.stop()
    
    
