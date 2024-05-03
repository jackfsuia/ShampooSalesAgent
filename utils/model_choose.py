    
def get_selling_talk(argv):
    if len(argv) <= 1:
        raise Exception("Needs arguments: model, key. For huggingface model, key is not needed.（请传入参数：模型名，你的访问key。huggingface模型不用参数key。）:")
    else:
        MODEL = argv[1]
        if len(argv) == 3:
            KEY = argv[2]
            print(f'You are using {MODEL}\'s API.(你在调用{MODEL}的API。)')
            if MODEL.startswith("baichuan") or MODEL.startswith("Baichuan"):
                from models import baichuan_web
                return baichuan_web.baichuan_salesAgent(MODEL, KEY).closuer_selling_talk()
            elif MODEL.startswith("kimi") or MODEL.startswith("moonshot"):
                from models import kimi_web
                return kimi_web.kimi_salesAgent(MODEL, KEY).closuer_selling_talk()
            elif MODEL.startswith("qwen"):
                from models import qwen_web
                return qwen_web.qwen_salesAgent(MODEL, KEY).closuer_selling_talk()
            elif MODEL.startswith("gpt"):
                from models import gpt_web
                return gpt_web.gpt_salesAgent(MODEL, KEY).closuer_selling_talk()
            elif MODEL.startswith("claude") or MODEL.startswith("anthropic"):
                from models import anthropic_web
                return anthropic_web.anthropic_salesAgent(MODEL, KEY).closuer_selling_talk()
            elif MODEL.startswith("ernie"):
                raise Exception("ernie needs API Key and Secret Key. You're missing one of them.(文心一言需要API Key 和 Secret Key, 您少输入了一个。)")
        elif len(argv) == 4 and (MODEL.startswith("ernie") or MODEL.startswith("ERNIE")):
            print(f'You are using {MODEL}\'s API.(你在调用{MODEL}的API。)')
            from models import ernie_web
            return ernie_web.ernie_salesAgent(MODEL, API_Key=argv[2], Secret_Key=argv[3]).closuer_selling_talk()
        elif len(argv) == 2:   
            print(f'You are using huggingface model {MODEL}.(你在用huggingface模型{MODEL}。)')
            from models import hf_model_web
            return hf_model_web.huggingface_salesAgent(MODEL).closuer_selling_talk()
        else:
            raise Exception("No such model or too many arguments.(此模型不存在或者参数过多。)")