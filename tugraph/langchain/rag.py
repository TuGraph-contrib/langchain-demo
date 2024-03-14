from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

# 创建LLM
llm = ChatOpenAI(model_name='gpt-4')

# 创建Prompt
prompt = ChatPromptTemplate.from_template('基于上下文：{context}\n回答：{input}')

# 创建输出解析器
output_parser = StrOutputParser()

# 模拟文档
docs = [Document(page_content="TuGraph是蚂蚁开源的图数据库产品")]

# 文档嵌入
splits = RecursiveCharacterTextSplitter().split_documents(docs)
vector_store = FAISS.from_documents(splits, OpenAIEmbeddings())
retriever = vector_store.as_retriever()

# 创建Chain
chain_no_context = RunnablePassthrough() | llm | output_parser
chain = (
    {"context": retriever, "input": RunnablePassthrough()}
    | prompt | llm | output_parser
)

# 调用Chain
print(chain_no_context.invoke('蚂蚁图数据库开源了吗？'))
print(chain.invoke('蚂蚁图数据库开源了吗？'))
