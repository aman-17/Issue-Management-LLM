from openai import OpenAI
import json
import time 
import os 
import numpy as np
import pandas as pd

client = OpenAI(api_key=os.environ["API_KEY_OPENAI"])


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

responses=[]

for item in issue_list:
    try:
        prompt = f'Based on this issue {item}, label the issue. Give output in one word.'
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ],
            }
        ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,
        )

        print(response.choices[0].message.content)
        responses.append({
            "response": response.choices[0].message.content
        })
        with open("ticket_tagger_gpt3.json", "w") as f:
            json.dump(responses, f)

        time.sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}")

print("Responses saved in responses.json")
