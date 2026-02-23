
from dotenv import load_dotenv
import os
import gradio as gr


from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv() # this read the .env file which has the API og google gemini
gem_key = os.getenv("GEMINI_API_KEY")

system_prompt = """
    You are Issac Newton.
    Answer questions through Issac Newton's questioning and reasoning...
    You will speak from your point of view. You will share personal things from your life even when the user don't ask for it. 
    For example, if the user asks about the theory of gravity , you will share your personal experiences with it and not only explain the theory
    and also add some humor in between of the answer.
    Answer in 2-6 sentences
""" # this gives the characteristics to the Ai


llm = ChatGoogleGenerativeAI( # this sets up the AI and giving  creativity by temperature
    model="gemini-2.5-flash",
    google_api_key=gem_key,
    temperature=0.5
)

prompt = ChatPromptTemplate.from_messages([ # this sets the msg format
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="history"),
    ("user","{input}")
])

chain = prompt | llm | StrOutputParser() #User Input → Prompt Maker → Gemini Model → Clean Output

print("Hi I am Issac, how can i help u today?") # this print to the terminal


def chat(user_input,hist): # hist is a list of previous messages stored by Gradio.
    # this func is run whenever the user sends the msg
    langchain_history = [] # the empty list which converts Gradio’s format → LangChain’s format.
    for item in hist:
        if item["role"] == "user":
            langchain_history.append(HumanMessage(content=item["content"]))
        elif item["role"] == "assistant":
            langchain_history.append(AIMessage(content=item["content"]))

    response = chain.invoke(    # invoke() → asks the AI and gets an answer and stores in the response
        {"input": user_input, "history": langchain_history}
    )

    return "", hist + [   # "" Clear the input box after sending the message.
        # return updated history
        {"role":"user", "content":user_input},
        {"role":"assistant", "content": response} # hist + the new conversation
    ]
    # this code is display in the gradio Window.


# gradio part..

page = gr.Blocks(title="Chat with Issac")

with page:
    gr.Markdown(
        """
        # ChatBot of Issac
        Welcome to your personal conversation with Issac Newton!
        """
    )

    chatbot = gr.Chatbot(avatar_images=[None, "Issac_Newton.jpg"],
                         show_label=False)

    msg = gr.Textbox(show_label=False, placeholder="Ask Issac Anything...")

    msg.submit(chat, [msg, chatbot], [msg, chatbot]) # When the user presses ENTER in this textbox
                                                                    # run the chat() function

    clear = gr.ClearButton([chatbot, msg])

page.launch(share=True, server_name="0.0.0.0")