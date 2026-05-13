import streamlit as st

# Page config
st.set_page_config(page_title="Movie Predictor", layout="centered")

# Custom button style
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

# Title
st.markdown("<h1 style='text-align: center;'>🎬 Movie Box Office Predictor</h1>", unsafe_allow_html=True)

# Description
st.markdown(
    "This system predicts movie box office performance based on genre, release timing, director experience, and production scale."
)

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

# Prediction Logic
if st.button("🚀 Predict Box Office"):

    # Base logic
    if genre == "Action" and studio == "Major Studio" and director == "Top Director":
        result = "🔥 Blockbuster (Very High Collection)"

    elif genre == "Action" and studio == "Major Studio":
        result = "💰 High Box Office"

    elif genre == "Drama" and director == "Top Director":
        result = "🎬 Critically Successful (Medium Collection)"

    elif genre == "Comedy":
        result = "😊 Decent Collection"

    elif genre == "Horror":
        result = "👻 Low to Medium Collection"

    elif genre == "Romance":
        result = "❤️ Moderate Success"

    elif genre == "Sci-Fi":
        result = "🚀 Depends on VFX & Budget (Medium to High)"

    else:
        result = "📉 Low Box Office"

    # Month boost
    if month in ["May", "Jun", "Jul", "Dec"]:
        result += " 🚀 (Peak Season Boost)"

    # Studio adjustment
    if studio == "Small Studio":
        result += " ⚠ Limited Reach"
    elif studio == "Major Studio":
        result += " 🌍 Wide Release"

    # Output
    st.markdown("## 🎯 Prediction Result")
    st.success(result)

# Footer
st.markdown("---")
st.markdown("Developed by Ansh | Uttarakhand University 🎓")
