import yfinance as yf
import streamlit as st
import pandas as pd 

st.write('''
# Simples Stock Price App

Shown are the stock **closing price** and **volume** of Google!
''')

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# Define the ticker symbol
tickerSymbol = 'GOOGL'
# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# Get the historical prices fot this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open High   Low Close    Volume Dividensd Stock Splits

st.write('''### Closing Price ''')
st.line_chart(tickerDf.Close)

st.write('''### Volume Price ''')
st.line_chart(tickerDf.Volume)
