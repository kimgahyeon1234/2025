import streamlit as st

# 앱 제목
st.set_page_config(page_title="🚦 교통 법규 퀴즈 앱 🚓", page_icon="🚓")
st.title("🚦 교통 법규 퀴즈 앱 🚓")
st.markdown("안전한 교통 문화를 위해 퀴즈를 풀어보세요! 📝")

# 퀴즈 데이터 (8문제)
quiz_data = [
    {
        "question": "신호등 없는 교차로에서 동시에 진입한 차량 A와 B가 있습니다. 누가 먼저 가야 할까요?",
        "options": ["A 차량", "B 차량", "양보 후 동시에 출발"],
        "answer": "A 차량",
        "explanation": "신호등 없는 교차로에서는 **우측에 있는 차량**이 우선권을 가집니다."
    },
    {
        "question": "횡단보도 앞에 보행자가 서 있을 때, 운전자가 해야 할 행동은?",
        "options": ["속도를 줄이지 않고 지나간다", "보행자가 건너기 시작할 때만 멈춘다", "무조건 정지한다"],
        "answer": "무조건 정지한다",
        "explanation": "보행자가 횡단보도에 있거나 건너려고 할 때 운전자는 반드시 정지해야 합니다."
    },
    {
        "question": "운전 중 휴대전화를 사용하려면 어떻게 해야 할까요?",
        "options": ["한 손으로만 조심해서 사용한다", "블루투스/핸즈프리 장치를 사용한다", "잠깐 멈춰서 급히 확인한다"],
        "answer": "블루투스/핸즈프리 장치를 사용한다",
        "explanation": "운전 중 휴대폰은 **직접 손으로 조작하면 안 되며**, 반드시 핸즈프리 장치를 사용해야 합니다."
    },
    {
        "question": "고속도로에서 앞차와의 안전거리는 어떻게 유지해야 할까요?",
        "options": ["차량 1대 거리", "시속에 따른 거리 확보 (예: 100km/h → 100m)", "상황에 따라 달라진다"],
        "answer": "시속에 따른 거리 확보 (예: 100km/h → 100m)",
        "explanation": "고속도로에서는 시속에 맞는 충분한 안전거리를 확보해야 합니다."
    },
    {
        "question": "비 오는 날 운전할 때 가장 주의해야 할 점은?",
        "options": ["속도를 줄이고 안전거리 확보", "와이퍼를 끄고 운전", "급정거 자주 하기"],
        "answer": "속도를 줄이고 안전거리 확보",
        "explanation": "빗길에서는 제동거리가 길어지므로 반드시 속도를 줄이고 거리를 확보해야 합니다."
    },
    {
        "question": "야간 운전 시 전조등을 켜야 하는 시기는?",
        "options": ["해가 완전히 진 후", "해가 지기 전 어두워지기 시작할 때", "상관없다"],
        "answer": "해가 지기 전 어두워지기 시작할 때",
        "explanation": "야간뿐만 아니라 해가 지기 전 어두워지는 시기에도 전조등을 켜야 합니다."
    },
    {
        "question": "운전 중 졸음이 쏟아질 때 가장 올바른 대처는?",
        "options": ["창문 열고 바람 쐬기", "졸음을 참으며 운전 계속하기", "휴게소나 안전한 곳에 정차 후 휴식"],
        "answer": "휴게소나 안전한 곳에 정차 후 휴식",
        "explanation": "졸음운전은 음주운전만큼 위험합니다. 반드시 안전한 곳에서 휴식을 취해야 합니다."
    },
    {
        "question": "좌회전 신호에서 직진하려고 할 때 어떻게 해야 할까요?",
        "options": ["좌회전 신호일 때 직진해도 된다", "직진 신호가 나올 때까지 기다린다", "경적을 울리고 진행한다"],
        "answer": "직진 신호가 나올 때까지 기다린다",
        "explanation": "좌회전 신호에서는 직진할 수 없습니다. 반드시 직진 신호가 켜질 때까지 기다려야 합니다."
    },
]

# 점수
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_q" not in st.session_state:
    st.session_state.current_q = 0

# 현재 문제 가져오기
if st.session_state.current_q < len(quiz_data):
    q = quiz_data[st.session_state.current_q]
    st.subheader(f"문제 {st.session_state.current_q+1}: {q['question']}")

    choice = st.radio("정답을 선택하세요:", q["options"])

    if st.button("제출하기"):
        if choice == q["answer"]:
            st.success("✅ 정답입니다!")
            st.session_state.score += 1
        else:
            st.error("❌ 오답입니다!")
        st.info(f"💡 해설: {q['explanation']}")

        st.session_state.current_q += 1
        st.experimental_rerun()

else:
    st.success(f"🎉 모든 문제를 풀었습니다! 최종 점수: {st.session_state.score}/{len(quiz_data)}")
    if st.button("다시 시작하기"):
        st.session_state.score = 0
        st.session_state.current_q = 0
        st.experimental_rerun()

