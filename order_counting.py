import eval.counting_money as cnt
import sys
import os
if __name__ == '__main__':

    current_dir = os.getcwd()
    exchange_rate_to_yuan=1
    if len(sys.argv) >= 2:
        for csvfile in sys.argv[1:]:
            order_number, order_money= cnt.sum_payment_amounts(os.path.join(current_dir, csvfile),exchange_rate_to_yuan=exchange_rate_to_yuan)
            print(f'num of orders is {order_number}, order_money is {order_money}')
    else:
        order_number, order_money= cnt.sum_payment_amounts(os.path.join(current_dir, "customer_orders.csv"),exchange_rate_to_yuan=exchange_rate_to_yuan)
        print(f'num of orders is {order_number}, order_money is {order_money} yuan')
