# MODEL name supports openai, kimi, baichuan, qwen, Hugggingface models. Hugggingface models don't require a real KEY.
import sys
import gradio as gr
from models import baichuan_web, kimi_web, qwen_web, gpt_web,local_model_web

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
            from models import local_model_web
            selling_talk = local_model_web.local_salesAgent(MODEL).closuer_selling_talk()
            print(f'You are using your local model {MODEL}.(你在用本地模型{MODEL}。)')
        else:
            raise Exception("No such model.(此模型不存在。)")

        print('Please go to one of the following  links to chat, and the second link can be shared. If the link crash during chat, please keep clicking the Retry button located at the bottom of the chat page. if you need it to speak English, you can just say \'speak english\' to it.(请点击以下任一网址进入聊天，第二个网址可以分享给其他人。聊天的时候崩溃请点聊天框下面的Retry按钮)')
        gr.ChatInterface(selling_talk).launch(share=True)
