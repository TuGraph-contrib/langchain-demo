import os

import requests

# API Key
api_key = os.getenv('OPENAI_API_KEY')

# 自定义头部信息
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

# 对话历史
messages = []


def chat_with_ai(message):
    # 记录历史
    messages.append({'role': 'user', 'content': message})
    print(f'me: {message}')

    # 对话请求
    data = {
        'model': 'gpt-4',
        'messages': messages,
        'temperature': 0
    }
    url = 'https://api.openai.com/v1/chat/completions'
    response = requests.post(url, json=data, headers=headers)

    # 解析回答
    if response.status_code == 200:
        answer = response.json()['choices'][0]['message']['content']
        messages.append({'role': 'assistant', 'content': answer})
        print(f"ai: {answer}")
    else:
        print(f'Error: {response.status_code}', response.json())


# 多轮对话
chat_with_ai('什么是图计算？')
chat_with_ai('刚才我问了什么问题？')
