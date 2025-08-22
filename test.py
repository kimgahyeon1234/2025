import streamlit as st

# ---- 앱 기본 설정 ----
st.set_page_config(page_title="🚓 범죄 신고 시뮬레이터 📞", page_icon="🚨")
st.title("🚓 범죄 신고 시뮬레이터 📞")
st.markdown("가상의 상황을 선택하고, 경찰에 어떻게 신고해야 하는지 연습해보세요! 📝")

# ---- 안전한 rerun (신/구 버전 호환) ----
def safe_rerun():
    try:
        st.rerun()  # 최신 버전
    except AttributeError:
        try:
            st.experimental_rerun()  # 구버전
        except AttributeError:
            pass  # 최후의 방어: rerun이 없어도 앱은 동작

# ---- 상태 초기화 ----
defaults = {
    "step": 1,
    "case": "",
    "location": "",
    "description": "",
    "suspect": ""
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ---- 진행도 표시(선택) ----
total_steps = 5
st.progress((st.session_state.step-1)/(total_steps-1))

# ---- Step 1: 사건 유형 선택 ----
if st.session_state.step == 1:
    st.subheader("1️⃣ 사건 유형을 선택하세요")
    cases = ["도난 사건", "폭행 목격", "교통사고", "실종 신고", "기타"]
    # 이전 선택 반영
    try:
        default_index = cases.index(st.session_state.case) if st.session_state.case in cases else 0
    except ValueError:
        default_index = 0

    selected_case = st.radio(
        "신고하려는 사건은 무엇인가요?",
        cases,
        index=default_index,
        key="case_radio"
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("다음 ➡️", key="to_step2"):
            st.session_state.case = selected_case
            st.session_state.step = 2
            safe_rerun()
    with col2:
        if st.button("처음으로 🔄", key="reset1"):
            for k in defaults:
                st.session_state[k] = defaults[k]
            safe_rerun()

# ---- Step 2: 장소 입력 ----
elif st.session_state.step == 2:
    st.subheader("2️⃣ 사건이 발생한 장소를 입력하세요")
    st.text_input("예: 서울시 강남구 ○○로 123 앞", key="location")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ 이전", key="back_to_1"):
            st.session_state.step = 1
            safe_rerun()
    with col2:
        if st.button("다음 ➡️", key="to_step3"):
            if st.session_state.location.strip() == "":
                st.warning("⚠️ 장소를 입력해주세요.")
            else:
                st.session_state.step = 3
                safe_rerun()

# ---- Step 3: 상황 설명 ----
elif st.session_state.step == 3:
    st.subheader("3️⃣ 사건 상황을 간단히 설명하세요")
    st.text_area(
        "예: 검은 옷을 입은 남성이 가게 안에 들어와 금품을 훔쳤습니다.",
        key="description"
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ 이전", key="back_to_2"):
            st.session_state.step = 2
            safe_rerun()
    with col2:
        if st.button("다음 ➡️", key="to_step4"):
            if st.session_state.description.strip() == "":
                st.warning("⚠️ 상황 설명을 입력해주세요.")
            else:
                st.session_state.step = 4
                safe_rerun()

# ---- Step 4: 용의자 특징(선택) ----
elif st.session_state.step == 4:
    st.subheader("4️⃣ 용의자 특징(있다면)을 입력하세요")
    st.text_area("예: 키 약 175cm, 검은 모자 착용, 회색 점퍼", key="suspect")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ 이전", key="back_to_3"):
            st.session_state.step = 3
            safe_rerun()
    with col2:
        if st.button("신고 내용 확인하기 ✅", key="to_step5"):
            st.session_state.step = 5
            safe_rerun()

# ---- Step 5: 최종 신고 내용 ----
elif st.session_state.step == 5:
    st.subheader("📞 최종 신고 내용")
    st.write(f"**사건 유형:** {st.session_state.case or '미입력'}")
    st.write(f"**발생 장소:** {st.session_state.location or '미입력'}")
    st.write(f"**상황 설명:** {st.session_state.description or '미입력'}")
    st.write(f"**용의자 특징:** {st.session_state.suspect.strip() or '없음'}")

    st.success("✅ 위 내용을 바탕으로 침착하게 112에 신고하세요.\n- 위치(구체적 주소/랜드마크)\n- 사건 내용(언제, 무엇이, 누구에게)\n- 위험 여부(긴급성)\n- 용의자/차량 특징(있다면)\n을 또렷이 전달하면 도움이 됩니다.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ 수정하기", key="back_to_4"):
            st.session_state.step = 4
            safe_rerun()
    with col2:
        if st.button("🔄 다시 시작하기", key="reset_all"):
            for k in defaults:
                st.session_state[k] = defaults[k]
            safe_rerun()

