# 랜덤 명언 생성기

GPT를 활용한 감성적인 명언 생성 웹 애플리케이션입니다.

## 기능

- 사용자가 입력한 주제에 대한 감성적인 명언 3개 생성
- 카드 형식의 깔끔한 UI
- 새로운 명언 생성 기능

## 설치 방법

1. 필요한 패키지 설치:
```bash
pip install -r requirements.txt
```

2. `.env` 파일 설정:
- `.env` 파일을 열고 `your_api_key_here`를 실제 OpenAI API 키로 교체하세요.

## 실행 방법

```bash
streamlit run app.py
```

## 환경 변수

- `OPENAI_API_KEY`: OpenAI API 키 (필수) 