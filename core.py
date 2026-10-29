import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

model = ChatMistralAI(model="open-mistral-nemo", temperature=0, max_tokens=600)

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an information extraction assistant.
Read the paragraph given by the user and extract the useful information.

Rules:
- Use only information stated in the paragraph. Do not guess.
- If something is not mentioned, write "Not mentioned".

Give the answer in this format:

Movie Name:
Genre:
Director:
Release Year:
Cast:
Music Composer:
Rating:
Setting:
Themes:
Critical Reception:

Quick Summary (2 sentences maximum):"""),
    ("human", "{paragraph}"),
])

chain = prompt | model

default_paragraph = """Interstellar is a visually stunning science fiction epic directed by Christopher Nolan. Released in 2014, the film stars Matthew McConaughey, Anne Hathaway, Jessica Chastain, and Michael Caine. The story revolves around a group of astronauts who travel through a wormhole near Saturn in search of a new home for humanity as Earth faces environmental collapse. The movie was widely appreciated for its emotional depth, scientific accuracy, and Hans Zimmer's powerful soundtrack. It holds a rating of 8.6 on IMDb and is often considered one of the greatest sci-fi films of the 21st century."""

st.set_page_config(page_title="Movie Information Extractor", page_icon="🎬")
st.title("🎬 Movie Information Extractor")
st.caption("Paste a paragraph about a movie and extract the useful information.")

paragraph = st.text_area("Paragraph", value=default_paragraph, height=250)

if st.button("Extract Information"):
    response = chain.invoke({"paragraph": paragraph})
    st.subheader("Extracted Information")
    st.write(response.content)