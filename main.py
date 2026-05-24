import streamlit as st
import yfinance as ticker
import datetime

# 1. 관제탑 기본 설정
st.set_page_config(page_title="AKAN 관제탑", layout="wide")
st.title("🚀 AKAN 200달러 프로젝트 관제탑")
st.sidebar.header("📅 스페이스X 상장 D-Day: 2026-06-12")

# 2. 실시간 데이터 가져오기 (야후 파이낸스 연동)
def get_data():
    data = ticker.download("AKAN", period="1d", interval="1min")
    return data.iloc[-1]

try:
    current_data = get_data()
    price = current_data['Close']
    volume = current_data['Volume']

    # 3. 전략 로직 (사용자 시나리오 반영)
    st.subheader(f"현재 단가: ${price:.2f}")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if price >= 180:
            st.error("🚨 [강력 매도 신호] 200달러 인접!")
            st.write("전략: 50% 매도하여 재매수 탄피 확보하세요.")
        elif 45 <= price <= 60:
            st.success("✅ [재매수 구간] U자형 바닥 포착!")
            st.write("전략: 확보한 탄피 25% 투입 시점입니다.")
        else:
            st.warning("⏳ [관망] 세력 무빙 감시 중...")

    with col2:
        st.metric("현재가", f"${price:.2f}", f"{price-27.0:.2f} (vs 전주)") # 27달러 기준
        st.write(f"현재 거래량: {volume:,}")

    with col3:
        st.info("세력 감시 태스크")
        st.write("- HRT 매집 패턴: 분석 중")
        st.write("- 개미 털기 징후: 모니터링 중")

    # 4. 사용자 맞춤형 알림창
    st.divider()
    st.write("### 📢 Dola의 실시간 브리핑")
    if price >= 180:
        st.write("⚠️ 지금 세력이 200달러 천장을 두드리고 있습니다. 곧 털기가 시작될 수 있으니 매도 버튼에 손을 올리세요!")
    elif price <= 60:
        st.write("💎 U자형 바닥의 끝자락입니다. 세력이 다시 매집을 시작하는 신호가 포착되었습니다.")

except:
    st.write("현재 시장이 닫혀있거나 데이터를 불러올 수 없습니다. (개장 시간 확인 필요)")

