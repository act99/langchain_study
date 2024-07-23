from langchain.chat_models import ChatOpenAI
from langchain.schema import BaseOutputParser
from langchain.prompts import ChatPromptTemplate

chat = ChatOpenAI(temperature=0.1)

class CommaOutputParser(BaseOutputParser):
    def parse(self, text):
        items = text.strip().split(",")
        return list(map(str.strip,items))
    
template = ChatPromptTemplate.from_messages(
    [("system", "당신은 list 생성 머신입니다. 입력받은 질문들은 모두 콤마를 붙여서 list 로 대답할겁니다. 최대 {max_items} 만큼요. list 가 아닌것은 답하지마세요"), 
     ("human", "{question}"),
     ]
)

chain = template | chat | CommaOutputParser()

results = chain.invoke({
    "max_items": 5,
    "question": "포켓몬 종류를 알려줘"
})

print(results)