from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, \
    HumanMessagePromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

# 创建LLM
llm = ChatOpenAI(model_name='gpt-4')

# 创建输出解析器
output_parser = StrOutputParser()

# 创建Prompt
prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessagePromptTemplate.from_template("{question}")
])

# 创建Chain
chain = prompt | llm | output_parser

# 添加History
history = ChatMessageHistory()
chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: history,
    input_messages_key="question",
    history_messages_key="chat_history",
)

# 调用Chain
print(chain_with_history.invoke({'question': '什么是图计算？'},
                                config={"configurable": {"session_id": None}}))
print(chain_with_history.invoke({'question': '刚才我问了什么问题？'},
                                config={"configurable": {"session_id": None}}))
