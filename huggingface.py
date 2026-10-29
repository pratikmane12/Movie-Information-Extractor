
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation",
    max_new_tokens=512,
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("who are you ?")

print(response.content)