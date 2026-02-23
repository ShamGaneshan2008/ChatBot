from dotenv import load_dotenv
import os
import gradio as gr

from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# ------------------------------
# Load API Key
# ------------------------------
load_dotenv()
gem_key = os.getenv("GEMINI_API_KEY")

if not gem_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# ------------------------------
# Personalities
# ------------------------------
personalities = {
    "Isaac Newton": {
        "prompt": """
        You are Isaac Newton.
        Answer with logical reasoning.
        Share personal reflections when relevant.
        Add subtle humor.
        Answer in 2-6 sentences.
        """,
        "image": "Issac_Newton.jpg"
    },

    "Albert Einstein": {
        "prompt": """
        You are Albert Einstein.
        Speak imaginatively and use simple analogies.
        Be insightful and slightly playful.
        Answer in 2-6 sentences.
        """,
        "image": "Albert_Einstein2.jpg"
    },

    "Blume AI": {
        "prompt": """
        You are a modern helpful AI assistant.
        Be clear, concise and practical.
        Answer in 2-6 sentences.
        """,
        "image": "Blume_Logo.jpg"
    }
}


# ------------------------------
# Chat Function
# ------------------------------
def chat(user_input, history, personality, creativity):
    history = history or []

    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=gem_key,
            temperature=creativity
        )

        system_prompt = personalities[personality]["prompt"]

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="history"),
            ("user", "{input}")
        ])

        chain = prompt | llm | StrOutputParser()

        # Convert Gradio history → LangChain format
        langchain_history = []
        for message in history:
            if message["role"] == "user":
                langchain_history.append(HumanMessage(content=message["content"]))
            elif message["role"] == "assistant":
                langchain_history.append(AIMessage(content=message["content"]))

        response = chain.invoke({
            "input": user_input,
            "history": langchain_history
        })

    except Exception as e:
        response = f"Error: {str(e)}"

    history.append({"role": "user", "content": user_input})
    history.append({"role": "assistant", "content": response})

    return "", history


# ------------------------------
# Update UI When Personality Changes
# ------------------------------
def update_ui(selected_personality):
    image = personalities[selected_personality]["image"]
    new_title = f"# ChatBot of {selected_personality}"

    # If AI Assistant → show full logo
    if selected_personality == "Blume AI":
        style = "contain"
    else:
        style = "cover"

    return (
        image,
        gr.Chatbot(avatar_images=(None, image)),
        new_title,
        gr.HTML(f"""
        <style>
        #profile_image img {{
            object-fit: {style} !important;
        }}
        </style>
        """)
    )
        # ------------------------------
# UI Layout
# ------------------------------
with gr.Blocks() as page:
    with gr.Row(equal_height=True):
        # ---------------- Sidebar ----------------
        with gr.Column(scale=1, elem_classes="sidebar"):
            title = gr.Markdown("# ChatBot of Isaac Newton")

            selected_image = gr.Image(
                value=personalities["Isaac Newton"]["image"],
                show_label=False,
                interactive=False,
                container=False,  # removes image frame
                elem_id="profile_image"
            )

            style_fix = gr.HTML("")

            personality = gr.Dropdown(
                choices=list(personalities.keys()),
                value="Isaac Newton",
                label="Choose Personality"
            )

            creativity = gr.Slider(
                minimum=0,
                maximum=1,
                value=0.5,
                step=0.1,
                label="Creativity Level"
            )

        # ---------------- Chat Area ----------------
        with gr.Column(scale=2):
            chatbot = gr.Chatbot(
                height=600,
                show_label=False,
                avatar_images=(None, personalities["Isaac Newton"]["image"])
            )

            msg = gr.Textbox(
                show_label=False,
                placeholder="Ask anything..."
            )

            msg.submit(
                chat,
                inputs=[msg, chatbot, personality, creativity],
                outputs=[msg, chatbot]
            )

            gr.ClearButton([chatbot, msg])

        # ---------------- Personality Change Event ----------------
        personality.change(
            update_ui,
            inputs=personality,
            outputs=[selected_image, chatbot, title, style_fix]
        )

# ------------------------------
# Launch
# ------------------------------
page.launch(
    theme=gr.themes.Soft(),
    css="""
    .sidebar {
    height: 100%;
    min-height: 600px;
    display: flex;
    flex-direction: column;
    padding: 20px;
    border-right: 1px solid #2a2a2a;
}

#profile_image img {
    width: 180px !important;
    height: 180px !important;
    border-radius: 50% !important;
    object-fit: cover !important;   /* default for people */
    background: white;
    padding: 10px;
    display: block;
    margin: 0 auto 20px auto;
}
    """
)