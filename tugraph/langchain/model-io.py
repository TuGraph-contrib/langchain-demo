from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# 创建LLM
llm = ChatOpenAI(model_name='gpt-4')

# 创建Prompt
prompt = ChatPromptTemplate.from_template("{question}")

# 创建输出解析器
output_parser = StrOutputParser()

# 调用LLM
message = prompt.invoke({'question': '什么是图计算？'})
response = llm.invoke(message)
answer = output_parser.invoke(response)
print(answer)