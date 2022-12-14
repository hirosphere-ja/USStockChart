import streamlit as st
import plotly.graph_objs as go
import re
from datetime import date
from datas.holidays import data
from packages.yahoo.WTIData import WTIDataFromDD

# from packages.investpy.StockHistoricalData import stockDataFromDD
from packages.yahoo.StockHistoricalData import stockDataFromDD

st.set_page_config(page_title="株価・金利比較チャート", layout="wide")

rep = r"^[a-zA-Z]{1,5}$"

st.sidebar.title("株価・WTI原油比較チャート")

if "ticker" not in st.session_state:
	st.session_state.ticker = ""

ticker = st.session_state.ticker
period = st.sidebar.slider("チャートの期間", min_value=1, max_value=5, value=3)
end_day = st.sidebar.date_input("チャートの最終日", date.today())
vrect_x0 = st.sidebar.date_input("強調表示開始日", date.today())
vrect_x1 = st.sidebar.date_input("強調表示終了日", date.today())
bond = st.sidebar.text_input("米国債利回り年数", 10)
df_wti = WTIDataFromDD(period, end_day)

if re.match(rep, ticker):
    df = stockDataFromDD(ticker, period, end_day)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df["Close"], name=f"{ticker.upper()}", yaxis="y1"))
    fig.add_trace(go.Scatter(x=df_wti.index, y=df_wti.Close, name="WTI原油", yaxis="y2",
									connectgaps=True,)) # 途切れたグラフを補完して繋げる
    fig.add_vrect(x0=vrect_x0, x1=vrect_x1, fillcolor="#333333", opacity=0.1, layer="below", line_width=0)
    fig.update_layout(width=1200, height=800, xaxis_rangeslider_visible=False, font_size=20,
                      yaxis1=dict(side="left", title=f"{ticker.upper()} ($)"),
                      yaxis2=dict(side="right", title="WTI原油 ($)", showgrid=False, overlaying="y"))
    fig.update_xaxes(rangebreaks=[
											dict(values=data),
											dict(bounds=["sat", "mon"])])
    fig.update_yaxes(tickformat="%b")

    st.plotly_chart(fig, use_container_width=True)
elif (ticker == ""):
    st.info("トップページでティッカーを入力してください")
