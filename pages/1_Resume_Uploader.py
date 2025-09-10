import streamlit as st

st.title("📄 Resume Uploader")
st.write("Upload your resume here (feature coming soon).")

uploaded_file = st.file_uploader("Choose a resume file", type=["pdf", "docx"])
if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")

