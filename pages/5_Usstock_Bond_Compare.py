import streamlit as st
import plotly.graph_objs as go
import re
from datetime import date
from packages.StockHistoricalData import stockDataFromDD
from packages.StockBondData import stockBondsDataFromDD

st.set_page_config(page_title="株価・金利比較チャート", layout="wide")

rep = r"^[a-zA-Z]{1,5}$"

st.sidebar.title("株価・金利比較チャート")
ticker = st.session_state.ticker
# ticker = st.sidebar.text_input("ティッカー", max_chars=5)
period = st.sidebar.slider("チャートの期間", min_value=1, max_value=5, value=3)
end_day = st.sidebar.date_input("チャートの最終日", date.today())
vrect_x0 = st.sidebar.date_input("強調表示開始日", date.today())
vrect_x1 = st.sidebar.date_input("強調表示終了日", date.today())
bond = "U.S. 10Y"

if re.match(rep, ticker):
    df = stockDataFromDD(ticker, period, end_day)
    df_10y = stockBondsDataFromDD(bond, period, end_day)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df["Close"], name=f"{ticker.upper()}", yaxis="y1"))
    fig.add_trace(go.Scatter(x=df_10y.index, y=df_10y["Close"], name=bond, yaxis="y2"))
    fig.add_vrect(
        x0=vrect_x0, x1=vrect_x1,
        fillcolor="#333333", opacity=0.1,
        layer="below", line_width=0,
    )
    fig.update_layout(width=1200, height=800, xaxis_rangeslider_visible=False, font_size=20,
                      yaxis1=dict(side="left",
                                  title=f"{ticker.upper()} ($)",
                                  ),
                      yaxis2=dict(side="right",
                                  title=f"{bond} (%)",
                                  showgrid=False,
                                  overlaying="y"
                                  ))
    fig.update_xaxes(rangebreaks=[dict(bounds=["sat", "sun"])])
    fig.update_yaxes(tickformat="%b")

    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("トップページでティッカーを入力してください")
