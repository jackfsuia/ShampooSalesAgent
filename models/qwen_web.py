import random
from http import HTTPStatus
import dashscope
from dashscope import Generation
from chat_flow.normal_flow import salesAgent

class qwen_salesAgent(salesAgent):
    def __init__(self, MODEL, KEY):

        if MODEL == 'qwen':
            MODEL='qwen1.5-72b-chat'
        super().__init__(MODEL, KEY)
        dashscope.api_key = KEY

    def talk_to_seller(self, query, history):
        history += [{
                "role": "user", 
                "content": query
            }]

        response = Generation.call(
            self.MODEL,
            messages=history,
            seed=random.randint(1, 10000),  # set the random seed, optional, default to 1234 if not set
            result_format='message',  # set the result to be "message"  format.
            stream=True,
            output_in_full=False  # get streaming output incrementally
        )

        for r in response:
            yield r.output.choices[0]['message']['content']

    
  
