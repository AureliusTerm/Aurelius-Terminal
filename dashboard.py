import streamlit as st
import yfinance as yf

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
    st.write(stock.info["longName"])
    st.write(f"Sector: {stock.info['sector']}")
    st.write(f"Market Cap: {stock.info['marketCap']:,}")

    st.subheader("Price Chart")
    hist = stock.history(period="6mo")
    st.line_chart(hist["Close"])
