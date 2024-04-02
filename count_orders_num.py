import eval.counting_cunstomer_orders as cnt
import sys
import os
if __name__ == '__main__':

    current_dir = os.getcwd()
    print(current_dir)
    if len(sys.argv) >= 2:
        for csvfile in sys.argv[1:]:
            print(f'num of orders is {cnt.count_order_lines_in_csv(os.path.join(current_dir, csvfile))}')
    else:
        print(os.path.join(current_dir,"customer_orders.csv"))
        print(f'Number of orders is {cnt.count_order_lines_in_csv(os.path.join(current_dir,"customer_orders.csv"))}')