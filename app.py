from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import google.generativeai as genai
import os

# Setup your Gemini API key
genai.configure(api_key="")  # 🔐 Keep secure!

app = FastAPI()

class Message(BaseModel):
    prompt: str

@app.post("/tamilchat/")
def tamil_chat(message: Message):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")  # Or use "gemini-1.5-flash"
        response = model.generate_content(
            [
                {"role": "user", "parts": [f"தமிழில் பதிலளி: {message.prompt}"]}
            ]
        )
        return {"reply": response.text}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
