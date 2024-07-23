
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

chat = ChatOpenAI(temperature=0.1)

template = ChatPromptTemplate.from_messages([
    ("system", "당신은 {language}로만 대답합니다."),
    ("ai", "난 {ai_name}이다."),
    ("human", "{brand}는 어떤 기업이 소유하고 있나요? 그리고 당신의 이름은 무엇인가요?")
])

prompt = template.format_messages(
    language="한국어",
    ai_name="주석봇",
    brand="구찌"
)

chat.predict_messages(prompt)