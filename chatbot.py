from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st 
import os


load_dotenv(r"C:\Users\004KXR744\llm_learning\.env")

#GROQ_API_KEY=os.getenv("MY_API_KEY")
os.environ["GROQ_API_KEY"]="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"

st.set_page_config(
    page_title="Chatbot", 
    page_icon="", 
    layout="centered"
)

st.title("Generative AI Chatbot")

#initiate chatHistory
#using session state because streamlit reruns the script on every user interaction, so we need to store the chat history in session state to persist it across reruns.
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    

#displaying chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        

#initiating the language model
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.5
)

#input text box for user input
user_prompt=st.chat_input("Ask Chatbot here: ")

if user_prompt:
    #displaying user message in chat message container
    st.chat_message("user").markdown(user_prompt)
    
    #storing user message in session state chat history
    st.session_state.chat_history.append({"role":"user","content":user_prompt})

    response=llm.invoke(
        input = [{"role": "system", "content": "You are a helpful chatbot."}, *st.session_state.chat_history  ]
    )
    #displaying bot message in chat message container
    with st.chat_message("assistant"):
        st.markdown(response.content)
    
    #storing bot message in session state chat history
    st.session_state.chat_history.append({"role":"assistant","content":response.content})
