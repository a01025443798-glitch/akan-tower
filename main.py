import streamlit as st
import yfinance as ticker

# 1. 페이지 설정
st.set_page_config(page_title="통합 관제탑", layout="wide")

# 2. 사이드바 메뉴 (아칸다와 수이 선택)
st.sidebar.title("📡 관제탑 메뉴")
mode = st.sidebar.radio("종목 선택", ["🚀 AKAN (아칸다)", "💧 SUI (수이 코인)"])

# 3. 데이터 로드 함수
def get_stock_data(symbol):
    data = ticker.download(symbol, period="1d", interval="1min")
    return data.iloc[-1]

# --- 모드 1: 아칸다 (내일 본 게임용) ---
if mode == "🚀 AKAN (아칸다)":
    st.title("🚀 아칸다(AKAN) 전략 관제탑")
    try:
        current_data = get_stock_data("AKAN")
        price = current_data['Close']
        st.metric("현재 AKAN 단가", f"${price:.2f}")
        
        st.subheader("⚠️ 전략 가이드")
        if price >= 180:
            st.error("🚨 [매도] 200달러 하단 털기 주의! 50% 수익실현 하세요.")
        elif price <= 60:
            st.success("✅ [매수] 50달러 지지선 확인! 탄피 25% 투입 시점.")
        else:
            st.warning("⏳ 현재 세력 눈치싸움 중 (관망)")
            
    except:
        st.write("❌ 현재 나스닥 시장이 닫혀있습니다. (마지막 가격 대기 중)")

# --- 모드 2: 수이 코인 (지금 연습용) ---
elif mode == "💧 SUI (수이 코인)":
    st.title("💧 수이(SUI) 실시간 연습장")
    try:
        current_data = get_stock_data("SUI-USD")
        price = current_data['Close']
        st.metric("현재 SUI 가격", f"${price:.4f}")
        
        st.info("💡 힌트: 코인은 24시간 움직이므로 지금 바로 테스트 가능합니다.")
        
        # 연습용 가상 신호
        if price >= 2.0:
            st.error("연습용 신호: 고점 통과 중!")
        else:
            st.success("연습용 신호: 현재 매수 가능 구간!")
            
    except:
        st.write("데이터 로딩 중...")

st.sidebar.divider()
st.sidebar.write("📅 스페이스X 상장 D-Day: 2026-06-12")
