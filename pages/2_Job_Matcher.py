import streamlit as st

st.title("🔍 Job Matcher")
st.write("Match your resume with job descriptions (feature coming soon).")

job_description = st.text_area("Paste a job description here")
if job_description:
    st.info("Job description received (matching logic will be added soon).")

