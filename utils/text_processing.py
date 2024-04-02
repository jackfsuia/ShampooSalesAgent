import re

def I_process_customer_text(customer_text):
    return "客户说：" + customer_text + "。"

def template_history(history, process_customer_text):
    templated_history = []
    for msg in history:
        templated_history += [
            {"role": "user", "content": process_customer_text(msg[0])},
            {"role": "assistant", "content": msg[1]},
        ]

    return templated_history

