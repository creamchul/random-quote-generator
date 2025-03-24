import streamlit as st
import random
import json
import time

# 세션 상태 초기화
if 'liked_quotes' not in st.session_state:
    st.session_state.liked_quotes = []
if 'excluded_quotes' not in st.session_state:
    st.session_state.excluded_quotes = []
if 'custom_quotes' not in st.session_state:
    st.session_state.custom_quotes = []
if 'show_liked_quotes' not in st.session_state:
    st.session_state.show_liked_quotes = False

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
    .button-container {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: 15px;
    }
    .liked {
        color: #e74c3c;
    }
    </style>
""", unsafe_allow_html=True)

# 기본 명언 리스트
base_quotes = [
    {"text": "삶이 있는 한 희망은 있다.", "author": "키케로", "id": "base_1"},
    {"text": "산다는 것은 호흡하는 것이 아니라 행동하는 것이다.", "author": "루소", "id": "base_2"},
    {"text": "하루에 3시간을 걸으면 7년 후에 지구를 한 바퀴 돌 수 있다.", "author": "사무엘 존슨", "id": "base_3"},
    {"text": "언제나 현재에 집중할 수 있다면 행복할 것이다.", "author": "파울로 코엘료", "id": "base_4"},
    {"text": "진정으로 웃으려면 고통을 참아야 하며, 나아가 고통을 즐길 줄 알아야 한다.", "author": "찰리 채플린", "id": "base_5"},
    {"text": "직업에서 행복을 찾아라. 아니면 행복이 무엇인지 절대 모를 것이다.", "author": "엘버트 허버드", "id": "base_6"},
    {"text": "신은 용기있는 자를 결코 버리지 않는다.", "author": "켄러", "id": "base_7"},
    {"text": "피할 수 없으면 즐겨라.", "author": "로버트 엘리엇", "id": "base_8"},
    {"text": "단순하게 살아라. 현대인은 쓸데없는 절차와 일 때문에 얼마나 복잡한 삶을 살아가는가?", "author": "이드리스 샤흐", "id": "base_9"},
    {"text": "먼저 자신을 비웃어라. 다른 사람이 당신을 비웃기 전에.", "author": "엘사 맥스웰", "id": "base_10"},
    {"text": "일하는 시간과 노는 시간을 뚜렷이 구분하라.", "author": "루이사 메이 올콧", "id": "base_11"},
    {"text": "절대 어제를 후회하지 마라. 인생은 오늘의 나 안에 있고 내일은 스스로 만드는 것이다.", "author": "L.론허바드", "id": "base_12"},
    {"text": "어리석은 자는 멀리서 행복을 찾고, 현명한 자는 자신의 발치에서 행복을 키워간다.", "author": "제임스 오펜하임", "id": "base_13"},
    {"text": "너무 소심하고 까다롭게 자신의 행동을 고민하지 말라.", "author": "카네기", "id": "base_14"},
    {"text": "인생은 한 권의 책과 같다. 바보들은 대충 훑어보지만 현명한 사람들은 신중히 읽는다.", "author": "안드레 모루아", "id": "base_15"},
    {"text": "행복한 삶을 살기 위한 필수조건은 절제이다.", "author": "아리스토텔레스", "id": "base_16"},
    {"text": "가장 큰 영광은 한 번도 실패하지 않음이 아니라 실패할 때마다 다시 일어서는 데 있다.", "author": "공자", "id": "base_17"},
    {"text": "성공의 비결은 단 한 가지, 잘할 수 있는 일에 광적으로 집중하는 것이다.", "author": "톰 모나건", "id": "base_18"},
    {"text": "자신을 내 믿으라. 당신이 생각하는 것보다 당신은 더 잘할 수 있다.", "author": "오그 맨디노", "id": "base_19"},
    {"text": "평생 살 것처럼 꿈을 꾸고 오늘 죽을 것처럼 살아라.", "author": "제임스 딘", "id": "base_20"},
    {"text": "인생에 뜻을 세우는데 있어 늦은 때라곤 없다.", "author": "볼드윈", "id": "base_21"},
    {"text": "도중에 포기하지 말라. 망설이지 말라. 최후의 성공을 거둘 때까지 밀고 나가자.", "author": "헨리포드", "id": "base_22"},
    {"text": "성공은 준비된 기회와 만나는 것이다.", "author": "보비 언서", "id": "base_23"},
    {"text": "꿈을 계속 간직하고 있으면 반드시 실현할 때가 온다.", "author": "괴테", "id": "base_24"},
    {"text": "희망을 품고 있으면 반드시 그 희망을 이룰 수 있다.", "author": "윌리엄 셰익스피어", "id": "base_25"},
    {"text": "작은 기회로부터 종종 위대한 업적이 시작된다.", "author": "데모스테네스", "id": "base_26"},
    {"text": "인생은 자전거를 타는 것과 같다. 균형을 잡으려면 움직여야 한다.", "author": "아인슈타인", "id": "base_27"},
    {"text": "행복은 습관이다. 그것을 몸에 지니라.", "author": "아리스토텔레스", "id": "base_28"},
    {"text": "성공은 결코 우연이 아니다.", "author": "호라티우스", "id": "base_29"},
    {"text": "당신이 할 수 있다고 믿든, 그렇지 않다고 믿든, 믿는 대로 될 것이다.", "author": "헨리 포드", "id": "base_30"}
]

# 모든 명언 합치기 (기본 명언 + 사용자 추가 명언)
all_quotes = base_quotes + st.session_state.custom_quotes

# 제목과 설명
st.title("💬 랜덤 명언 생성기")
st.markdown("""
    <div style='text-align: center; color: #7f8c8d; margin-bottom: 30px;'>
        버튼을 클릭하면 랜덤으로 선택된 명언을 보여드립니다.
    </div>
""", unsafe_allow_html=True)

# 검색 기능
search_query = st.text_input("🔍 명언 검색", placeholder="명언이나 작성자로 검색해보세요...")
if search_query:
    search_query = search_query.lower()
    search_results = [
        quote for quote in all_quotes 
        if search_query in quote['text'].lower() or search_query in quote['author'].lower()
    ]
    
    if search_results:
        st.markdown(f"### 📝 검색 결과 ({len(search_results)}개)")
        for quote in search_results:
            st.markdown(f"""
                <div class="quote-card">
                    <div class="quote-text">"{quote['text']}"</div>
                    <div class="quote-author">- {quote['author']}</div>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("검색 결과가 없습니다.")

# 사이드바에 명언 추가 폼
with st.sidebar:
    st.header("✍️ 새로운 명언 추가")
    with st.form("add_quote_form"):
        new_quote_text = st.text_area("명언 내용")
        new_quote_author = st.text_input("작성자")
        submit_button = st.form_submit_button("명언 추가")
        
        if submit_button and new_quote_text and new_quote_author:
            new_quote = {
                "text": new_quote_text,
                "author": new_quote_author,
                "id": f"custom_{len(st.session_state.custom_quotes)}"
            }
            st.session_state.custom_quotes.append(new_quote)
            st.success("새로운 명언이 추가되었습니다! 🎉")
            st.balloons()
            st.rerun()

# 수동으로 명언 추가
with st.expander("📝 직접 명언 추가하기"):
    new_quote_text = st.text_area("명언을 입력하세요")
    new_quote_author = st.text_input("작가를 입력하세요")
    
    if st.button("추가하기"):
        if new_quote_text and new_quote_author:
            # 현재 시간을 기반으로 한 고유 id 생성
            new_quote_id = f"manual_{int(time.time())}"
            new_quote = {
                "text": new_quote_text,
                "author": new_quote_author,
                "id": new_quote_id
            }
            st.session_state.custom_quotes.append(new_quote)
            st.success("새로운 명언이 추가되었습니다!")
            st.rerun()
        else:
            st.error("명언과 작가를 모두 입력해주세요.")

# 현재 표시된 명언을 세션 상태에 저장
if 'current_quote' not in st.session_state:
    st.session_state.current_quote = None

# 명언 생성 버튼
if st.button("🎲 새로운 명언 보기", type="primary"):
    # 제외된 명언을 제외한 명언 리스트 생성
    available_quotes = [q for q in all_quotes if q not in st.session_state.excluded_quotes]
    
    if available_quotes:
        st.session_state.current_quote = random.choice(available_quotes)
    else:
        st.warning("모든 명언이 제외되었습니다. 제외 목록을 초기화하시겠습니까?")
        if st.button("제외 목록 초기화"):
            st.session_state.excluded_quotes = []
            st.success("제외 목록이 초기화되었습니다!")
            st.rerun()

# 현재 명언 표시
if st.session_state.current_quote:
    quote = st.session_state.current_quote
    
    # 명언 카드 표시
    st.markdown(f"""
        <div class="quote-card">
            <div class="quote-text">"{quote['text']}"</div>
            <div class="quote-author">- {quote['author']}</div>
        </div>
    """, unsafe_allow_html=True)
    
    # 좋아요/제외 버튼
    col1, col2 = st.columns(2)
    with col1:
        if quote in st.session_state.liked_quotes:
            if st.button("❤️ 좋아요 취소", key=f"unlike_current_{quote['id']}"):
                st.session_state.liked_quotes.remove(quote)
                st.success("좋아요가 취소되었습니다!")
                st.rerun()
        else:
            if st.button("🤍 좋아요", key=f"like_{quote['id']}"):
                st.session_state.liked_quotes.append(quote)
                st.success("좋아요가 추가되었습니다!")
                st.rerun()
    
    with col2:
        if st.button("🚫 다시 보지 않기", key=f"exclude_{quote['id']}"):
            st.session_state.excluded_quotes.append(quote)
            st.session_state.current_quote = None
            st.success("해당 명언이 제외되었습니다!")
            st.rerun()

# 좋아요한 명언 목록
if st.session_state.liked_quotes:
    st.markdown("### ❤️ 좋아요한 명언")
    for quote in st.session_state.liked_quotes:
        st.markdown(f"""
            <div class="quote-card">
                <div class="quote-text">"{quote['text']}"</div>
                <div class="quote-author">- {quote['author']}</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("좋아요 취소", key=f"unlike_list_{quote['id']}"):
            st.session_state.liked_quotes.remove(quote)
            st.success("좋아요가 취소되었습니다!")
            st.rerun()

# 하단 설명
st.markdown("""
    <div style='text-align: center; margin-top: 50px; color: #95a5a6;'>
        새로운 명언을 보려면 버튼을 다시 클릭하세요.
    </div>
""", unsafe_allow_html=True) 