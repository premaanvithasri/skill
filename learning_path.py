import google.generativeai as genai

def get_learning_recommendations(topic: str) -> str:
    try:
        model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")

        prompt = f"""
Create a personalized learning path for the topic: {topic}

Include:
- Beginner topics
- Intermediate topics
- Advanced topics
- Recommended resources
- Study order
"""

        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        return f"Error in Learning Path: {e}"