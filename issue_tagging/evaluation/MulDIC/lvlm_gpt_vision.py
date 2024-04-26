from openai import OpenAI
import json
import time 
import os 
import numpy as np
import pandas as pd

client = OpenAI(api_key=os.environ["API_KEY_OPENAI"])

# Change the files here.
data = pd.read_csv('Flutter_train_bug.csv')

responses = []
for item in data:
    try:
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f'This the title of GitHub issue {item["title"]}? This is my full code and error {item["code"]}. Please help me resolving this issue. Give your confidence score.'
                    }#,
                    # {
                    #     "type": "image_url",
                    #     "image_url": {
                    #         "url": item["image_data"][0]["image_src"]
                    #     },
                    # }
                ],
            }
        ]
        response = client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=messages,
            max_tokens=500,
        )

        print(response.choices[0].message.content)
        responses.append({
            "claim": item["title"],
            "response": response.choices[0].message.content
        })
        with open("responses2.json", "w") as f:
            json.dump(responses, f)

        time.sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}")

print("Responses saved in responses.json")
