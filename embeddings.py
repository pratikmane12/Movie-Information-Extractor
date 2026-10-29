from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import MistralAIEmbeddings

embeddings = MistralAIEmbeddings(model="mistral-embed")

texts = [
    "Hello this is Tony Stark",
    "Hello your name is Jarvis",
]

vectors = embeddings.embed_documents(texts)

print(len(vectors))      # number of texts -> 2
print(len(vectors[0]))   # dimensions -> 1024
print(vectors[0][:5])    # first 5 numbers of the first vector