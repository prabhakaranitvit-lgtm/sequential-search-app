import streamlit as st
import pandas as pd
import time

# Sequential Search Function
def sequential_search(arr, key):
    for i in range(len(arr)):
        # Convert to string for flexible comparison if needed
        if str(arr[i]) == str(key):
            return i
    return -1

st.set_page_config(page_title="Sequential Search Pro", layout="centered")
st.title("🔍 Advanced Sequential Search")

# --- Data Input Section ---
st.sidebar.header("Data Settings")
upload_option = st.sidebar.radio("Choose Input Method:", ("Manual Entry", "Upload CSV"))

arr = []

if upload_option == "Manual Entry":
    raw_input = st.text_input("Enter numbers separated by commas:", "10, 23, 45, 70, 11, 15")
    # Clean and convert input to a list
    arr = [x.strip() for x in raw_input.split(",") if x.strip()]

else:
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Preview of Data:")
        st.dataframe(df.head())
        
        column = st.selectbox("Select column to search in:", df.columns)
        arr = df[column].tolist()

# --- Search Section ---
if arr:
    st.divider()
    key = st.text_input("Enter element to search for:")
    
    if st.button("Run Search"):
        with st.spinner("Searching..."):
            start = time.time()
            result = sequential_search(arr, key)
            end = time.time()
            
            duration = end - start
            
        if result != -1:
            st.success(f"**Match Found!** Element `{key}` is at index **{result}**.")
        else:
            st.error(f"**No Match Found.** `{key}` is not in the list.")
            
        st.caption(f"Search completed in {duration:.6f} seconds")
else:
    st.info("Please provide data via the sidebar to begin.")
