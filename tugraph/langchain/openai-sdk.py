from langchain_openai import ChatOpenAI

# 调用Chat Completion API
llm = ChatOpenAI(model_name='gpt-4')
response = llm.invoke('什么是图计算？')
print(response)