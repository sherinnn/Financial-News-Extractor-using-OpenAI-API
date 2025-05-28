import streamlit as st
from llm_extractor import extract_financial_data

st.set_page_config(page_title="📊 Financial Data Extractor", layout="centered")
st.title("💼 Financial Data Extractor from News")
st.markdown("This tool will extract core stock information such as revenue and EPS from any financial news article! 📈")

input_text = st.text_area("📰 News Article", height=300, placeholder="e.g. Tesla reported 30B in revenue...")

if st.button("✨ Extract Financial Data"):
    if input_text.strip() == "":
        st.warning("Please enter some news text first!")
    else:
        with st.spinner("Crunching numbers..."):
            df = extract_financial_data(input_text)
            st.success("Here’s the structured output")
            st.dataframe(df, use_container_width=True)
