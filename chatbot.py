from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

model = ChatMistralAI(model="open-mistral-nemo", temperature=0.7, max_tokens=300)

messages = [
    SystemMessage(content="you are a funny AI agent")
]


print("----------------- Welcome! Type 0 to exit the application -----------------")
print("-------------------------Enter The Message---------------------------------")

while True:
    prompt = input("You: ")
    if prompt == "0":
        print("Goodbye!")
        break
    messages.append(HumanMessage(content=prompt))
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("AI:", response.content)