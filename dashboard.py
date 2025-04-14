import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(
    page_title="Aurelius Terminal",
    page_icon="📈",
    layout="wide"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

    html, body, div, span, input, label, section, h1, h2, h3, h4, h5, h6, p {
        font-family: 'Press Start 2P', monospace !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Aurelius Terminal")

ticker = st.text_input("Enter a stock ticker (e.g. AAPL)", "AAPL")

if ticker:
    stock = yf.Ticker(ticker)

       st.subheader("Company Info")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Name:** {stock.info.get('longName', 'N/A')}")
        st.write(f"**Sector:** {stock.info.get('sector', 'N/A')}")
        st.write(f"**Market Cap:** {stock.info.get('marketCap', 'N/A')}")
        st.write(f"**P/E Ratio:** {stock.info.get('trailingPE', 'N/A')}")
        st.write(f"**EPS (TTM):** {stock.info.get('trailingEps', 'N/A')}")

    with col2:
        st.write(f"**Dividend Yield:** {stock.info.get('dividendYield', 'N/A')}")
        st.write(f"**52-Week High:** {stock.info.get('fiftyTwoWeekHigh', 'N/A')}")
        st.write(f"**52-Week Low:** {stock.info.get('fiftyTwoWeekLow', 'N/A')}")
        st.write(f"**Volume:** {stock.info.get('volume', 'N/A')}")
        st.write(f"**Beta:** {stock.info.get('beta', 'N/A')}")
