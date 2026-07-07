from fastapi import FastAPI, Request, Query
from fastapi.responses import JSONResponse

from qna import answer_question_with_gemini
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI(title="EduGenie Learning Assistant")

@app.get("/")
def home():
    return {"message": "Welcome to EduGenie Learning Assistant"}

@app.get("/qa")
def qa(question: str = Query(...)):
    answer = answer_question_with_gemini(question)
    return {"question": question, "answer": answer}

@app.post("/explain")
async def explain(request: Request):
    data = await request.json()
    topic = data.get("topic")

    if not topic:
        return JSONResponse(content={"error": "Please provide a topic"}, status_code=400)

    explanation = explain_topic(topic)
    return {"topic": topic, "explanation": explanation}

@app.post("/summarize")
async def summarize(request: Request):
    data = await request.json()
    text = data.get("text")

    if not text:
        return JSONResponse(content={"error": "Please provide text to summarize"}, status_code=400)

    summary = summarize_text(text)
    return {"summary": summary}

@app.post("/quiz")
async def quiz(request: Request):
    data = await request.json()
    text = data.get("text")

    if not text:
        return JSONResponse(content={"error": "Please provide text for quiz"}, status_code=400)

    quiz_data = generate_quiz(text)
    return {"quiz": quiz_data}

@app.get("/learn/recommendations")
def learning_path(topic: str = Query(...)):
    recommendation = get_learning_recommendations(topic)
    return {"topic": topic, "recommendation": recommendation}