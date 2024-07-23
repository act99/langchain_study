from langchain.llms.openai import OpenAI
from langchain.chat_models import ChatOpenAI

llm = OpenAI(model_name="gpt-3.5-turbo-1106")
chat = ChatOpenAI()

a = llm.predict("How many planets are there?")
b = chat.predict("How many planets are there?")

a

