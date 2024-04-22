import openai
import os

def generate_response(input_prompt, text):
    openai.api_key = os.getenv("OPENAI_KEY")
    message = [
        {
            "role": "system",
            "content": "" },
        {
            "role": "user",
            "content": f"""{input_prompt}

user_input: {text}"""
        }
    ]
    response = openai.ChatCompletion.create(
        model='gpt-4-1106-preview',
        messages=message,
    )
    # 반환된 결과를 파일에 쓰는 대신 반환
    return response.choices[0].message.content


def generate_response_type2(user_input):
    openai.api_key = os.getenv("OPENAI_KEY")
    message = [
        {
            "role": "system",
            "content": "" },
        {
            "role": "user",
            "content": f"""{user_input}"""
        }
    ]
    response = openai.ChatCompletion.create(
        model='gpt-4-1106-preview',
        messages=message,
    )
    # 반환된 결과를 파일에 쓰는 대신 반환
    return response.choices[0].message.content