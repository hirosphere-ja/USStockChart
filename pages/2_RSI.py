import streamlit as st
import plotly.graph_objs as go
import re
from datetime import date
from packages.investpy.StockHistoricalData import stockDataFromDD
from packages.indicators import RSI

st.set_page_config(page_title="RSI", layout="wide")

rep = r"^[a-zA-Z]{1,5}$"

ticker = st.session_state.ticker
period = st.sidebar.slider("チャートの期間", min_value=1, max_value=5, value=3)
end_day = st.sidebar.date_input("チャートの最終日", date.today())
vrect_x0 = st.sidebar.date_input("強調表示開始日", date.today())
vrect_x1 = st.sidebar.date_input("強調表示終了日", date.today())

if re.match(rep, ticker):
    df = stockDataFromDD(ticker, period, end_day)
    df = RSI(df, 14)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df.RSI14, name="RSI14"))
    fig.add_vrect(
        x0=vrect_x0, x1=vrect_x1,
        fillcolor="#333333", opacity=0.1,
        layer="below", line_width=0,
    )
    fig.update_layout(
        xaxis_rangeslider_visible=False,
        width=1200,
        height=800,
        title=f"{ticker.upper()} - RSI",
        xaxis_title="Date",
        yaxis_title="RSI",
        font_size=20,
    )

    st.plotly_chart(fig, use_container_width=True)
elif(ticker == ""):
    st.info("トップページでティッカーを入力してください")
