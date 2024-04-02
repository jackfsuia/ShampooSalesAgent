import pandas as pd
import re
def to_yuan(money_str, exchange_rate_to_yuan = 1):
    match = re.search(r'\d+', money_str)
    if match:
        number = int(match.group())
    else:
        raise ValueError("illegal payment amounts.金额项异常")
    return exchange_rate_to_yuan*number
def sum_payment_amounts(file_path, exchange_rate_to_yuan=1):

    df = pd.read_csv(file_path)

    return len(df['付款总额(payment amounts)']), sum([to_yuan(i,exchange_rate_to_yuan) for i in df['付款总额(payment amounts)']])