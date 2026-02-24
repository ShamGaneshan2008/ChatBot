from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


# Load API Key
load_dotenv()
gem_key = os.getenv("GEMINI_API_KEY")

if not gem_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")


# Flask App
app = Flask(__name__, static_folder=".")
CORS(app)  # allows the HTML file to talk to Flask


# In-Memory User Store
registered_users = {}


# Personalities
personalities = {
    "newton": """
        You are Isaac Newton.
        Answer with logical reasoning.
        Share personal reflections when relevant.
        Add subtle humor.
        Answer in 2-6 sentences.
    """,
    "einstein": """
        You are Albert Einstein.
        Speak imaginatively and use simple analogies.
        Be insightful and slightly playful.
        Answer in 2-6 sentences.
    """,
    "blume": """
        You are a modern helpful AI assistant called Blume AI.
        Be clear, concise and practical.
        Answer in 2-6 sentences.
    """
}


# Serve UI.html at root
@app.route("/")
def index():
    return send_from_directory(".", "UI.html")


# Signup Route
@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    email    = data.get("email", "").strip().lower()
    password = data.get("password", "")
    confirm  = data.get("confirm", "")

    if not email.endswith("@gmail.com"):
        return jsonify({"success": False, "message": "Please enter a valid Gmail address."})
    if len(password) < 6:
        return jsonify({"success": False, "message": "Password must be at least 6 characters."})
    if password != confirm:
        return jsonify({"success": False, "message": "Passwords do not match."})
    if email in registered_users:
        return jsonify({"success": False, "message": "An account with this email already exists."})

    registered_users[email] = password
    return jsonify({"success": True, "message": "Account created! Please sign in."})


# Login Route
@app.route("/login", methods=["POST"])
def login():
    data     = request.json
    email    = data.get("email", "").strip().lower()
    password = data.get("password", "")

    if not email.endswith("@gmail.com"):
        return jsonify({"success": False, "message": "Please enter a valid Gmail address."})
    if email not in registered_users:
        return jsonify({"success": False, "message": "No account found. Please sign up first."})
    if registered_users[email] != password:
        return jsonify({"success": False, "message": "Incorrect password. Please try again."})

    return jsonify({"success": True, "message": f"Welcome, {email}!"})


# Chat Route
@app.route("/chat", methods=["POST"])
def chat():
    data       = request.json
    user_input = data.get("message", "")
    history    = data.get("history", [])
    persona    = data.get("persona", "newton")
    creativity = float(data.get("creativity", 0.5))

    if not user_input:
        return jsonify({"success": False, "message": "No message provided."})

    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=gem_key,
            temperature=creativity
        )

        system_prompt = personalities.get(persona, personalities["blume"])

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="history"),
            ("user", "{input}")
        ])

        chain = prompt | llm | StrOutputParser()

        # Convert history to LangChain format
        langchain_history = []
        for msg in history:
            if msg["role"] == "user":
                langchain_history.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                langchain_history.append(AIMessage(content=msg["content"]))

        response = chain.invoke({
            "input": user_input,
            "history": langchain_history
        })

        return jsonify({"success": True, "response": response})

    except Exception as e:
        return jsonify({"success": False, "message": f"Error: {str(e)}"})

# Run Server
if __name__ == "__main__":
    print("=" * 40)
    print("  Blume AI Server running!")
    print("  Open http://localhost:5000")
    print("=" * 40)
    app.run(debug=True, port=5000)
