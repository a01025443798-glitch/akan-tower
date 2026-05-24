import streamlit as st
import requests
import yfinance as yf

st.set_page_config(page_title="관제탑 연습")
st.title("📡 실시간 데이터 연결 테스트")

# 테스트용 수이(SUI) 시세 함수
def get_sui():
    try:
        # 방법 1: 바이낸스 API (매우 빠름)
        res = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=SUIUSDT", timeout=5).json()
        return float(res['price']), "Binance"
    except:
        try:
            # 방법 2: 야후 파이낸스
            data = yf.download("SUI-USD", period="1d", interval="1min", progress=False)
            return float(data.iloc[-1]['Close']), "Yahoo"
        except:
            return 1.2345, "Test(연결실패)"

price, source = get_sui()

st.metric(label=f"SUI 가격 (출처: {source})", value=f"${price:.4f}")

if st.button("🔄 시세 새로고침"):
    st.rerun()

st.write("---")
st.write("💡 이 화면이 보인다면 일단 성공입니다! 가격이 안 변하면 '새로고침'을 눌러보세요.")
