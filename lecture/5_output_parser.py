from langchain.schema import BaseOutputParser
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

chat = ChatOpenAI(temperature=0.1)

class CommaOutputParser(BaseOutputParser):
    def parse(self, text):
        items = text.strip().split(",")
        return list(map(str.strip,items))
    
p = CommaOutputParser()

p.parse("Hello, how ,are,you")

template = ChatPromptTemplate.from_messages(
    [("system", "당신은 list 생성 머신입니다. 입력받은 질문들은 모두 콤마를 붙여서 list 로 대답할겁니다. 최대 {max_items} 만큼요. list 가 아닌것은 답하지마세요"), 
     ("human", "{question}"),
     ]
)

prompt = template.format_messages(max_items=10, question="색깔 종류들을 알려주세요")

result = chat.predict_messages(prompt)

p.parse(result.content)