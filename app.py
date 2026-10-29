
import streamlit as st

st.set_page_config(page_title="LaunchLab AI", page_icon="🚀")

st.markdown("""
<style>
.stApp {
    background-color: #101827;
    color: white;
}
h1, h2, p, label {
    color: white !important;
}
.stButton button {
    background-color: #B7F76A;
    color: #101827;
    border-radius: 8px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 LaunchLab AI")
st.subheader("Turn Your Ideas Into Startups")

st.write("""
Welcome to LaunchLab AI!

Have a problem you want to solve or an idea you want to explore?
Our AI will help you turn it into a startup plan.
""")

st.info("Use the page in the sidebar to generate your startup idea.")

st.markdown("---")
st.caption("Developed by Khansa Shakeel | National Incubation Center")