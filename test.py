import streamlit as st
import pandas as pd
import yfinance as yf
import datetime as dt

st.write(""" 
# Stock price app
Visualize your favorite stock 

""")

ticker = st.text_input("Type ticker here")
ticker_data = yf.Ticker(ticker.upper())

col1, col2 = st.beta_columns(2)

with col1:
    start_date = st.date_input("Start date")

with col2:
    end_date = st.date_input("End date")


tickerDf = ticker_data.history(
    period='1d', start=start_date, end=end_date)

st.area_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
