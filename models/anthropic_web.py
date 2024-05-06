

import anthropic

from chat_flow.normal_flow import salesAgent

class anthropic_salesAgent(salesAgent):
    def __init__(self, MODEL, KEY):

        if MODEL == 'claude':
            MODEL="claude-3-opus-20240229"
        super().__init__(MODEL, KEY)
        
        self.client=anthropic.Anthropic(api_key=self.KEY)

    def talk_to_seller(self, query, history):
        history += [{
            "role": "user", 
            "content": query
        }]


        stream = self.client.messages.stream(
            max_tokens=1024,
            messages=history,
            model=self.MODEL,
        ) 

        for r in stream.text_stream:
            yield r


