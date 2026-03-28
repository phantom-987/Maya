from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import json, os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

ANALYZE_PROMPT = """Analyze this text and return ONLY valid JSON (no markdown):
{
  "emotions": { "happiness": 0-100, "sadness": 0-100, "fear": 0-100, "excitement": 0-100, "neutral": 0-100, "down": 0-100 },
  "dominant_emotion": "emotion name",
  "confidence": 0-100,
  "summary": "1-2 sentence empathetic analysis",
  "robot_expression": "happy|sad|fear|excited|neutral|thinking",
  "robot_message": "short conversational response max 25 words"
}
Emotion values must sum to ~100."""

CHAT_PROMPT = """You are ARIA, a friendly AI assistant inside a Sentiment Analysis app.
Help users understand their emotions, use the app, and interpret results.
Be warm, concise (under 60 words), and supportive."""

class TextReq(BaseModel):
    text: str

class ChatReq(BaseModel):
    message: str
    history: list = []

@app.post("/analyze")
async def analyze(req: TextReq):
    if not req.text.strip():
        raise HTTPException(400, "Text is empty")
    try:
        res = client.chat.completions.create(
            model="gpt-3.5-turbo",
            max_tokens=500,
            messages=[
                {"role": "system", "content": ANALYZE_PROMPT},
                {"role": "user", "content": req.text}
            ]
        )
        return json.loads(res.choices[0].message.content.strip())
    except Exception as e:
        raise HTTPException(500, str(e))

@app.post("/chat")
async def chat(req: ChatReq):
    try:
        msgs = [{"role": "system", "content": CHAT_PROMPT}]
        msgs += req.history[-8:]
        msgs += [{"role": "user", "content": req.message}]
        res = client.chat.completions.create(
            model="gpt-3.5-turbo",
            max_tokens=150,
            messages=msgs
        )
        return {"reply": res.choices[0].message.content.strip()}
    except Exception as e:
        raise HTTPException(500, str(e))

@app.get("/health")
def health(): return {"status": "ok"}

