import os
from src.utils.get_text_from_file.get_text_from_file import get_text_from_file
from src.utils.remove_linebreak_text.remove_linebreak_text import remove_linebreak_text

import json
import requests
from dotenv import load_dotenv
from time import sleep

load_dotenv()


def fetch_ia_and_generate_resume_personalized_json(job_description, prompt = ''):
    
    
    prompt_without_linebreak = remove_linebreak_text(prompt)
    
    token = os.getenv("AI_TOKEN")
    URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={token}"  # URL corrigida
    headers = {
        "Content-Type": "application/json"
    }
    
    payload = {
        "contents": [
            {
                "role": "assistant",
                "parts": [
                    {
                        "text": f"{prompt_without_linebreak}"
                    }
                ]
            },
            {
                "role": "user",
                "parts": [
                    {
                        "text": f"VAGA: (({job_description}))"
                    }
                ]
            }
        ],
        "generation_config": {
            # "candidate_count": 1,
            "temperature": 0.3
        }
    }
    try:
        response = requests.post(URL, headers=headers, json=payload, timeout=100)
        response.raise_for_status()  # Lança exceção para status 4xx/5xx
        sleep(2)
        if response.status_code == 200:
            response_json = response.json()
            generated_text = response_json["candidates"][0]["content"]["parts"][0]["text"]
            text_without_linebreak = remove_linebreak_text(generated_text)
            return text_without_linebreak
        return None
            
    except requests.exceptions.RequestException as e:
        print(e)
        raise e
    except json.JSONDecodeError as e:
        print(e)
        raise e
    