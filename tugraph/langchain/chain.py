from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

# 创建LLM
llm = ChatOpenAI(model_name='gpt-4')

# 创建Prompt
prompt = ChatPromptTemplate.from_template("{question}")

# 创建输出解析器
output_parser = StrOutputParser()

# 创建Chain
chain = {"question": RunnablePassthrough()} | prompt | llm | output_parser

# 调用Chain
answer = chain.invoke('什么是图计算？')
print(answer)