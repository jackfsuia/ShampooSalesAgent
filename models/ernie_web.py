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
        """
        使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
        """
            
        url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={self.API_Key}&client_secret={self.Secret_Key}"
        
        payload = json.dumps("")
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json().get("access_token")
    
    def talk_to_seller(self, query, history):
        history += [{
            "role": "user", 
            "content": query
        }]

        data = json.dumps({
            "messages": history,
            "stream": True
        })
           
        response = requests.request("POST", self.URL, headers=self.headers, data=data, stream=True)

        return response.iter_lines()

    
    def correct_response(self,response):
        response_str=response.decode('utf-8')
        pattern = r'"result":"([^"]*)"'
        match = re.search(pattern, response_str)
        if match:
            return match.group(1)
        pattern = r'"error_msg":"([^"]*)"'
        match = re.search(pattern, response_str)
        if match:
            return match.group(1)
        return None
