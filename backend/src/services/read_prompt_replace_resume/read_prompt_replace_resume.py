def read_prompt_replace_resume(prompt_path, text):
    with open(prompt_path, 'r' , encoding='utf-8') as file:
        prompt = file.read()
    prompt = prompt.replace('{{CURRICULO}}', text)
    return prompt