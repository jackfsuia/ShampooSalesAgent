import requests
import re

from chat_flow.normal_flow import salesAgent

class baichuan_salesAgent(salesAgent):
    def __init__(self, MODEL, KEY):

        if MODEL == 'baichuan':
            MODEL='Baichuan2-Turbo'
        super().__init__(MODEL, KEY)
        
        self.URL = 'https://api.baichuan-ai.com/v1/chat/completions'
        self.headers = {
        "Content-Type": "application/json",
        "Authorization":f"Bearer {self.KEY}"
        }

    def talk_to_seller(self, query, history):
        history += [{
            "role": "user", 
            "content": query
        }]

        data = {
        "model": self.MODEL,
        "messages": history,
        "stream": True, 
        "temperature": 0,

        }
                            
        response = requests.post(self.URL, headers=self.headers, json=data, stream=True, timeout=60) 
        for r in response.iter_lines():
            pattern = r'"content":"([^"]*)"'
            match = re.search(pattern, r.decode('utf-8'))
            if match:
                yield match.group(1)

    
    
  
