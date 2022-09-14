import streamlit as st
import re

st.header("米国株個別銘柄各種チャート")
st.markdown(
	'''
	米国株のティッカーを入力すると以下のチャートを見ることができます。
	1. 株価
	2. RSI
	3. MACD
	4. ストキャスティクス
	5. 株価・金利比較
	6. MACD売買シグナル
	'''
)

rep = r"^[a-zA-Z]{1,5}$"
ticker = ""

if "ticker" not in st.session_state:
	st.session_state.ticker = ""

ticker = st.text_input("ティッカー", max_chars=5)

if re.match(rep, ticker):
	st.session_state.ticker = ticker #値の更新
	st.subheader(f"{ticker.upper()}の各種チャートを表示します")
else:
	st.write("ティッカーを入力してください")

