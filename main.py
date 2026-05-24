import streamlit as st
import pandas as pd
import yfinance as yf
import requests

# 1. 페이지 설정
st.set_page_config(page_title="통합 관제탑", layout="wide")

# 2. 데이터 엔진 (주식용 & 코인용)
def get_stock_price(symbol):
    try:
        data = yf.download(symbol, period="1d", interval="1min", progress=False)
        return float(data.iloc[-1]['Close']) if not data.empty else None
    except: return None

def get_crypto_price(symbol):
    try:
        # 바이낸스 API 직접 연결 (야후보다 훨씬 빠름)
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT"
        return float(requests.get(url, timeout=5).json()['price'])
    except: return None

# 3. 사이드바 구성
st.sidebar.title("📡 모니터링 선택")
mode = st.sidebar.radio("종목", ["🚀 AKAN (아칸다)", "💧 SUI (수이 코인)"])

# 4. 메인 화면
if mode == "🚀 AKAN (아칸다)":
    st.title("🚀 아칸다(AKAN) 전략 관제탑")
    price = get_stock_price("AKAN")
    if price:
        st.metric("현재 AKAN 가격", f"${price:.2f}")
        if price >= 180: st.error("🚨 고점! 수익실현 검토")
        elif price <= 60: st.success("✅ 저점! 추가매수 검토")
    else:
        st.info("시장이 닫혀있습니다. (마지막 가격 대기 중)")

else:
    st.title("💧 수이(SUI) 실시간 연습장")
    price = get_crypto_price("SUI")
    if price:
        st.metric("SUI 실시간 시세", f"${price:.4f}")
        st.success("✅ 실시간 연결 성공! (Binance 데이터)")
        st.write("화면을 새로고침할 때마다 가격이 즉시 변합니다.")
    else:
        st.error("데이터 연결 실패. 인터넷 연결을 확인해 주세요.")

st.divider()
if st.button('🔄 시세 새로고침'):
    st.rerun()
