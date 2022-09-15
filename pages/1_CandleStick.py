import streamlit as st
import plotly.graph_objs as go
import re
from packages.investpy.StockHistoricalData import stockDataFromDD
from packages.indicators import SMA, BB
from datas.holidays import data
from datetime import date

st.set_page_config(page_title="米国株価チャート", layout="wide")

rep = r"^[a-zA-Z]{1,5}$"

ticker = st.session_state.ticker
period = st.sidebar.slider("チャートの期間", min_value=1, max_value=5, value=3)
end_day = st.sidebar.date_input("チャートの最終日", date.today())
vrect_x0 = st.sidebar.date_input("強調表示開始日", date.today())
vrect_x1 = st.sidebar.date_input("強調表示終了日", date.today())

fill_on = st.sidebar.checkbox("ボリンジャーバンド背景色ON")
if fill_on:
		fill_on = "tonexty"
else:
    fill_on = None

if re.match(rep, ticker):
    df = stockDataFromDD(ticker, period, end_day)
    df = SMA(df, 50)
    df = SMA(df, 200)
    df = BB(df, 2)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df.SMA50, name="50day SMA"))
    fig.add_trace(go.Scatter(x=df.index, y=df.SMA200, name="200day SMA"))
    fig.add_trace(go.Scatter(x=df.index, y=df.Lower, name="-2σ",
                  fill=None, line=dict(color="#2962ff")))
    fig.add_trace(go.Scatter(x=df.index, y=df.Upper, name="+2σ",
                  fill=fill_on, line=dict(color="#2962ff")))
    fig.add_trace(go.Scatter(x=df.index, y=df.STD, name="base", line=dict(color="#ff6d00")))
    fig.add_trace(
        go.Candlestick(
            name="price",
            x=df.index,
            open=df.Open,
            high=df.High,
            low=df.Low,
            close=df.Close,
            increasing_line_color="darkgreen",
            decreasing_line_color="red"
        )
    )
    fig.add_vrect(
        x0=vrect_x0, x1=vrect_x1,
        fillcolor="#333333", opacity=0.1,
        layer="below", line_width=0,
    )
    fig.update_layout(
        xaxis_rangeslider_visible=False,
        width=1200,
        height=800,
        title=f"{ticker.upper()} - 米国株価チャート",
        yaxis_title="Stock Price USD($)",
        font_size=20,
    )
    fig.update_xaxes(
        rangebreaks=[
            dict(bounds=["sat", "mon"]),  # hide weekends
            dict(values=data)
        ]
    )

    st.plotly_chart(fig, use_container_width=True)
elif(ticker == ""):
    st.info("トップページでティッカーを入力してください")
