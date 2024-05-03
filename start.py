# MODEL name supports openai, kimi, baichuan, qwen, Hugggingface models. Hugggingface models don't need a KEY.
import sys
import gradio as gr
from utils.model_choose import get_selling_talk
if __name__ == '__main__':
    selling_talk = get_selling_talk(sys.argv)
    gr.ChatInterface(selling_talk).launch(share=True)