import random

from langchain_core.output_parsers.openai_tools import JsonOutputToolsParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


# 定义Tool
@tool
def get_temperature(city: str) -> int:
    """获取指定城市的当前气温"""
    return random.randint(-20, 50)


# 创建LLM
llm = ChatOpenAI(model_name='gpt-4')

# 创建JSON输出解析器
output_parser = JsonOutputToolsParser()

# 创建Chain
chain = (
    RunnablePassthrough()
    | llm.bind_tools(tools=[get_temperature])
    | output_parser
)

# 调用Chain
print(chain.invoke('杭州今天多少度？'))
