# 진짜 README

Python 3.11.9 (아마 버전 상관 없을듯)

### 패키지 설치

```bash
pip install -r requirements.txt
```

</br></br>

### 사용법

prompts.py에서 프롬프트를 작성

```python
# prompts.py
default = """
당신은 뛰어난 Python 프로그래머입니다.
사용자가 제시한 실험 주제에 맞는 Python 코드를 작성하세요.
- 코드 외에는 아무런 설명도 추가하지 마세요.
- 기타 등등등

실험 주제: {experiment_desc}

Python 코드:
"""

your_prompt = """
당신은 FANGA 출신의 시니어 개발자입니다.
실험을 위한 테스트 코드를 작성해주세요.

실험 주제: {experiment_desc}

Python 코드:
"""
```

promtps.py에 초기화 한 문자열 변수를 모듈로</br>
main.py에서 불러온다다 

```python
# main.py

# model 
llm = ChatOpenAI(model="gpt-4o-mini")
# ex 실험 주제: {experiment_desc}   Python 코드:
prompt = ChatPromptTemplate.from_template(prompts.your_prompt)  # 리터럴에 프롬프트 입력
```