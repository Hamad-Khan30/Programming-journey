from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_flashcards(topic):
    try:
        response = client.responses.create(

            model="gpt-4.1-mini",
            input=f"""Generate exactly 20 flashcards about {topic}.Return ONLY valid JSON.
            Format:[{{"question":"Question here","answer":"Answer here"}}]Do not write any explanation.Do not use markdown.Return only JSON.""")

        flashcards = json.loads(response.output_text)
        return flashcards

    except json.JSONDecodeError:
        print("\nAI returned invalid JSON.")
        return []

    except Exception as e:
        print("\nAPI Error:")
        print(e)
        return []