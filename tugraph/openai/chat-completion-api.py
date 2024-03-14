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
    'model': 'gpt-4',
    'messages': [{'role': 'user', 'content': '什么是图计算？'}],
    'temperature': 0.7
}

# 调用API
url = 'https://api.openai.com/v1/chat/completions'
response = requests.post(url, json=data, headers=headers)
answer = response.json()['choices'][0]['message']['content']
print(answer)

