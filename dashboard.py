import streamlit as st
import yfinance as yf

st.title("Aurelius Terminal – Mini Bloomberg")

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
