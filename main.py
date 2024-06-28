from langchain_community.llms import Ollama
import streamlit as sl

llm = Ollama(model='llama3')

sl.title('Your fav chatbot :)')

prompt = sl.text_area('Enter whatever you want :]')

if sl.button('Generate'):
    if prompt:
        with sl.spinner('Generating the response ...'):
            sl.write_stream(llm.stream(prompt, stop=['<|eot_id|>']))
