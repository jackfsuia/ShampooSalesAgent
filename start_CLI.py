# MODEL name supports openai, kimi, baichuan, qwen, Hugggingface models. Hugggingface models don't need a KEY.
import sys
from utils.model_choose import get_selling_talk
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
    selling_talk = get_selling_talk(sys.argv)
    CLI_interface(selling_talk)
