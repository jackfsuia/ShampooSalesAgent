import csv
import re
import datetime
import os
def extract_order_string(text):
    pattern = r"<[^<>]+><[^<>]+><[^<>]+><[^<>]+><[^<>]+>"

    match = re.search(pattern, text)

    if match:
        return match.group(0)
    else:
        return None

def print_orders_to_csv(order, csvfile ='customer_orders.csv'):

    pattern = re.compile(r'<([^<>]+)>')

    matches = pattern.findall(order)

    order_time = order[: order.index("<")]

    fieldnames = ["订单时间(order time)", "客户姓名(customer name)", "地址(address)", "联系方式(phone number)", "购买数量(purchase quantity)", "付款总额(payment amounts)"]
    orders = [
        {
            "订单时间(order time)": order_time,
            "客户姓名(customer name)": matches[0],
            "地址(address)": matches[1],
            "联系方式(phone number)": matches[2],
            "购买数量(purchase quantity)": matches[3],
            "付款总额(payment amounts)": matches[4],
        }
    ]

    with open(csvfile, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if os.stat(csvfile).st_size < 10:
            writer.writeheader()
        for order in orders:
            writer.writerow(order)

    print(f"Customer order information has been written to {csvfile}")

def order_check(order_string):
    if order_string == None:
        return False
    info_pattern = re.compile(r'<([^<>]+)>')
    matches = info_pattern.findall(order_string)
    digit_pattern = r'\d'
    if re.search(digit_pattern, matches[2]) and re.search(digit_pattern, matches[3]) and re.search(digit_pattern, matches[4]):
        return True
    return False


def print_order(collected_messages):
    order_string = extract_order_string(collected_messages)
    if order_check(order_string):
        order_time = str(datetime.datetime.now())
        print(f"{order_time} {order_string}")
        print_orders_to_csv(order_time + order_string)
