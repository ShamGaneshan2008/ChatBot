# ChatBot
⚗️ Isaac Newton AI
“If I have seen further, it is by standing on the shoulders of Giants.”

A personality-driven conversational AI that lets you speak directly with
Sir Isaac Newton — reimagined through modern Large Language Models.

🌌 About The Project

What if the father of classical physics had access to Artificial Intelligence?

Isaac Newton AI is a conversational chatbot that simulates the thoughts, reasoning, and personality of Sir Isaac Newton using Google Gemini.

The model responds with:

Scientific depth

Historical tone

Analytical reasoning

Calm philosophical reflection

This project blends history + AI + prompt engineering into a clean, interactive web experience.

🧠 How It Works
You → Gradio Interface → LangChain Prompt Engine → Gemini Model → Newton’s Response

Behind the scenes:

A custom system prompt defines Newton’s personality

Conversation history maintains context

Gemini (gemini-2.5-flash) generates intelligent responses

LangChain structures the interaction pipeline

Gradio delivers a real-time web interface

✨ Core Features

🔹 Personality-based AI simulation
🔹 Context-aware multi-turn conversations
🔹 Secure API key management (.env)
🔹 Real-time web interface
🔹 Modular and scalable architecture
🔹 Clean project structure for deployment

🛠 Tech Stack
Technology	Purpose
Python	Core development
Google Gemini	Large Language Model
LangChain	Prompt orchestration
Gradio	Web interface
python-dotenv	Secure API management


📁 Project Structure
Isaac-Newton-Gemini-Chatbot/
              │
              ├── main.py                # Core chatbot logic
              ├── Issac_Newton.jpg       # Profile image
              ├── screenshot.png         # UI preview
              ├── requirements.txt       # Dependencies
              ├── README.md              # Documentation
              └── .gitignore             # Security config
              🚀 Installation Guide
1️⃣ Clone the Repository:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2️⃣ Install Dependencies:
pip install -r requirements.txt

3️⃣ Add Your API Key:
Create a .env file
GEMINI_API_KEY=your_api_key_here

⚠ Never push your API key to GitHub.

4️⃣ Run the Application:
python main.py

Then open:

http://localhost:7860

📸 Demo

![Chatbot Screenshot](https://github.com/ShamGaneshan2008/ChatBot/blob/8ff865ccbdf7188fe3d33bd702d25f6d5f2121a5/Screenshots.png/Screenshot%202026-02-23%20132217.png)
🔐 Security Practices

API keys stored securely using environment variables

.env excluded from version control

No sensitive data hardcoded

🎯 What This Project Demonstrates

✔️ Large Language Model integration
✔️ Personality-based prompt engineering
✔️ Context memory handling
✔️ Secure development workflow
✔️ Real-world AI application building

🔮 Future Enhancements

🌍 Cloud deployment (Render / Hugging Face Spaces)

🧾 Conversation history persistence

🎭 Multi-scientist personality selection

🎨 Enhanced UI theme customization

📊 Usage analytics dashboard

👨‍💻 Author

Shom
Computer Science Student
AI • Python • Automation • LLM Applications

🏁 Final Note

This is not just a chatbot.
It is an experiment in bringing historical intellect into the age of Artificial Intelligence.
