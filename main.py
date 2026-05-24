import streamlit as st
import requests

st.set_page_config(page_title="SUI 실시간", layout="wide")
st.title("💧 SUI 실시간 시세 (연습용)")

# 가장 확실한 바이낸스 API 사용
try:
    url = "https://api.binance.com/api/v3/ticker/price?symbol=SUIUSDT"
    res = requests.get(url, timeout=5).json()
    price = float(res['price'])
    st.metric("현재 SUI 가격", f"${price:.4f}")
    st.success("✅ 실시간 연결 성공!")
    if st.button('🔄 시세 새로고침'):
        st.rerun()
except:
    st.error("데이터를 가져오는 중입니다. 잠시 후 새로고침하세요.")
