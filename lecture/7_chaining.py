from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.callbacks import StreamingStdOutCallbackHandler

chat = ChatOpenAI(temperature=0.1, streaming=True, callbacks=[StreamingStdOutCallbackHandler()])

chef_prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 세계 최고의 요리사이다. 너는 어떤 종류의 요리든 쉽게 구할 수 있고, 재료로 따라하기 쉬운 레시피를 만들어준다."), 
    ("human", "나는 {cuisine} 요리를 만들고 싶어."),
])

chef_chain = chef_prompt | chat

veg_chef_prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 채식주의자를 위한 셰프이다. 너는 전통적인 방식으로 채식주의 음식 레시피를 알려줄 수 있다. 그리고 너는 질문받은 레시피에서 너무 벗어난 음식 레시피를 알려주면 안된다."), 
    ("human", "{recipe}"),
])

veg_chain = veg_chef_prompt | chat

final_chain = {"recipe": chef_chain} | veg_chain

final_chain.invoke({
    "cuisine": "한국"
})
