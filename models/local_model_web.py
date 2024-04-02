from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from threading import Thread
import torch
from chat_flow.normal_flow import salesAgent

class local_salesAgent(salesAgent):
    def __init__(self, MODEL):
        if MODEL == None:
            print('model missing') 
            return
        
        def try_gpu(i=0):
            if torch.cuda.device_count() >= i + 1:
                return torch.device(f'cuda:{i}')
            return torch.device('cpu')
        
        self.device = try_gpu()
        self.tok = AutoTokenizer.from_pretrained(MODEL,trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(MODEL, trust_remote_code=True, device_map="auto")

        super().__init__(MODEL)

    def talk_to_seller(self, query, history):
        history += [{
            "role": "user", 
            "content": query
        }]

        input_ids = self.tok.apply_chat_template(
                history ,
                tokenize=True,
                add_generation_prompt=True,
                return_tensors="pt"
            ).to(self.device)
        streamer = TextIteratorStreamer(self.tok, skip_prompt=True, skip_special_tokens=True)

        generation_kwargs = {'input_ids': input_ids, "streamer":streamer, "max_new_tokens":500}
        thread = Thread(target=self.model.generate, kwargs=generation_kwargs)
        thread.start()

        return streamer
    
    def correct_response(self, response):
        
        return response

            

  
