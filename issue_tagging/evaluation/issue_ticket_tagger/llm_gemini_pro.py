import google.generativeai as genai
import os, json
import requests
from PIL import Image

genai.configure(api_key=os.environ["API_KEY_GEMINI"])
model = genai.GenerativeModel('gemini-pro')


file_path = './../datasets/issue_ticket_tagger/issue_ticket_tagger.txt'

issue_list = []
with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if line.startswith('__label__bug'):
            index = len('__label__bug')
            issue_text = line[index:].strip()
            # print(rest_of_text)
            issue_list.append(issue_text)

responses = []
for item in issue_list:
    try:
        prompt = f'Based on this issue {item}, label the issue. Give output in one word.'
        response = model.generate_content(prompt)
        print(response.text)
        responses.append({
        "response": response.text
        })
        with open("gemini_pro_ticket_tagger.json", "w") as f:
            json.dump(responses, f, indent=4)

    except Exception as e:
        print(f"An error occurred: {e}")