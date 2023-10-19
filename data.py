import requests
from dotenv import dotenv_values

config = dotenv_values(".env")
order_name = input('Order name: ')
language = ''
order_data = {}

shop_url = config['SHOP_URL']

def create_session():
    s = requests.Session()
    s.headers.update({
        'Content-Type': 'application/json',
        'X-Shopify-Access-Token': config['ACCESS_TOKEN']
    })
    return s

def datify(date):
    day = ''
    month = ''
    year = ''
    count = 0
    for i in date:
        if i == 'T':
            break
        else:
            if i == '-':
                count += 1
                continue
            else:
                if count == 0:
                    year += i
                elif count == 1:
                    month += i
                else:
                    day += i
    order_date = f"{day}.{month}.{year}"
    return order_date

def data(date, name, language):
    order_data.update({
        'date':date,
        'name':name,
        'language':language,
        'order_no':order_name
    })

def get_orders(orders):
    for i in orders:
        if i['name'] == order_name:
            language = i['customer_locale']
            customer = f"{i['customer']['first_name']} {i['customer']['last_name']}"
            data(datify(i['closed_at']), customer, language)

def main():
    sess = create_session()
    resp = sess.get(shop_url + "/admin/api/2023-10/orders.json?status=any")
    orders = resp.json()['orders']
    get_orders(orders)
