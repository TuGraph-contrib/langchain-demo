from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, \
    HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI

# 创建LLM
llm = ChatOpenAI(model_name='gpt-4')

# 创建Prompt
prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name='chat_history'),
    HumanMessagePromptTemplate.from_template('{question}')
])

# 创建Memory
memory = ConversationBufferMemory(memory_key='chat_history',
                                  return_messages=True)
# 创建LLMChain
llm_chain = LLMChain(llm=llm, memory=memory, prompt=prompt)

# 调用LLMChain
print(llm_chain.predict(question='什么是图计算？'))
print(llm_chain.predict(question='刚才我问了什么问题？'))
