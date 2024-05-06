from openai import OpenAI

from chat_flow.normal_flow import salesAgent

class kimi_salesAgent(salesAgent):
    def __init__(self, MODEL, KEY):
 
        if MODEL == 'kimi':
            MODEL='moonshot-v1-8k'
        super().__init__(MODEL, KEY)
        self.URL = 'https://api.moonshot.cn/v1'
        self.client = OpenAI(api_key =self.KEY, base_url =self.URL)

    def talk_to_seller(self, query, history):
        history += [{
            "role": "user", 
            "content": query
        }]

        response = self.client.chat.completions.create(
        model=self.MODEL,
        messages=history,
        temperature=0.3,
        stream=True
        )
        
        for r in response:
            yield r.choices[0].delta.content


    