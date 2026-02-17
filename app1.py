import streamlit as st
import pandas as pd
import time

# Page Config
st.set_page_config(page_title="Search Pro", page_icon="🔍", layout="wide")

# --- GUI / Welcome Section ---
col1, col2 = st.columns([2, 1])

with col1:
    st.title("👋 Welcome to Search Pro")
    st.subheader("High-efficiency Sequential Search Algorithm")
    st.write("""
        This tool allows you to perform sequential searches on custom datasets. 
        Whether you have a small list or a large CSV file, our algorithm will 
        locate your data and measure performance in real-time.
    """)

with col2:
    # Option 1: Use a URL for an image (Easy for GitHub/Streamlit Cloud)
    st.image("https://cdn-icons-png.flaticon.com", width=150)
    # Option 2: To use a local file, upload 'welcome.png' to GitHub and use:
    # st.image("welcome.png")

st.divider()

# --- File Upload Section ---
st.header("📂 Step 1: Upload Your Data")
uploaded_file = st.file_uploader("Choose a CSV file to get started", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")
    
    # Show Preview
    with st.expander("View Data Preview"):
        st.dataframe(df.head(10))
    
    # --- Search Section ---
    st.header("🔍 Step 2: Search Configuration")
    search_col = st.selectbox("Which column should we search in?", df.columns)
    search_key = st.text_input("Enter the value you want to find:")

    if st.button("Start Sequential Search"):
        data_list = df[search_col].astype(str).tolist()
        
        start_time = time.time()
        
        # Search Logic
        found = False
        index = -1
        for i, item in enumerate(data_list):
            if item == str(search_key):
                found = True
                index = i
                break
        
        end_time = time.time()
        
        # Results
        if found:
            st.balloons()
            st.success(f"**Found!** Value `{search_key}` is at row index **{index}**.")
        else:
            st.error(f"**Not Found.** `{search_key}` does not exist in the '{search_col}' column.")
            
        st.info(f"⚡ Execution Time: `{end_time - start_time:.6f}` seconds")

else:
    st.info("Waiting for a CSV file to be uploaded...")
