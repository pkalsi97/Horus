import requests

def validate_api_key(key: str) -> bool:
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
