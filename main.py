import modules
import prompts

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()



# model 
llm = ChatOpenAI(model="gpt-4o-mini")
# ex 실험 주제: {experiment_desc}   Python 코드:
prompt = ChatPromptTemplate.from_template(prompts.default)  # 리터럴에 프롬프트 입력
output_parser = StrOutputParser()

# chain 연결 (LCEL)
chain = prompt | llm | output_parser


# chain 호출
print("원하는 실험을 입력하세요.")
command = input('> ')
response = chain.invoke({"experiment_desc": command})

response = modules.python_code_parse(response)
print(response)

modules.run_experiment(response)