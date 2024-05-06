import os
from openai import OpenAI

from chat_flow.normal_flow import salesAgent

class gpt_salesAgent(salesAgent):
    def __init__(self, MODEL, KEY):

        if MODEL == 'gpt':
            MODEL="gpt-3.5-turbo"
        super().__init__(MODEL, KEY)
        os.environ["OPENAI_API_KEY"] = self.KEY
        self.client = OpenAI()

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
        

    

  
