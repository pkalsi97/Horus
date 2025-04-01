import requests
from google import genai
from openai import OpenAI
import anthropic


available_llms = {
    "GOOGLE": lambda key: genai.Client(api_key=key),
    "OPENAI": lambda key: OpenAI(api_key=key),
    "ANTHROPIC": lambda key: anthropic.Anthropic(api_key=key)
    }

def validate_api_key(key: str,llm: str) -> bool:
    if llm == "ANTHROPIC":
        url = "https://api.anthropic.com/v1/models"
        headers = {
            "x-api-key": key,
            "anthropic-version": "2023-06-01"
        }
        response = requests.get(url,headers=headers)
        return True if response.status_code == 200 else False
    elif llm == "OPENAI":
        url = "https://api.openai.com/v1/models"
        headers = {
            "Authorization": f"Bearer {key}"
        }
        response = requests.get(url,headers=headers)
        return True if response.status_code == 200 else False
    elif llm == "GOOGLE":
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={key}"
        headers = {
            "Content-Type":"application/json"
        }
        data = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": "hi"
                        }
                    ]
                }
            ]
        }
        response = requests.post(url,headers=headers,json=data)
        return True if response.status_code == 200 else False
    
    return False
        
    


class ChatUtility:
    def __init__(self, user:str, llm_provider: str, api_key: str):
        self.user = user
        self.llm_provider = llm_provider
        self.api_key = api_key
        self.client = available_llms[llm_provider](api_key)
    
    def chat(self,message: str)->str:
        if self.llm_provider == "GOOGLE":
            response = self.client.models.generate_content_stream(
                model="gemini-2.0-flash",
                contents=[message]
            )
            for chunk in response:
                print(chunk.text, end="")
        elif self.llm_provider == "ANTHROPIC":
            with self.client.messages.stream(
                max_tokens=1024,
                messages=[{"role": "user", "content": message}],
                model="claude-3-7-sonnet-20250219",
            ) as stream:
                for text in stream.text_stream:
                    print(text, end="", flush=True)
        elif self.llm_provider == "OPENAI":
            stream = self.client.responses.create(
                model="gpt-4o",
                input=[
                    {
                        "role": "user",
                        "content": message,
                    },
                ],
                stream=True,
            )
            for event in stream:
                print(event)

            
        
