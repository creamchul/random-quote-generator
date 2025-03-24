import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="랜덤 명언 생성기",
    page_icon="💬",
    layout="centered"
)

# CSS 스타일
st.markdown("""
    <style>
    .stApp {
        background-color: #f5f5f5;
    }
    .quote-card {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 20px 0;
        text-align: center;
    }
    .quote-text {
        font-size: 1.3em;
        color: #2c3e50;
        line-height: 1.6;
        margin-bottom: 15px;
    }
    .quote-author {
        color: #7f8c8d;
        font-size: 1.1em;
    }
    </style>
""", unsafe_allow_html=True)

# 명언 리스트
quotes = [
    {"text": "삶이 있는 한 희망은 있다.", "author": "키케로"},
    {"text": "산다는 것은 호흡하는 것이 아니라 행동하는 것이다.", "author": "루소"},
    {"text": "하루에 3시간을 걸으면 7년 후에 지구를 한 바퀴 돌 수 있다.", "author": "사무엘 존슨"},
    {"text": "언제나 현재에 집중할 수 있다면 행복할 것이다.", "author": "파울로 코엘료"},
    {"text": "진정으로 웃으려면 고통을 참아야 하며, 나아가 고통을 즐길 줄 알아야 한다.", "author": "찰리 채플린"},
    {"text": "직업에서 행복을 찾아라. 아니면 행복이 무엇인지 절대 모를 것이다.", "author": "엘버트 허버드"},
    {"text": "신은 용기있는 자를 결코 버리지 않는다.", "author": "켄러"},
    {"text": "피할 수 없으면 즐겨라.", "author": "로버트 엘리엇"},
    {"text": "단순하게 살아라. 현대인은 쓸데없는 절차와 일 때문에 얼마나 복잡한 삶을 살아가는가?", "author": "이드리스 샤흐"},
    {"text": "먼저 자신을 비웃어라. 다른 사람이 당신을 비웃기 전에.", "author": "엘사 맥스웰"},
    {"text": "일하는 시간과 노는 시간을 뚜렷이 구분하라.", "author": "루이사 메이 올콧"},
    {"text": "절대 어제를 후회하지 마라. 인생은 오늘의 나 안에 있고 내일은 스스로 만드는 것이다.", "author": "L.론허바드"},
    {"text": "어리석은 자는 멀리서 행복을 찾고, 현명한 자는 자신의 발치에서 행복을 키워간다.", "author": "제임스 오펜하임"},
    {"text": "너무 소심하고 까다롭게 자신의 행동을 고민하지 말라.", "author": "카네기"},
    {"text": "인생은 한 권의 책과 같다. 바보들은 대충 훑어보지만 현명한 사람들은 신중히 읽는다.", "author": "안드레 모루아"},
    {"text": "행복한 삶을 살기 위한 필수조건은 절제이다.", "author": "아리스토텔레스"},
    {"text": "가장 큰 영광은 한 번도 실패하지 않음이 아니라 실패할 때마다 다시 일어서는 데 있다.", "author": "공자"},
    {"text": "성공의 비결은 단 한 가지, 잘할 수 있는 일에 광적으로 집중하는 것이다.", "author": "톰 모나건"},
    {"text": "자신을 내 믿으라. 당신이 생각하는 것보다 당신은 더 잘할 수 있다.", "author": "오그 맨디노"},
    {"text": "평생 살 것처럼 꿈을 꾸고 오늘 죽을 것처럼 살아라.", "author": "제임스 딘"},
    {"text": "인생에 뜻을 세우는데 있어 늦은 때라곤 없다.", "author": "볼드윈"},
    {"text": "도중에 포기하지 말라. 망설이지 말라. 최후의 성공을 거둘 때까지 밀고 나가자.", "author": "헨리포드"},
    {"text": "성공은 준비된 기회와 만나는 것이다.", "author": "보비 언서"},
    {"text": "꿈을 계속 간직하고 있으면 반드시 실현할 때가 온다.", "author": "괴테"},
    {"text": "희망을 품고 있으면 반드시 그 희망을 이룰 수 있다.", "author": "윌리엄 셰익스피어"},
    {"text": "작은 기회로부터 종종 위대한 업적이 시작된다.", "author": "데모스테네스"},
    {"text": "인생은 자전거를 타는 것과 같다. 균형을 잡으려면 움직여야 한다.", "author": "아인슈타인"},
    {"text": "행복은 습관이다. 그것을 몸에 지니라.", "author": "아리스토텔레스"},
    {"text": "성공은 결코 우연이 아니다.", "author": "호라티우스"},
    {"text": "당신이 할 수 있다고 믿든, 그렇지 않다고 믿든, 믿는 대로 될 것이다.", "author": "헨리 포드"}
]

# 제목과 설명
st.title("💬 랜덤 명언 생성기")
st.markdown("""
    <div style='text-align: center; color: #7f8c8d; margin-bottom: 30px;'>
        버튼을 클릭하면 랜덤으로 선택된 명언을 보여드립니다.
    </div>
""", unsafe_allow_html=True)

# 명언 생성 버튼
if st.button("새로운 명언 보기", type="primary"):
    quote = random.choice(quotes)
    st.markdown(f"""
        <div class="quote-card">
            <div class="quote-text">"{quote['text']}"</div>
            <div class="quote-author">- {quote['author']}</div>
        </div>
    """, unsafe_allow_html=True)

# 하단 설명
st.markdown("""
    <div style='text-align: center; margin-top: 50px; color: #95a5a6;'>
        새로운 명언을 보려면 버튼을 다시 클릭하세요.
    </div>
""", unsafe_allow_html=True) 