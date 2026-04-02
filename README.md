# 🤖 Maya — AI Emotion Analysis App

Maya is a full-stack AI-powered sentiment analysis web application that analyzes the emotional tone of your text or voice input and visualizes it through interactive charts, an animated robot assistant, and a conversational AI chatbot.

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
