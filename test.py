import streamlit as st

st.set_page_config(page_title="응급처치 퀴즈", page_icon="🚑", layout="centered")

st.title("🚨 응급 상황 대처 퀴즈")
st.write("응급 상황에서 올바른 행동을 퀴즈로 배워보세요!")

# 상황별 퀴즈 데이터
scenarios = {
    "🚗 교통사고": [
        {
            "question": "교통사고 현장에서 가장 먼저 해야 할 일은 무엇일까요?",
            "options": ["부상자에게 즉시 이동시키기", "2차 사고 방지를 위해 안전 조치하기", "사진 찍기"],
            "answer": "2차 사고 방지를 위해 안전 조치하기",
            "explanation": "🚧 먼저 비상등을 켜고, 2차 사고를 방지하기 위해 안전 조치를 해야 합니다."
        },
        {
            "question": "부상자가 의식이 없는 경우, 가장 먼저 확인해야 할 것은?",
            "options": ["호흡과 맥박", "출혈 여부", "휴대폰으로 신고"],
            "answer": "호흡과 맥박",
            "explanation": "💨 의식이 없으면 즉시 호흡과 맥박을 확인해야 합니다."
        }
    ],
    "🔥 화상": [
        {
            "question": "뜨거운 물에 화상을 입었을 때 가장 먼저 해야 할 일은?",
            "options": ["얼음을 대기", "흐르는 찬물에 10분 이상 식히기", "연고 바르기"],
            "answer": "흐르는 찬물에 10분 이상 식히기",
            "explanation": "💧 화상 시 즉시 흐르는 찬물에 충분히 식혀주는 것이 가장 중요합니다."
        },
        {
            "question": "화상 부위에 물집이 생겼다면 어떻게 해야 할까요?",
            "options": ["터트린다", "냅둔다", "바늘로 소독 후 제거한다"],
            "answer": "냅둔다",
            "explanation": "⚠️ 물집은 감염 방지 역할을 하므로 절대 터뜨리면 안 됩니다."
        }
    ],
    "🤕 심정지": [
        {
            "question": "심정지 환자를 발견하면 가장 먼저 해야 할 일은?",
            "options": ["환자를 흔들어 깨운다", "119에 신고한다", "심폐소생술을 바로 시작한다"],
            "answer": "환자를 흔들어 깨운다",
            "explanation": "👋 먼저 의식이 있는지 확인해야 합니다."
        },
        {
            "question": "심정지가 확인되면 다음 단계는 무엇일까요?",
            "options": ["AED 가져오기", "심폐소생술(CPR) 시작", "환자를 편히 눕히기"],
            "answer": "119에 신고한다",
            "explanation": "📞 의식이 없으면 즉시 119에 신고하고 구조를 요청해야 합니다."
        }
    ]
}

# 사용자 상황 선택
situation = st.selectbox("⚡ 어떤 상황을 학습할까요?", list(scenarios.keys()))

# 진행 상태 저장용 세션
if "step" not in st.session_state:
    st.session_state.step = 0
if "score" not in st.session_state:
    st.session_state.score = 0

questions = scenarios[situation]

# 퀴즈 진행
if st.session_state.step < len(questions):
    q = questions[st.session_state.step]
    st.subheader(f"문제 {st.session_state.step+1}️⃣")
    st.write(q["question"])
    
    choice = st.radio("선택하세요:", q["options"], key=f"q{st.session_state.step}")
    
    if st.button("제출", key=f"submit{st.session_state.step}"):
        if choice == q["answer"]:
            st.success("✅ 정답입니다!")
            st.session_state.score += 1
        else:
            st.error("❌ 오답입니다!")
            st.info(f"👉 정답: {q['answer']}")
        st.write(q["explanation"])
        st.session_state.step += 1
else:
    st.success(f"🎉 모든 문제를 완료했습니다! 점수: {st.session_state.score}/{len(questions)}")
    if st.button("🔄 다시 시작"):
        st.session_state.step = 0
        st.session_state.score = 0

