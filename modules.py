import time
import re
import memory_profiler


def run_experiment(experiment_code:str):
    start_time = time.time()
    mem_before = memory_profiler.memory_usage()[0]

    # LLM이 생성한 코드 실행 (예: 딥러닝 학습)
    exec(experiment_code)

    end_time = time.time()
    mem_after = memory_profiler.memory_usage()[0]
    
    print(f"실행 시간: {end_time - start_time} 초")
    print(f"메모리 사용량 증가: {mem_after - mem_before} MB")


def python_code_parse(python_code):
    # 정규 표현식으로 Python 코드만 추출하기
    python_code = re.search(r"```python(.*?)```", python_code, re.DOTALL)

    if python_code:
        # 추출한 Python 코드
        code = python_code.group(1).strip()
        return code
    else:
        print("Python 코드 블록을 찾을 수 없습니다.")