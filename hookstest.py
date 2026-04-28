import requests
import os
import json
import asyncio
from dotenv import load_dotenv

load_dotenv()

HOOKS_URL = os.environ["OPENCLAW_HOOKS_URL"]

def foo():
    response = requests.post(f"{HOOKS_URL}/agent", 
                             headers={"Authorization": "Bearer leohooks"},
                             json={
                                "message": "Run this",
                                "name": "Email",
                                "agentId": "hooks",
                                "sessionKey": "hook:email:msg-123",
                                "wakeMode": "now",
                                "deliver": True,
                                "channel": "last",
                                "to": "+15551234567",
                                "model": "openai/gpt-5.2-mini",
                                "thinking": "low",
                                "timeoutSeconds": 120
                            })
    print(response.headers)
    print(response.content)
    print(response.status_code)
    return


if __name__=="__main__":
    foo()

