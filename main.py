import streamlit as st
import requests

st.title("💧 SUI 실시간 시세")

# 바이낸스 거래소에서 직접 시세 가져오기
try:
    data = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=SUIUSDT").json()
    price = float(data['price'])
    
    # 큰 글씨로 가격 표시
    st.write(f"### 현재가: ${price:.4f}")
    
    if st.button('🔄 새로고침'):
        st.rerun()

except:
    st.write("연결 중입니다... 잠시 후 새로고침 버튼을 눌러주세요.")
