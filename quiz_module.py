import google.generativeai as genai
import json
import re

def clean_json_block(text):
    return re.sub(r"```(?:json)?\n(.*?)```", r"\1", text, flags=re.DOTALL).strip()

def generate_quiz(text: str):
    try:
        model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")

        prompt = f"""
Create 3 multiple-choice questions from this passage.

Return valid JSON only:
[
  {{
    "question": "Question text",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }}
]

Passage:
{text}
"""

        response = model.generate_content(prompt)
        cleaned_text = clean_json_block(response.text)
        return json.loads(cleaned_text)

    except Exception as e:
        return {"error": f"Error in Quiz Generation: {e}"}