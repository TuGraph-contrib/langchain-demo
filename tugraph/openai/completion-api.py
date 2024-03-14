import os
import requests

# API Key
api_key = os.getenv('OPENAI_API_KEY')

# 头部信息
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

# 准备数据
data = {
    'model': 'gpt-3.5-turbo-instruct',
    'prompt': ['什么是图计算？'],
    'max_tokens': 1024
}

# 调用API
url = 'https://api.openai.com/v1/completions'
response = requests.post(url, json=data, headers=headers)
answer = response.json()['choices'][0]['text']
print(answer)
