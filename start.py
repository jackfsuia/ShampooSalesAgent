# MODEL name supports openai, kimi, baichuan, qwen, Hugggingface models. Hugggingface models don't require a real KEY.
import sys
import gradio as gr
from models import baichuan_web, kimi_web, qwen_web, gpt_web,local_model_web

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Needs arguments: model, key. For huggingface model, key is not needed.（请传入参数：模型名，你的访问key。huggingface模型不用参数key。）:")
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
        else:
            from models import local_model_web
            selling_talk = local_model_web.local_salesAgent(MODEL).closuer_selling_talk()

        print('please go to one of the following  links to chat, and the second link can be shared. If the link crash during chat, please keep clicking the Retry button located at the bottom of the chat page. if you need it to speak English, you can just say \'speak english\' to it.(请点击以下任一网址进入聊天，第二个网址可以分享给其他人。聊天的时候崩溃请点聊天框下面的Retry按钮)')
        gr.ChatInterface(selling_talk).launch(share=True)
