import streamlit as st
import json
import urllib.request

st.set_page_config(page_title="SUI 실시간")
st.title("💧 SUI 실시간 시세 (직통 채널)")

def get_sui_price():
    try:
        # 브라우저인 것처럼 속여서 데이터를 가져오는 헤더 추가 (차단 방지)
        url = "https://api.binance.com/api/v3/ticker/price?symbol=SUIUSDT"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return float(data['price'])
    except Exception as e:
        return None

price = get_sui_price()

if price:
    st.success(f"데이터 연결 성공!")
    st.metric(label="현재 SUI 가격", value=f"${price:.4f}")
else:
    st.error("데이터 서버와 통신이 원활하지 않습니다.")
    st.info("해결 방법: 오른쪽 하단 'Manage app' -> 'Reboot app'을 눌러주세요.")

if st.button('🔄 다시 불러오기'):
    st.rerun()
