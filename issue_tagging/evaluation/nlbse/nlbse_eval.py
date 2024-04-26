import pandas as pd
import emoji
import re
import string
from openai import OpenAI
import concurrent.futures
import tiktoken

client = OpenAI(api_key='open-ai-api')

test_data = pd.read_csv("./data/issues/issues_test.csv")
train_data = pd.read_csv("./data/issues/issues_train.csv")

cleaned_count = 0
original_count = 0

def clean_text(text):
    global cleaned_count, original_count
    if not isinstance(text, str):
        original_count += 1
        return text
    text = text.replace('"', '')
    text = re.sub(r'DevTools.*?\(automated\)', '', text)
    text = text.lower()
    text = emoji.demojize(text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(f"[{re.escape(string.punctuation)}]", '', text)
    text = text.replace("#", "")
    text = re.sub(r'\s+', ' ', text)
    words = text.split()
    words = [word for word in words if len(word) <= 20]
    cleaned_text = ' '.join(words)

    cleaned_count += 1
    return cleaned_text

def apply_clean_text(data):
    data['body'] = data['body'].apply(clean_text)
    data['title'] = data['title'].apply(clean_text)
    return data

test_data = apply_clean_text(test_data)
train_data = apply_clean_text(train_data)

print(f"Cleaned {cleaned_count} times.")
print(f"Returned original text {original_count} times.")

def query_chatgpt(prompt, model, temperature=0.0, max_tokens=1, max_retries=5):
    attempt = 0
    max_content_tokens = 3999

    encoding = tiktoken.get_encoding("cl100k_base")  # Assuming this is used elsewhere

    def truncate_message(message, max_length):
        tokens = encoding.encode(message)
        if len(tokens) > max_length:
            truncated_tokens = tokens[:max_length]
            message = encoding.decode(truncated_tokens)
        return message

    prompt = truncate_message(prompt, max_content_tokens)

    while attempt < max_retries:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(
                OpenAI.chat.completions.create,
                model=model,
                messages=[{"role": "system", "content": "GitHub Issue Report Classifier"}, {"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature
            )
            try:
                response = future.result(timeout=5)  # 5 seconds timeout
                return response.choices[0].message.content
            except concurrent.futures.TimeoutError:
                print(f"Attempt {attempt + 1}/{max_retries} - Request timed out. Retrying...")
            except Exception as e:
                print(f"Attempt {attempt + 1}/{max_retries} - An error occurred: {e}")
            finally:
                attempt += 1

    print("Failed to get a response after several retries.")
    return None

labels = ['feature', 'bug', 'question']
