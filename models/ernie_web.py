import requests
import re
import json
from chat_flow.normal_flow import salesAgent


class ernie_salesAgent(salesAgent):

    def __init__(self, MODEL, API_Key, Secret_Key):
        super().__init__(MODEL)
        self.API_Key=API_Key
        self.Secret_Key=Secret_Key
        self.URL = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + self.get_access_token
        self.headers = {
        'Content-Type': 'application/json'
        }

    @property
    def get_access_token(self):
            
        url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={self.API_Key}&client_secret={self.Secret_Key}"
        
        payload = json.dumps("")
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json().get("access_token")
    
    def talk_to_seller(self, query, history):
        #baidu好像不接受system prompt
        history=history[1:]
        history += [{
            "role": "user", 
            "content": query
        }]

        data = json.dumps({
            "messages": history,
            "stream": True
        })
           
        response = requests.request("POST", self.URL, headers=self.headers, data=data, stream=True)

        for r in response.iter_lines():
            response_str=r.decode('utf-8')
            result=""
            try:
                result = json.loads(response_str[6:])["result"]
            except:
                result = response_str
            yield result

    
  
