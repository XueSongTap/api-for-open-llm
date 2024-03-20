from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import HumanMessage

text = "hello"
messages = [HumanMessage(content=text)]
print(messages)
chat = ChatOpenAI(openai_api_base="http://localhost:8700/v1",openai_api_key="sk-xxx")
# llm = ChatOpenAI(openai_api_key="yxc", openai_api_base="http://localhost:8700/v1")
print(chat(messages))

# # print(llm(messages))

# embedding = OpenAIEmbeddings(openai_api_key="xxx", openai_api_base="http://localhost:8700/v1")
# print(embedding.embed_documents(["你好"]))
