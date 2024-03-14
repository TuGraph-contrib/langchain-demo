import random

from langchain.agents import create_openai_tools_agent, \
    AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, \
    HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

# 创建LLM
llm = ChatOpenAI()


# 定义Tool
@tool
def get_temperature(city: str) -> int:
    """获取指定城市的当前气温"""
    return random.randint(-20, 50)


# 获取提示词
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template('You are a helpful assistant'),
    MessagesPlaceholder(variable_name='chat_history', optional=True),
    HumanMessagePromptTemplate.from_template('{input}'),
    MessagesPlaceholder(variable_name='agent_scratchpad')
])

# 创建Agent
tools = [get_temperature]
agent = create_openai_tools_agent(llm, tools, prompt=prompt)

# 执行Agent
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
print(agent_executor.invoke({'input': '今天杭州多少度？'})['output'])
