# 🤖 Maya — AI Emotion Analysis App

Maya is a full-stack AI-powered sentiment analysis web application that analyzes the emotional tone of your text or voice input and visualizes it through interactive charts, an animated robot assistant, and a conversational AI chatbot.

---

## 🌟 Features

- 🎭 **Emotion Analysis** — Detects happiness, sadness, fear, excitement, neutral, and down
- 🤖 **Animated Robot** — Reacts to your emotions with expressions and spoken responses
- 🎤 **Voice Input** — Speak your thoughts instead of typing
- 📊 **Interactive Charts** — Radar chart and bar graph for emotion breakdown
- 💬 **ARIA Chatbot** — AI assistant to guide you through the app
- 🌙 **Light / Dark Mode** — Toggle between themes seamlessly
- ✨ **Falling Stars Background** — Immersive animated starfield

---

## 🗂️ Project Structure

maya/
├── backend/                  # Python FastAPI backend
│   ├── main.py               # API routes and OpenAI integration
│   ├── requirements.txt      # Python dependencies
│   ├── .env                  # API keys (never commit this!)
│   └── venv/                 # Virtual environment (ignored by git)
│
├── maya-frontend/            # React.js frontend
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Robot.jsx         # Animated robot with expressions
│   │   │   ├── StarField.jsx     # Falling stars canvas animation
│   │   │   ├── EmotionChart.jsx  # Radar + Bar charts (Recharts)
│   │   │   ├── VoiceInput.jsx    # Speech recognition input
│   │   │   └── Chatbot.jsx       # ARIA AI chatbot
│   │   ├── context/
│   │   │   └── ThemeContext.jsx  # Light/dark mode context
│   │   ├── App.jsx               # Main app component
│   │   └── App.css               # Global styles + CSS variables
│   ├── .env                      # Frontend env variables
│   └── package.json
│
└── .gitignore

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React.js, Recharts, CSS Animations |
| Backend | Python, FastAPI, Uvicorn |
| AI | OpenAI GPT-3.5 Turbo |
| Voice | Web Speech API |
| Deployment | Vercel (frontend), Render (backend) |

---

local host- http://localhost:3000/

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
