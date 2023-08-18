import streamlit as st
import yfinance as yf
import datetime

# st.write("# Stock price Analysis")
"# Stock price Analysis Magic"

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Please enter start date", datetime.date(2019,7,6))

with col2:
    end_date = st.date_input("Please enter end date", datetime.date(2023,7,6))


# symbol = "AAPL"
symbol = st.selectbox("Which stock symbol you want to analyse", ["AAPL","GOOG","TSLA"])

ticker_data = yf.Ticker(symbol)
ticker_df = ticker_data.history(start = start_date, end=end_date)

ticker_df

# st.dataframe(ticker_df)

"## Closing Prices"

st.line_chart(ticker_df["Close"])

"## Volume Prices"
st.line_chart(ticker_df["Volume"])


