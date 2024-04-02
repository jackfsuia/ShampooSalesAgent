from openai import OpenAI

from chat_flow.normal_flow import salesAgent

class kimi_salesAgent(salesAgent):
    def __init__(self, MODEL, KEY):
        if KEY == None:
            print('key missing') 
            return
        self.URL = 'https://api.moonshot.cn/v1'
        if MODEL == 'kimi':
            MODEL='moonshot-v1-8k'
        self.client = OpenAI(KEY, self.URL)
        super().__init__(MODEL, KEY)

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

        return response

    
    def correct_response(self,response):
        content = response.choices[0].delta.content
        return content

    