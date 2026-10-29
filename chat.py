from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="open-mistral-nemo", temperature=0.9 ,max_tokens=20)
response = model.invoke("give me a paragraph on Machine Learning")

print(response.content)