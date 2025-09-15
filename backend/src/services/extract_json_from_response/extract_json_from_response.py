import re
import json


def extract_json_from_response(response:str):
    """
    Extrai o JSON da resposta usando regex
    """
    # Regex para encontrar o JSON após "RESPOSTA: "
    match_first = re.search(r'RESPOSTA:\s*(\{.*\})', response, re.DOTALL)
    if match_first:
        json_string = match_first.group(1)
        return json.loads(json_string)
    
    match_second = re.search(r'```json\s*(\{.*?\})\s*```', response, re.DOTALL)
    if match_second:
        json_string = match_second.group(1)
        return json.loads(json_string)
    return None
