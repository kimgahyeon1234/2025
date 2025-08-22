import streamlit as st

# 앱 기본 설정
st.set_page_config(page_title="🚓 범죄 신고 시뮬레이터 📞", page_icon="🚨")
st.title("🚓 범죄 신고 시뮬레이터 📞")
st.markdown("가상의 상황을 선택하고, 경찰에 어떻게 신고해야 하는지 연습해보세요! 📝")

# 단계 저장용 세션 상태
if "step" not in st.session_state:
    st.session_state.step = 1
if "case" not in st.session_state:
    st.session_state.case = None
if "location" not in st.session_state:
    st.session_state.location = ""
if "description" not in st.session_state:
    st.session_state.description = ""
if "suspect" not in st.session_state:
    st.session_state.suspect = ""

# Step 1: 사건 유형 선택
if st.session_state.step == 1:
    st.subheader("1️⃣ 사건 유형을 선택하세요")
    case = st.radio(
        "신고하려는 사건은 무엇인가요?",
        ["도난 사건", "폭행 목격", "교통사고", "실종 신고", "기타"]
    )
    if st.button("다음 ➡️"):
        st.session_state.case = case
        st.session_state.step = 2
        st.experimental_rerun()

# Step 2: 장소 입력
elif st.session_state.step == 2:
    st.subheader("2️⃣ 사건이 발생한 장소를 입력하세요")
    location = st.text_input("예: 서울시 강남구 ○○로 123 앞", st.session_state.location)

    if st.button("다음 ➡️"):
        if location.strip() == "":
            st.warning("⚠️ 장소를 입력해주세요.")
        else:
            st.session_state.location = location
            st.session_state.step = 3
            st.experimental_rerun()

# Step 3: 상황 설명
elif st.session_state.step == 3:
    st.subheader("3️⃣ 사건 상황을 간단히 설명하세요")
    description = st.text_area("예: 검은 옷을 입은 남성이 가게 안에 들어와 금품을 훔쳤습니다.", st.session_state.description)

    if st.button("다음 ➡️"):
        if description.strip() == "":
            st.warning("⚠️ 상황 설명을 입력해주세요.")
        else:
            st.session_state.description = description
            st.session_state.step = 4
            st.experimental_rerun()

# Step 4: 용의자 특징 입력
elif st.session_state.step == 4:
    st.subheader("4️⃣ 용의자 특징(있다면)을 입력하세요")
    suspect = st.text_area("예: 키 약 175cm, 검은 모자 착용, 회색 점퍼", st.session_state.suspect)

    if st.button("신고 내용 확인하기 ✅"):
        st.session_state.suspect = suspect
        st.session_state.step = 5
        st.experimental_rerun()

# Step 5: 최종 신고 내용 정리
elif st.session_state.step == 5:
    st.subheader("📞 최종 신고 내용")
    st.write(f"**사건 유형:** {st.session_state.case}")
    st.write(f"**발생 장소:** {st.session_state.location}")
    st.write(f"**상황 설명:** {st.session_state.description}")
    if st.session_state.suspect.strip():
        st.write(f"**용의자 특징:** {st.session_state.suspect}")
    else:
        st.write("**용의자 특징:** 없음")

    st.success("✅ 이제 위 내용을 바탕으로 112에 신고할 수 있습니다.")

    if st.button("🔄 다시 시작하기"):
        st.session_state.step = 1
        st.session_state.case = None
        st.session_state.location = ""
        st.session_state.description = ""
        st.session_state.suspect = ""
        st.experimental_rerun()

