import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="MBTI 진로 탐색", layout="wide")

# 제목
st.title("🌱 MBTI 기반 진로 탐색 웹앱")

# MBTI 선택
st.subheader("1. 당신의 MBTI를 선택하세요!")
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]
user_mbti = st.selectbox("MBTI 유형", mbti_types)

# MBTI별 진로 추천 데이터
career_dict = {
    "INTJ": ["전략 컨설턴트", "데이터 과학자", "연구원"],
    "ENFP": ["광고/마케팅", "창업가", "예술가"],
    "ISTJ": ["회계사", "공무원", "엔지니어"],
    "ESFP": ["배우", "디자이너", "이벤트 기획자"],
    # ... 나머지 유형도 추가 가능
}

# 결과 출력
st.subheader("2. 추천 진로")
if user_mbti in career_dict:
    st.success(f"👉 {user_mbti} 유형에게 어울리는 진로는:")
    for job in career_dict[user_mbti]:
        st.write(f"- {job}")
else:
    st.warning("아직 데이터가 부족합니다. 업데이트 예정!")

# 추가 기능
with st.expander("🔎 MBTI 유형별 특징 보기"):
    st.write("""
    - **ISTJ**: 철저하고 책임감이 강함  
    - **ENFP**: 창의적이고 열정적  
    - **INTJ**: 전략적이고 분석적  
    - **ESFP**: 사교적이고 즉흥적  
    """)
