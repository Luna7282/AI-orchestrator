from openai import OpenAI
import json
from dotenv import load_dotenv
import os
from fastapi import FastAPI, HTTPException
import re


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=api_key)
app = FastAPI()

@app.post('/clean')
def cleaning(request: dict):
    user_data = request.get("data")

    if not user_data:
        raise HTTPException(status_code=400, detail="Missing 'data' field in request.")

    prompt = f"""
    You are a data processing assistant. Your task is to clean the given dataset.

    Instructions:
    - Trim extra spaces from all text fields.
    - Ensure emails are in a valid format. If invalid, replace with `null`.
    - Convert age to an integer if possible; otherwise, set it to `null`.
    - Remove entries where the `name` is missing or is "N/A".
    - Preserve the original structure of the data.

    Here is the dataset:
    ```json
    {json.dumps(user_data)}
    ```
    """

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": prompt}]
    )

    raw_response = response.choices[0].message.content.strip()



    try:
        
        if raw_response.startswith("```json"):
            raw_response = raw_response[7:-3].strip()  
            raw_response = re.sub(r'"\s*null\s*"', 'null', raw_response)
        return json.loads(raw_response)

    except json.JSONDecodeError:
        print(f"JSONDecodeError: Unable to parse -> {raw_response}")
        return {"error": "Invalid JSON response from LLM"}
