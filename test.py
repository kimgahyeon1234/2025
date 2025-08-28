import streamlit as st

st.set_page_config(page_title="응급처치 퀴즈", page_icon="🚑", layout="centered")

st.title("🚨 응급 상황 대처 퀴즈")
st.caption("학습 목적용입니다. 실제 응급상황에선 즉시 119에 신고하고, 지역 지침을 따르세요.")

# =============================
# 64문제 데이터: 8상황 × 8문제
# 보기 난이도를 약간 높여 헷갈리는 선택지를 포함했습니다.
# =============================
scenarios = {
    "🚗 교통사고": [
        {
            "question": "교통사고 현장에서 가장 먼저 해야 할 일은?",
            "options": [
                "부상자부터 차량 밖으로 이동시킨다",
                "2차 사고 방지를 위한 안전 조치(비상등/삼각대/안전거리 확보)",
                "블랙박스/현장 사진 촬영부터 한다",
            ],
            "answer": "2차 사고 방지를 위한 안전 조치(비상등/삼각대/안전거리 확보)",
            "explanation": "2차 사고가 발생하면 피해가 커집니다. 후방 경고와 안전거리 확보가 최우선입니다.",
        },
        {
            "question": "의식이 없는 부상자를 확인할 때 첫 순서는?",
            "options": ["출혈 확인 → 신고 → 호흡 확인", "의식 확인 → 호흡/맥박 확인", "신고 → 사진 촬영 → 이동"],
            "answer": "의식 확인 → 호흡/맥박 확인",
            "explanation": "반응 확인 후 즉시 호흡과 맥박을 평가해야 합니다.",
        },
        {
            "question": "환자를 현장에서 옮겨야 하는 합당한 경우는?",
            "options": ["추가 위험 없음", "화재/폭발 등 2차 위험", "목격자가 요청"],
            "answer": "화재/폭발 등 2차 위험",
            "explanation": "2차 위험이 임박한 경우를 제외하면 불필요한 이동은 금물입니다.",
        },
        {
            "question": "119 신고 시 우선 전달해야 할 정보는?",
            "options": ["사고 위치", "환자 상태", "현재 상황"],
            "answer": "사고 위치",
            "explanation": "정확한 위치가 구조 도착 시간을 좌우합니다.",
        },
        {
            "question": "출혈이 심한 환자에게 가장 먼저 시행할 처치는?",
            "options": ["상처 소독", "압박 지혈", "병원 이송"],
            "answer": "압박 지혈",
            "explanation": "깨끗한 천/거즈로 직접 압박하여 출혈을 우선 멈춥니다.",
        },
        {
            "question": "척추 손상이 의심되는 환자에게 적절한 대처는?",
            "options": ["자세를 편하게 바꿔준다", "절대 움직이지 않게 고정", "목만 들어 호흡을 편하게 한다"],
            "answer": "절대 움직이지 않게 고정",
            "explanation": "척추 손상이 의심되면 움직임을 최소화하고 머리·목·몸통을 일직선으로 유지해야 합니다.",
        },
        {
            "question": "화상 부위에 옷이 달라붙었다. 어떻게 할까?",
            "options": ["강제로 떼어낸다", "그대로 둔 채 의료진에게 맡긴다", "기름을 발라 떼어낸다"],
            "answer": "그대로 둔 채 의료진에게 맡긴다",
            "explanation": "무리한 제거는 조직 손상을 키웁니다. 주변부만 가위로 자르고 붙은 부분은 그대로.",
        },
        {
            "question": "넓은 범위 화상/얼굴 화상 발생 시 우선 조치로 적절한 것은?",
            "options": ["연고 도포 후 대기", "119 신고 및 신속 이송", "차가운 물에 전신을 담근다"],
            "answer": "119 신고 및 신속 이송",
            "explanation": "기도 손상/쇼크 위험이 커 즉시 전문 치료가 필요합니다.",
        },
    ],

    "❤️ 심정지": [
        {
            "question": "심정지 의심 환자 발견 시 첫 단계는?",
            "options": ["AED 찾기", "의식 확인(반응 확인)", "즉시 인공호흡"],
            "answer": "의식 확인(반응 확인)",
            "explanation": "어깨 두드리며 반응을 확인하고, 무반응이면 도움을 요청합니다.",
        },
        {
            "question": "무반응/비정상 호흡(or 무호흡) 확인 후의 조치는?",
            "options": ["119 신고 및 AED 요청", "물 마시게 하기", "회복자세"],
            "answer": "119 신고 및 AED 요청",
            "explanation": "신고와 AED 확보가 생존사슬의 핵심입니다.",
        },
        {
            "question": "성인 흉부압박 깊이는?",
            "options": ["약 2~3cm", "약 5~6cm", "10cm 이상"],
            "answer": "약 5~6cm",
            "explanation": "충분한 깊이(흉곽의 1/3 정도)를 유지합니다.",
        },
        {
            "question": "흉부압박 속도(성인)는?",
            "options": ["분당 60~80회", "분당 100~120회", "분당 140회 이상"],
            "answer": "분당 100~120회",
            "explanation": "너무 빠르면 충분한 이완이 어렵고, 느리면 관류가 떨어집니다.",
        },
        {
            "question": "압박:호흡의 비율(1인 구조자, 성인)은?",
            "options": ["15:2", "30:2", "50:5"],
            "answer": "30:2",
            "explanation": "표준 비율은 30회 압박 후 2회 인공호흡입니다(교육 이수자에 한함).",
        },
        {
            "question": "AED가 도착했다. 올바른 순서는?",
            "options": ["전원 켬 → 패드 부착 → 음성 지시 따름", "충격 버튼 먼저 누름", "패드 부착 전 가슴털 제거는 불필요"],
            "answer": "전원 켬 → 패드 부착 → 음성 지시 따름",
            "explanation": "AED의 음성 지시에 따르며, 필요한 경우 패드 부착부의 땀/털 제거.",
        },
        {
            "question": "흉부압박을 중단해도 되는 시점은?",
            "options": ["환자 자발호흡/움직임 회복", "압박자가 피곤할 때", "2분마다 반드시 중단"],
            "answer": "환자 자발호흡/움직임 회복",
            "explanation": "전문인력 인계, AED 분석/충격, 위험 제거 등의 예외를 제외하고 중단 금지.",
        },
        {
            "question": "심정지 발견 후 효과적 생존율을 높이려면 몇 분 내 압박을 시작해야 하나?",
            "options": ["1분 이내", "약 4분 이내", "10분 후"],
            "answer": "약 4분 이내",
            "explanation": "무산소 손상 전의 골든타임 확보가 핵심입니다.",
        },
    ],

    # 나머지 출혈, 기도 막힘, 익사, 동물·곤충 물림, 재난 파트는 그대로 유지
    # (위 코드에서 에러 없으니 생략)
    # ...
}

# =============================
# 세션 상태
# =============================
if "step" not in st.session_state:
    st.session_state.step = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "current" not in st.session_state:
    st.session_state.current = None

# 사이드바: 상황 선택 및 진행률
with st.sidebar:
    st.header("학습 설정")
    situation = st.selectbox("상황 선택", list(scenarios.keys()))
    total = len(scenarios[situation])
    st.progress(0 if total == 0 else st.session_state.step/total)
    st.caption("⏱️ 정답 제출 후 자동으로 다음 단계로 이동합니다.")

# 새로운 상황 선택 시 초기화
if st.session_state.current != situation:
    st.session_state.current = situation
    st.session_state.step = 0
    st.session_state.score = 0

questions = scenarios[situation]

# =============================
# 퀴즈 본문
# =============================
if st.session_state.step < len(questions):
    idx = st.session_state.step
    q = questions[idx]
    st.subheader(f"문제 {idx+1} / {len(questions)}")
    st.write(q["question"]) 

    choice = st.radio("정답을 고르세요:", q["options"], key=f"q_{situation}_{idx}")

    col1, col2 = st.columns([1,1])
    with col1:
        submit = st.button("제출", key=f"submit_{situation}_{idx}")
    with col2:
        skip = st.button("건너뛰기", key=f"skip_{situation}_{idx}")

    if submit:
        if choice == q["answer"]:
            st.success("✅ 정답입니다! 잘하셨어요.")
            st.session_state.score += 1
        else:
            st.error("❌ 오답입니다.")
            st.info(f"👉 정답: {q['answer']}")
        st.write(q["explanation"])
        st.session_state.step += 1
    elif skip:
        st.warning("⏭️ 문제를 건너뛰었습니다. 다음 문제로 이동합니다.")
        st.info(f"참고: {q['answer']}")
        st.session_state.step += 1
else:
    st.success("🎉 해당 상황의 모든 문제를 완료했습니다!")
    st.metric("점수", f"{st.session_state.score} / {len(questions)}")

    ratio = st.session_state.score / len(questions)
    if ratio == 1:
        st.balloons()
        st.write("🏆 완벽해요! 실제 상황에서도 차분히 대처하실 수 있어요.")
    elif ratio >= 0.75:
        st.write("👍 아주 잘하셨어요. 조금만 더 연습하면 완벽!")
    elif ratio >= 0.5:
        st.write("🙂 보통입니다. 틀린 문제의 해설을 복습해 보세요.")
    else:
        st.write("📚 더 연습이 필요해요. 해설을 꼼꼼히 읽고 다시 도전! 💪")

    if st.button("🔄 다시 풀기"):
        st.session_state.step = 0
        st.session_state.score = 0

st.divider()
st.caption("❗ 이 앱은 교육용이며, 실제 응급상황에서는 즉시 119에 신고하고 최신 지역 지침과 인증된 교육 내용을 따르세요.")
