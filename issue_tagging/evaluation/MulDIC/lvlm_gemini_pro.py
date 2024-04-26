import google.generativeai as genai
import os, json
import requests
from PIL import Image

genai.configure(api_key=os.environ["API_KEY_GEMINI"])
model = genai.GenerativeModel('gemini-pro-vision')

with open('dataset.json', "r") as infile:
    data = json.load(infile)

responses = []
for item in data:
    try:
        prompt = f'This the title of GitHub issue {item["title"]}? This is my full code and error {item["code"]}. Please help me resolving this issue. Give your confidence score.'
        response = model.generate_content([prompt])#, image_data])
        # os.remove(save_path)
        print(response.text)
        responses.append({
        "claim": item["claim"],
        "response": response.text
        })
        with open("gemini_responses.json", "w") as f:
            json.dump(responses, f, indent=4)

    except Exception as e:
        print(f"An error occurred: {e}")