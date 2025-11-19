import streamlit as st
import pandas as pd
import numpy as np

"""
df = pd.read_csv("https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv")


st.set_page_config(page_title="My app", layout="centered")

name = st.text_input("Name")

if st.button("Submit"):
    if name:
        st.success(f"Hello, {name}!")
    else:
        st.warning("Enter name")

with st.expander("See details"):
    st.write("Hidden content")
    st.dataframe(df)
"""

df = pd.DataFrame(
    np.random.randn
)

st.set_page_config(layout="wide")
st.title("📊 Sales Dashboard")

# Sidebar filters
with st.sidebar:
    year = st.selectbox("Year", [2023, 2024, 2025])
    min_revenue = st.slider(
    "Min revenue", 0, 100000, 20000
    )

# Apply filters to data
filtered = df[(df["year"] == year) & (df["revenue"] >= min_revenue)]

# Layout with columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Revenue by Region")
    st.bar_chart(filtered)

with col2:
    st.subheader("Revenue Distribution")
    st.line_chart(filtered)

# Expandable data table
with st.expander("See filtered data"):
    st.dataframe(filtered)
