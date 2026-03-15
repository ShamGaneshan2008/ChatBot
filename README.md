# 🤖 Gemini Chatbot

A simple, clean chatbot web application powered by the **Google Gemini API**.

---

## ✨ Features

- 💬 Real-time conversational interface
- ⚡ Powered by Google Gemini (gemini-pro model)
- 🎨 Clean, responsive UI
- 🔄 Multi-turn conversation support (remembers context)
- 📱 Mobile-friendly design

---

## 🚀 Getting Started

### Prerequisites

- A modern web browser
- A [Google Gemini API key](https://aistudio.google.com/app/apikey)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/gemini-chatbot.git
   cd gemini-chatbot
   ```

2. **Add your API key**

   Open `index.html` (or `config.js` if applicable) and replace the placeholder with your actual Gemini API key:
   ```js
   const API_KEY = "YOUR_GEMINI_API_KEY_HERE";
   ```

3. **Run the app**

   Simply open `index.html` in your browser — no build step or server required.

   ```bash
   open index.html
   ```

---

## 🛠️ Tech Stack

| Layer       | Technology              |
|-------------|-------------------------|
| Frontend    | HTML, CSS, JavaScript   |
| AI Backend  | Google Gemini API       |
| HTTP Client | Fetch API (native JS)   |

---

## 📁 Project Structure

```
gemini-chatbot/
├── index.html       # Main app UI
├── style.css        # Styling
├── script.js        # Gemini API logic & chat handling
└── README.md        # You're here!
```

---

## 🔑 Getting a Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy and paste it into the app

> ⚠️ **Keep your API key private.** Never commit it to a public repository.

---

## 💡 How It Works

1. The user types a message and hits **Send**
2. The app sends the message to the **Gemini API** via a `POST` request
3. Gemini processes the input and returns a response
4. The response is displayed in the chat window

```
User Input → Gemini API → AI Response → Chat UI
```

---

## 📸 Screenshot

> *(Add a screenshot of your app here)*

---

## 🧩 Customization

- **Change the model**: Swap `gemini-pro` for `gemini-1.5-flash` or `gemini-1.5-pro` in `script.js`
- **Adjust tone**: Add a system prompt to the API request body to give the chatbot a custom persona
- **Style it**: Edit `style.css` to match your brand or preferences

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 🙌 Acknowledgements

- [Google Gemini API](https://ai.google.dev/)
- [Google AI Studio](https://aistudio.google.com/)
