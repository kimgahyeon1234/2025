import streamlit as st

st.set_page_config(page_title="응급처치 퀴즈", page_icon="🚑", layout="centered")

st.title("🚨 응급 상황 대처 퀴즈")
st.write("응급 상황에서 올바른 행동을 퀴즈로 배워보세요! ✅")

# 상황별 문제 데이터
scenarios = {
    "🚗 교통사고": [
        {"question": "교통사고 현장에서 가장 먼저 해야 할 일은?",
         "options": ["부상자 확인", "2차 사고 방지를 위한 안전 조치", "사진 촬영"],
         "answer": "2차 사고 방지를 위한 안전 조치",
         "explanation": "🚧 비상등을 켜고, 2차 사고 방지를 위한 안전 조치가 최우선입니다."},
        {"question": "부상자가 의식이 없는 경우 가장 먼저 확인해야 하는 것은?",
         "options": ["호흡과 맥박", "출혈 여부", "휴대폰으로 신고"],
         "answer": "호흡과 맥박",
         "explanation": "💨 의식이 없으면 호흡과 맥박을 확인해야 합니다."},
        {"question": "부상자를 옮길 때 가장 중요한 원칙은?",
         "options": ["최대한 빨리 이동", "아무렇게나 들어 옮김", "척추 손상 방지를 위해 최소한으로 이동"],
         "answer": "척추 손상 방지를 위해 최소한으로 이동",
         "explanation": "⚠️ 척추 손상이 의심되므로 최소한으로만 움직여야 합니다."},
        {"question": "의식은 있지만 출혈이 심한 환자에게 해야 할 응급처치는?",
         "options": ["심폐소생술", "압박 지혈", "호흡 확인"],
         "answer": "압박 지혈",
         "explanation": "🩸 출혈 시 즉시 압박 지혈을 해야 합니다."},
        {"question": "119 신고 시 가장 중요한 정보는?",
         "options": ["부상자 이름", "목격자 신분", "사고 위치"],
         "answer": "사고 위치",
         "explanation": "📍 구조대가 도착할 수 있도록 위치를 정확히 알려야 합니다."},
        {"question": "부상자가 차량 안에 갇혀 있고 불이 나지 않은 경우 해야 할 일은?",
         "options": ["구조대가 올 때까지 기다린다", "무조건 꺼낸다", "창문을 깨서 꺼낸다"],
         "answer": "구조대가 올 때까지 기다린다",
         "explanation": "🚑 불이 나지 않았다면 섣불리 옮기지 않고 구조대를 기다립니다."},
        {"question": "경미한 사고라도 반드시 해야 하는 것은?",
         "options": ["경찰 신고 및 사고 접수", "그냥 넘어가기", "부상자 확인 없이 떠나기"],
         "answer": "경찰 신고 및 사고 접수",
         "explanation": "👮 모든 사고는 반드시 경찰에 신고해야 합니다."},
        {"question": "사고 현장 목격자로서의 최선의 행동은?",
         "options": ["119 신고 및 2차 사고 예방 조치", "동영상 촬영", "아무것도 안 하기"],
         "answer": "119 신고 및 2차 사고 예방 조치",
         "explanation": "📞 즉시 신고하고, 2차 사고를 방지해야 합니다."},
    ],
    "🔥 화상": [
        {"question": "화상 시 가장 먼저 해야 할 일은?",
         "options": ["흐르는 찬물로 10분 이상 식히기", "연고 바르기", "얼음 대기"],
         "answer": "흐르는 찬물로 10분 이상 식히기",
         "explanation": "💧 화상은 즉시 흐르는 찬물에 식혀야 합니다."},
        {"question": "물집이 생긴 경우 올바른 대처는?",
         "options": ["터뜨리기", "그대로 두기", "바늘로 제거"],
         "answer": "그대로 두기",
         "explanation": "⚠️ 물집은 감염 방지 역할을 하므로 터뜨리면 안 됩니다."},
        {"question": "화상 부위에 붙은 옷은 어떻게 해야 할까?",
         "options": ["억지로 떼어낸다", "그대로 두고 의료진에게 맡긴다", "가위로 자른다"],
         "answer": "그대로 두고 의료진에게 맡긴다",
         "explanation": "👕 억지로 떼면 피부 손상이 더 심해집니다."},
        {"question": "화상 부위가 넓으면 해야 할 일은?",
         "options": ["즉시 연고 바르기", "차가운 물에 전신 담그기", "119에 신고하고 병원 이송"],
         "answer": "119에 신고하고 병원 이송",
         "explanation": "🚑 넓은 화상은 즉시 전문 치료가 필요합니다."},
        {"question": "화상 후 통증 완화를 위해 하면 안 되는 행동은?",
         "options": ["얼음을 직접 대는 것", "찬물에 담그기", "의료기관 방문"],
         "answer": "얼음을 직접 대는 것",
         "explanation": "❌ 얼음은 피부를 손상시킬 수 있습니다."},
        {"question": "화학물질에 의한 화상의 경우 대처는?",
         "options": ["흐르는 물로 오랫동안 씻어내기", "연고 바르기", "붕대로 감싸기"],
         "answer": "흐르는 물로 오랫동안 씻어내기",
         "explanation": "💦 충분히 씻어내야 화학물질을 제거할 수 있습니다."},
        {"question": "전기 화상의 경우 반드시 확인해야 하는 것은?",
         "options": ["출혈 여부", "피부 상태만 보기", "심장 리듬 이상 여부"],
         "answer": "심장 리듬 이상 여부",
         "explanation": "⚡ 전기 화상은 심장에 영향을 줄 수 있습니다."},
        {"question": "화상 환자가 쇼크 증세를 보일 때 대처법은?",
         "options": ["다리를 올리고 119 신고", "세게 흔들어 깨우기", "찬물 더 끼얹기"],
         "answer": "다리를 올리고 119 신고",
         "explanation": "🚑 쇼크 상태일 때는 즉시 응급 이송이 필요합니다."},
    ],
    "🤕 심정지": [
        {"question": "심정지 환자를 발견하면 가장 먼저 해야 할 일은?",
         "options": ["의식 확인", "CPR 시작", "AED 찾기"],
         "answer": "의식 확인",
         "explanation": "👋 먼저 환자의 의식을 확인해야 합니다."},
        {"question": "의식이 없으면 다음 단계는?",
         "options": ["물 마시게 한다", "119 신고", "주변 구경꾼 찾기"],
         "answer": "119 신고",
         "explanation": "📞 의식이 없으면 즉시 119에 신고해야 합니다."},
        {"question": "호흡이 없으면 해야 할 일은?",
         "options": ["심폐소생술 시작", "물 뿌리기", "눕혀놓기만 하기"],
         "answer": "심폐소생술 시작",
         "explanation": "💓 호흡이 없으면 즉시 심폐소생술을 시작해야 합니다."},
        {"question": "성인 흉부압박 위치는?",
         "options": ["명치", "왼쪽 가슴", "가슴 중앙"],
         "answer": "가슴 중앙",
         "explanation": "➡️ 가슴 중앙이 올바른 압박 위치입니다."},
        {"question": "흉부 압박 깊이는?",
         "options": ["1cm", "5~6cm", "10cm"],
         "answer": "5~6cm",
         "explanation": "⚖️ 성인은 5~6cm 깊이로 눌러야 합니다."},
        {"question": "흉부 압박 속도는?",
         "options": ["분당 50회", "분당 80회", "분당 100~120회"],
         "answer": "분당 100~120회",
         "explanation": "⏱️ 올바른 속도는 분당 100~120회입니다."},
        {"question": "인공호흡과 흉부압박 비율은?",
         "options": ["10:1", "50:5", "30:2"],
         "answer": "30:2",
         "explanation": "💨 30회 압박 후 2회 인공호흡이 기본입니다."},
        {"question": "AED가 도착하면 해야 할 일은?",
         "options": ["전원 켜고 음성 지시 따르기", "바로 패드 붙이고 임의 충격", "그냥 CPR 계속하기"],
         "answer": "전원 켜고 음성 지시 따르기",
         "explanation": "🔌 전원을 켜고 음성 지시에 따라 사용해야 합니다."},
    ],
    "💉 출혈": [
        {"question": "출혈 환자에게 가장 먼저 해야 할 일은?",
         "options": ["압박 지혈", "물 마시게 하기", "심폐소생술"],
         "answer": "압박 지혈",
         "explanation": "🩸 출혈 시에는 즉시 압박 지혈을 해야 합니다."},
        {"question": "압박 지혈 시 사용하는 것은?",
         "options": ["깨끗한 천이나 거즈", "손톱", "플라스틱"],
         "answer": "깨끗한 천이나 거즈",
         "explanation": "🧻 깨끗한 천이나 거즈로 압박해야 감염을 막을 수 있습니다."},
        {"question": "지혈이 잘 안되면 어떻게 해야 할까?",
         "options": ["그냥 놔둔다", "더 세게 압박", "상처 문지르기"],
         "answer": "더 세게 압박",
         "explanation": "💪 압박 강도를 높여야 합니다."},
        {"question": "사지가 출혈 중이면 어떻게 해야 할까?",
         "options": ["상처 부위를 심장보다 높게 올린다", "아래로 내린다", "아무것도 안 한다"],
         "answer": "상처 부위를 심장보다 높게 올린다",
         "explanation": "📈 피의 흐름을 줄이기 위해 심장보다 높여야 합니다."},
        {"question": "지혈이 안되면 사용하는 것은?",
         "options": ["수건", "지혈대(압박대)", "붕대 풀기"],
         "answer": "지혈대(압박대)",
         "explanation": "🪢 지혈대를 사용해 출혈을 막습니다."},
        {"question": "코피가 날 때 올바른 자세는?",
         "options": ["눕는다", "고개를 앞으로 숙이고 콧등 압박", "고개 젖히기"],
         "answer": "고개를 앞으로 숙이고 콧등 압박",
         "explanation": "👃 코피는 앞으로 숙이고 눌러줘야 합니다."},
        {"question": "출혈 부위를 자주 확인해야 할까?",
         "options": ["네, 자주 풀어서 본다", "아니요, 압박을 유지한다", "상처 씻기"],
         "answer": "아니요, 압박을 유지한다",
         "explanation": "⛔ 압박을 풀면 출혈이 심해질 수 있습니다."},
        {"question": "과다출혈 환자의 쇼크 증상 대처는?",
         "options": ["다리를 올리고 따뜻하게 유지", "물 마시게 하기", "일으켜 세우기"],
         "answer": "다리를 올리고 따뜻하게 유지",
         "explanation": "🛏️ 쇼크 상태에서는 다리를 올려 혈액 순환을 돕습니다."},
    ],
    "😨 기도 막힘": [
        {"question": "기도가 막힌 환자에게 가장 먼저 해야 할 일은?",
         "options": ["기침 유도", "눕히기", "물 주기"],
         "answer": "기침 유도",
         "explanation": "😮 스스로 기침을 유도하는 것이 우선입니다."},
        {"question": "기침이 불가능하면 해야 할 처치는?",
         "options": ["눕히기", "하임리히법(복부 밀어올리기)", "머리 흔들기"],
         "answer": "하임리히법(복부 밀어올리기)",
         "explanation": "👊 기침이 안되면 하임리히법을 실시해야 합니다."},
        {"question": "하임리히법 압박 부위는?",
         "options": ["명치", "배꼽 위, 명치 아래", "가슴 중앙"],
         "answer": "배꼽 위, 명치 아래",
         "explanation": "📍 배꼽 위, 명치 아래가 올바른 위치입니다."},
        {"question": "하임리히법 시행 자세는?",
         "options": ["환자 뒤에 서서 양팔로 감싸기", "눕혀서 압박", "옆으로 눕히기"],
         "answer": "환자 뒤에 서서 양팔로 감싸기",
         "explanation": "🙌 환자 뒤에서 양팔로 감싸고 압박해야 합니다."},
        {"question": "기도 막힘 시 하면 안 되는 것은?",
         "options": ["등 두드리기", "손가락으로 무리하게 이물질 꺼내기", "하임리히법"],
         "answer": "손가락으로 무리하게 이물질 꺼내기",
         "explanation": "❌ 무리하게 꺼내면 더 깊이 들어갈 수 있습니다."},
        {"question": "영아의 기도 막힘 시 방법은?",
         "options": ["등을 5회 두드리고 가슴 압박 5회", "하임리히법", "눕히기만 하기"],
         "answer": "등을 5회 두드리고 가슴 압박 5회",
         "explanation": "👶 영아는 하임리히법 대신 등에 두드림과 가슴 압박을 합니다."},
        {"question": "기도 막혀 의식 잃으면 해야 할 일은?",
         "options": ["CPR 시작", "그냥 기다리기", "물 마시게 하기"],
         "answer": "CPR 시작",
         "explanation": "💔 기도가 막혀 의식이 없으면 CPR을 시작해야 합니다."},
        {"question": "기도 막힘 환자 응급조치 후 해야 할 일은?",
         "options": ["반드시 병원 이송", "그냥 귀가", "가만히 두기"],
         "answer": "반드시 병원 이송",
         "explanation": "🚑 기도가 막혔던 환자는 반드시 병원 진료를 받아야 합니다."},
    ],
}

# --- 상태 저장 ---
if "step" not in st.session_state:
    st.session_state.step = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "selected_scenario" not in st.session_state:
    st.session_state.selected_scenario = None

# --- 상황 선택 ---
situation = st.selectbox("⚡ 어떤 상황을 학습할까요?", list(scenarios.keys()))

# 새로운 상황 선택 시 초기화
if situation != st.session_state.selected_scenario:
    st.session_state.step = 0
    st.session_state.score = 0
    st.session_state.selected_scenario = situation

questions = scenarios[situation]

# --- 퀴즈 진행 ---
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
