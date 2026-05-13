
import streamlit as st

st.title("Movie Success Predictor 🎬")

st.write("Demo-safe version (no sliders)")

budget = st.number_input("Budget (in millions)", min_value=0.0, value=50.0)
runtime = st.number_input("Runtime (minutes)", min_value=0, value=120)
rating = st.selectbox("Rating", ["G", "PG", "PG-13", "R"])

if st.button("Predict"):
    # Fake prediction logic (replace with your model)
    score = budget * 0.3 + runtime * 0.1

    if rating == "PG-13":
        score += 10

    if score > 50:
        st.success("This movie is likely to be a HIT! 🚀")
    else:
        st.warning("This movie might not perform well 😬")
