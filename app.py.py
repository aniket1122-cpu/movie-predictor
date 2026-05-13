st.markdown(
    """
    <style>
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        font-size: 18px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
import streamlit as st

# Title
st.set_page_config(page_title="Movie Predictor", layout="centered")

st.markdown("<h1 style='text-align: center;'>🎬 Movie Box Office Predictor</h1>", unsafe_allow_html=True)
st.markdown("---")

# Input Section
st.subheader("🎯 Enter Movie Details")

col1, col2 = st.columns(2)

with col1:
    genre = st.selectbox("🎬 Genre", ["Action", "Comedy", "Drama", "Horror", "Romance", "Sci-Fi"])
    director = st.selectbox("🎥 Director Tier", ["Emerging", "Mid-level", "Top Director"])

with col2:
    month = st.selectbox("📅 Release Month", 
                         ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    studio = st.selectbox("🏢 Studio Tier", ["Small Studio", "Medium Studio", "Major Studio"])

st.markdown("---")

# Predict Button
if st.button("🚀 Predict Box Office"):
    st.success("Prediction will appear here 🎉")
