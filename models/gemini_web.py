
import google.generativeai as genai

from chat_flow.normal_flow import salesAgent

class gemini_salesAgent(salesAgent):
    def __init__(self, MODEL, KEY):

        if MODEL == 'gemini':
            MODEL='gemini-pro'
        super().__init__(MODEL, KEY)
        genai.configure(api_key=KEY)
        self.chat = genai.GenerativeModel(self.MODEL).start_chat(history=[])

    def talk_to_seller(self, query, _):

        response = self.chat.send_message(query, stream=True)

        return response

    def correct_response(self,response):
        
        return response.text

