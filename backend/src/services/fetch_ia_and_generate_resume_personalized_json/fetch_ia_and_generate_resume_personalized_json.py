import os
from src.utils.get_text_from_file.get_text_from_file import get_text_from_file
from src.utils.remove_linebreak_text.remove_linebreak_text import remove_linebreak_text

import json
import requests
from dotenv import load_dotenv
from time import sleep

load_dotenv()


def fetch_ia_and_generate_resume_personalized_json(job_description, prompt=''):
    prompt_without_linebreak = remove_linebreak_text(prompt)
    token = os.getenv("AI_TOKEN")
    
    headers = {
        "Content-Type": "application/json",
    }
    
    payload = {
        # The instruction "prompt" must come here to avoid order errors
        "system_instruction": {
            "parts": [
                {"text": prompt_without_linebreak}
            ]
        },
        "contents": [
            {
                "role": "user",  # Required to be 'user' in the first position
                "parts": [
                    {"text": f"VAGA: (({job_description}))"}
                ]
            }
        ],
        "generation_config": {
            "temperature": 0.3
        }
    }
    sleep(0.3)
    try:
        # The URL now uses the token variable via params 
        response = requests.post(
            "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent", 
            headers=headers,
            json=payload,
            timeout=100,
            params={"key": token}
        )
        
        response.raise_for_status()
        
        response_json = response.json()
        # Accessing the text field safely
        generated_text = response_json["candidates"][0]["content"]["parts"][0]["text"]
        return remove_linebreak_text(generated_text)
            
    except requests.exceptions.HTTPError as e:
        # Extracts the real Google error message hidden in the JSON
        try:
            error_details = e.response.json()
            error_msg = error_details.get("error", {}).get("message", e.response.text)
        except:
            error_msg = e.response.text
        raise Exception(f"Gemini API Error: {error_msg}") from e
        
    except requests.exceptions.RequestException as e:
        raise e
    except (json.JSONDecodeError, KeyError) as e:
        raise ValueError(f"Error processing AI response: {str(e)}")