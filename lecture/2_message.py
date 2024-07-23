from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(temperature=0.1)

messages = [
    SystemMessage(content="당신은 {language}로만 대답합니다."),
    AIMessage(content="난 {ai_name}이다."),
    HumanMessage(content="{brand}는 어떤 기업이 소유하고 있나요? 그리고 당신의 이름은 무엇인가요?")
]

chat.predict_messages(messages)