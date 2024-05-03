from zhipuai import ZhipuAI

from chat_flow.normal_flow import salesAgent

class zhipu_salesAgent(salesAgent):
    def __init__(self, MODEL, KEY):

        if MODEL == 'glm' or MODEL == 'zhipu' or MODEL == 'GLM':
            MODEL="glm-4"
        super().__init__(MODEL, KEY)
        self.client = ZhipuAI(api_key=self.KEY)

    def talk_to_seller(self, query, history):
        history += [{
            "role": "user", 
            "content": query
        }]

        response = self.client.chat.completions.create(
            model=self.MODEL,  
            messages=history,
            stream=True,
        )
                            
        return response

    
    def correct_response(self,response):
        content = response.choices[0].delta.content
        return content
