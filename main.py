import streamlit as st
import yfinance as yf
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="AKAN-SUI 통합 관제탑", layout="wide")

# 2. 데이터 가져오기 (속도 최적화 버전)
@st.cache_data(ttl=60) # 1분간 데이터를 저장해 속도 향상
def get_live_data(symbol):
    try:
        # 데이터를 1분이 아닌 1일 치를 가져와서 마지막 값 추출 (더 안정적)
        df = yf.download(symbol, period="1d", interval="1min", progress=False)
        if not df.empty:
            return df.iloc[-1]
        else:
            return None
    except:
        return None

# 3. 사이드바 메뉴
st.sidebar.title("📡 모니터링 선택")
mode = st.sidebar.radio("종목", ["🚀 AKAN (아칸다)", "💧 SUI (수이 코인)"])
st.sidebar.divider()
st.sidebar.write("6/12 스페이스X 상장 D-Day")

# --- 메인 화면 로직 ---
if mode == "🚀 AKAN (아칸다)":
    st.title("🚀 아칸다(AKAN) 전략 관제탑")
    data = get_live_data("AKAN")
    
    if data is not None:
        price = float(data['Close'])
        st.metric("현재 AKAN 가격", f"${price:.2f}")
        
        # 전략 신호
        if price >= 180:
            st.error("🚨 [매도 신호] 200달러 인근! 수익 실현 준비!")
        elif price <= 60:
            st.success("✅ [매수 신호] 50달러 바닥권! 재매수 타이밍!")
        else:
            st.warning("⏳ 관망 구간: 세력의 움직임을 지켜보는 중")
    else:
        st.info("현재 시장이 닫혀있거나 데이터를 불러오는 중입니다. (월요일 오후 5시 개장)")

elif mode == "💧 SUI (수이 코인)":
    st.title("💧 수이(SUI) 실시간 연습장")
    # 코인은 SUI-USD로 검색해야 정확합니다
    data = get_live_data("SUI-USD")
    
    if data is not None:
        price = float(data['Close'])
        st.metric("현재 SUI 실시간가", f"${price:.4f}")
        
        st.subheader("🛠️ 작동 테스트")
        st.write("가격이 실시간으로 변한다면 관제탑이 정상 작동하는 것입니다.")
        
        # 가상 연습 신호 (현재가 기준 5% 변동성 테스트)
        if price >= 2.0:
            st.error("연습용 신호: 고점 돌파!")
        else:
            st.success("연습용 신호: 정상 거래 중")
    else:
        st.error("데이터 로딩 실패. 새로고침(F5)을 해주세요.")

# 하단 새로고침 안내
st.divider()
st.caption("화면을 아래로 당기거나 새로고침 버튼을 눌러 시세를 업데이트하세요.")
