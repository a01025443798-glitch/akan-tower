import streamlit as st
import yfinance as yf
import time

# 1. 페이지 설정
st.set_page_config(page_title="통합 관제탑", layout="wide")

# 2. 데이터 가져오기 함수 (실패 시 재시도 로직 추가)
def fetch_data(symbol):
    # 여러 가지 티커 형태를 시도 (코인은 거래소마다 이름이 다를 수 있음)
    tickers_to_try = [symbol, symbol.replace("-USD", "USD=X"), symbol.split("-")[0] + "-USD"]
    
    for t in tickers_to_try:
        try:
            data = yf.download(t, period="1d", interval="1min", progress=False)
            if not data.empty:
                return data.iloc[-1], t
        except:
            continue
    return None, None

# 3. 사이드바
st.sidebar.title("📡 모니터링")
mode = st.sidebar.radio("종목 선택", ["🚀 AKAN (아칸다)", "💧 SUI (수이 코인)"])

# --- 메인 화면 ---
if mode == "🚀 AKAN (아칸다)":
    st.title("🚀 아칸다 전략 관제탑")
    with st.spinner('아칸다 데이터 연결 중...'):
        data, ticker_used = fetch_data("AKAN")
        if data is not None:
            price = float(data['Close'])
            st.metric("현재 AKAN 가격", f"${price:.2f}")
            st.success(f"데이터 연결 성공 (티커: {ticker_used})")
        else:
            st.warning("현재 나스닥 시장이 휴장 중이거나 데이터를 불러올 수 없습니다.")
            st.info("개장 시간: 월요일 오후 10:30 (한국시간)")

elif mode == "💧 SUI (수이 코인)":
    st.title("💧 수이(SUI) 실시간 연습장")
    with st.spinner('수이 실시간 시세 파악 중...'):
        # 수이 코인의 다양한 이름을 시도합니다
        data, ticker_used = fetch_data("SUI-USD")
        
        if data is not None:
            price = float(data['Close'])
            st.divider()
            st.metric("SUI 실시간 시세", f"${price:.4f}", help="1분 단위 실시간 가격입니다.")
            st.write(f"✅ 연결된 티커: `{ticker_used}`")
            
            # 연습용 신호
            if price > 1.2:
                st.error("🚨 고점 알림 테스트!")
            else:
                st.success("✅ 정상 거래 범위")
        else:
            st.error("⚠️ 수이 데이터를 가져오지 못했습니다.")
            st.write("해결 방법: 1. 화면을 새로고침(F5) 해주세요. 2. 잠시 후 다시 시도해 주세요.")

st.divider()
if st.button('🔄 지금 시세 새로고침'):
    st.rerun()

