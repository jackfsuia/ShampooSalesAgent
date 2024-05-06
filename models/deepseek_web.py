# python3
from openai import OpenAI

from chat_flow.normal_flow import salesAgent

class deepseek_salesAgent(salesAgent):
    def __init__(self, MODEL, KEY):

        if MODEL == 'deepseek':
            MODEL="deepseek-chat"
        super().__init__(MODEL, KEY)
        
        self.client = OpenAI(api_key=KEY, base_url="https://api.deepseek.com/v1")

    def talk_to_seller(self, query, history):
        history += [{
            "role": "user", 
            "content": query
        }]

        response = self.client.chat.completions.create(
        model=self.MODEL,
        messages=history,
        stream=True
        )

        for r in response:
            yield r.choices[0].delta.content
