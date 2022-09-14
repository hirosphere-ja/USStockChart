import numpy as np
from packages.StockHistoricalData import stockDataFromToday
from packages.indicators import MACD
import plotly.graph_objects as go
import streamlit as st
import re
from datas.holidays import data

st.set_page_config(page_title="MACD - Close Price Buy & Sell Signal", layout="wide")

ticker = st.session_state.ticker

rep = r"^[a-zA-Z]{1,5}$"

def buy_sell(signal):
    Buy = []
    Sell = []
    flag = -1

    for i in range(0, len(signal)):
        # buy
        if ((signal["MACD"][i]) > (signal["SignalLine"][i])):
            Sell.append(np.nan)
            if flag != 1:
                Buy.append(signal["Close"][i])
                flag = 1
            else:
                Buy.append(np.nan)
        # sell
        elif ((signal["MACD"][i]) < (signal["SignalLine"][i])):
            Buy.append(np.nan)
            if flag != 0:
                Sell.append(signal["Close"][i])
                flag = 0
            else:
                Sell.append(np.nan)
        else:
            Buy.append(np.nan)
            Sell.append(np.nan)
    return (Buy, Sell)

def macd_chart(ticker, title=""):
    if re.match(rep, ticker):
        df = stockDataFromToday(ticker, 1)
        MACD(df)

        a = buy_sell(df)
        df["Buy_Signal_Price"] = a[0]
        df["Sell_Signal_Price"] = a[1]

        fig = go.Figure()
        fig.add_trace(go.Scatter(mode="lines", x=df.index, y=df["Close"], name="Close Price"))
        fig.add_trace(go.Scatter(mode="markers", x=df.index,
                      y=df["Buy_Signal_Price"], marker_symbol="triangle-up", marker_size=20, name="Buy Signal"))
        fig.add_trace(go.Scatter(mode="markers", x=df.index,
                      y=df["Sell_Signal_Price"], marker_symbol="triangle-down", marker_size=20, name="Sell Signal"))
        fig.update_layout(title=title, xaxis_title="Date", yaxis_title="Close Price USD ($)",
                          autosize=True, width=1200, height=800, xaxis_rangeslider_visible=False, font_size=20)
        # plt.savefig("MACD.png")
        fig.update_xaxes(
            rangebreaks=[
                dict(bounds=["sat", "mon"]),  # hide weekends
                dict(values=data)
            ]
        )
        st.plotly_chart(fig, use_container_width=True)
if ticker:
		macd_chart(ticker.upper(), f"{ticker.upper()} - MACD Close Price Buy & Sell Signal")
else:
    st.info("トップページでティッカーを入力してください")
