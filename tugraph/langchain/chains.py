from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

# 创建LLM
llm = ChatOpenAI(model_name='gpt-4')

# 创建输出解析器
output_parser = StrOutputParser()

# 创建Prompt
topic_prompt = ChatPromptTemplate.from_template("生成一种'{input}'的名称")
good_prompt = ChatPromptTemplate.from_template("列举{topic}的好处:")
bad_prompt = ChatPromptTemplate.from_template("列举{topic}的坏处:")
summary_prompt = ChatPromptTemplate.from_messages(
    [
        ("ai", "{topic}"),
        ("human", "好处:\n{good}\n\n坏处:\n{bad}"),
        ("system", "生成最终结论"),
    ]
)

# 创建组合Chain
topic_chain = topic_prompt | llm | output_parser | {"topic": RunnablePassthrough()}
goods_chain = good_prompt | llm | output_parser
bads_chain = bad_prompt | llm | output_parser
summary_chain = summary_prompt | llm | output_parser
chain = (
    topic_chain
    | {
        "good": goods_chain,
        "bad": bads_chain,
        "topic": itemgetter("topic"),
    }
    | summary_chain
)

# 打印chain的计算图
chain.get_graph().print_ascii()

# 调用chain
answer = chain.invoke({"input": '常见水果'})
print(answer)
