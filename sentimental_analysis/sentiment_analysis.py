from openai import OpenAI
import json
from dotenv import load_dotenv
import os
from fastapi import FastAPI, HTTPException


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=api_key)
app = FastAPI()

@app.post("/analyze")
def sentimental_analysis(request: dict):
    text = request.get("data", "")
    
    if not text:
        raise HTTPException(status_code=400, detail="Missing 'data' field in request.")

    prompt = f"""
    You are a sentiment analysis expert.
    Analyze the sentiment of the following text:
    
    Text: "{text}"
    
    Classify it as:
    - Positive
    - Negative
    - Neutral
    
    Return the result in valid JSON format:
    ```json
    {{
        "sentiment": "positive/negative/neutral",
        "explanation": "Brief explanation of why the text has this sentiment."
    }}
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
        return json.loads(raw_response)

    except json.JSONDecodeError:
        print(f"JSONDecodeError: Unable to parse -> {raw_response}")
        return {"error": "Invalid JSON response from LLM"}