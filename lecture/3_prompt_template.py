from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

chat = ChatOpenAI(temperature=0.1)

template = PromptTemplate.from_template("{brand}는 어떤 기업이 소유하고 있나요? 그리고 당신의 이름은 무엇인가요?")

prompt = template.format(brand = '샤넬')

chat.predict(prompt)