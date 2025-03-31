from fastapi import FastAPI, HTTPException
import requests
from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=api_key)


app = FastAPI()


def determine_task(user_request: str):
    prompt = f"""
    User request: "{user_request}"
    
    Choose the correct task for this request:
    - "data_cleaning" if it is about formatting, fixing, or refining data.
    - "sentiment_analysis" if it is about analyzing emotions or opinions in text.

    Respond with **ONLY ONE WORD**: either "data_cleaning" or "sentiment_analysis".
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "system", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return str(e)


@app.post("/process")
async def service_request(request: dict):
    user_input = request.get("data")
    
    if not user_input:
        raise HTTPException(status_code=400, detail="No data provided")

    # Determine the task using LLM
    task_type = determine_task(user_input)
    

    if task_type == "data_cleaning":
        response = requests.post('http://localhost:8001/clean', json={"data": user_input})
    elif task_type == "sentiment_analysis":
        response = requests.post('http://localhost:8002/analyze', json={"data": user_input})
    else:
        return {"error": "Invalid Task type"}

    return response.json()