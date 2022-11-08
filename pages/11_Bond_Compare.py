import streamlit as st
import plotly.graph_objs as go
import re
from datetime import date
from datas.holidays import data
from packages.fred.StockBondData import stockBondsDataFromDD

st.set_page_config(page_title="株価・金利比較チャート", layout="wide")

st.sidebar.title("株価・金利比較チャート")

period = st.sidebar.slider("チャートの期間", min_value=1, max_value=5, value=3)
end_day = st.sidebar.date_input("チャートの最終日", date.today())
vrect_x0 = st.sidebar.date_input("強調表示開始日", date.today())
vrect_x1 = st.sidebar.date_input("強調表示終了日", date.today())
df_bond_2 = stockBondsDataFromDD(2, period, end_day)
df_bond_5 = stockBondsDataFromDD(5, period, end_day)
df_bond_10 = stockBondsDataFromDD(10, period, end_day)

fig = go.Figure()
fig.add_trace(go.Scatter(x=df_bond_2.index, y=df_bond_2["DGS2"], name="米国債券2年利回り",
							connectgaps=True,)) # 途切れたグラフを補完して繋げる
fig.add_trace(go.Scatter(x=df_bond_5.index, y=df_bond_5["DGS5"], name="米国債券5年利回り",
							connectgaps=True,)) # 途切れたグラフを補完して繋げる
fig.add_trace(go.Scatter(x=df_bond_10.index, y=df_bond_10["DGS10"], name="米国債券10年利回り",
							connectgaps=True,)) # 途切れたグラフを補完して繋げる
fig.add_vrect(x0=vrect_x0, x1=vrect_x1, fillcolor="#333333", opacity=0.1, layer="below", line_width=0)
fig.update_layout(
		xaxis_rangeslider_visible=False,
		width=1200,
		height=800,
		title="米国債券利回り比較",
		font_size=20,
)
fig.update_xaxes(rangebreaks=[
									dict(values=data),
									dict(bounds=["sat", "mon"])])
fig.update_yaxes(tickformat="%b")

st.plotly_chart(fig, use_container_width=True)
