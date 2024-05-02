# MODEL name supports openai, kimi, baichuan, qwen, Hugggingface models. Hugggingface models don't need a KEY.
import sys

def CLI_interface(selling_talk):
    history = []
    while True:
        print("\r\033[0;33;40mCustomer(客户):\033[0m", end="", flush=True)
        customer_text = input()
        if len(customer_text) == 0:
            continue
            # exit
        if customer_text.lower() == "exit":
            break

        res_stream = selling_talk(customer_text, history)

        print("\r\033[0;32;40mSellsAgent(推销员):\033[0m", end="")
        start_pos = 0
        for res in res_stream:
            print(res[start_pos:], end="", flush=True)
            start_pos = len(res)
        print("\n",end='')


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        raise Exception("Needs arguments: model, key. For huggingface model, key is not needed.（请传入参数：模型名，你的访问key。huggingface模型不用参数key。）:")
    else:
        MODEL = sys.argv[1]
        if len(sys.argv) == 3:
            KEY = sys.argv[2]
            if MODEL.startswith("baichuan") or MODEL.startswith("Baichuan"):
                from models import baichuan_web
                selling_talk = baichuan_web.baichuan_salesAgent(MODEL, KEY).closuer_selling_talk()
            elif MODEL.startswith("kimi") or MODEL.startswith("moonshot"):
                from models import kimi_web
                selling_talk = kimi_web.kimi_salesAgent(MODEL, KEY).closuer_selling_talk()
            elif MODEL.startswith("qwen"):
                from models import qwen_web
                selling_talk = qwen_web.qwen_salesAgent(MODEL, KEY).closuer_selling_talk()
            elif MODEL.startswith("gpt"):
                from models import gpt_web
                selling_talk = gpt_web.gpt_salesAgent(MODEL, KEY).closuer_selling_talk()
            elif MODEL.startswith("ernie"):
                raise Exception("ernie needs API Key and Secret Key. You're missing one of them.(文心一言需要API Key 和 Secret Key, 您少输入了一个。)")
            print(f'You are using {MODEL}\'s API.(你在调用{MODEL}的API。)')
        elif len(sys.argv) == 4 and (MODEL.startswith("ernie") or MODEL.startswith("ERNIE")):
            from models import ernie_web
            selling_talk = ernie_web.ernie_salesAgent(MODEL, API_Key=sys.argv[2], Secret_Key=sys.argv[3]).closuer_selling_talk()
            print(f'You are using {MODEL}\'s API.(你在调用{MODEL}的API。)')
        elif len(sys.argv) == 2:   
            from models import hf_model_web
            selling_talk = hf_model_web.huggingface_salesAgent(MODEL).closuer_selling_talk()
            print(f'You are using huggingface model {MODEL}.(你在用huggingface模型{MODEL}。)')
        else:
            raise Exception("No such model or too many arguments.(此模型不存在或者参数过多。)")
        
        CLI_interface(selling_talk)
