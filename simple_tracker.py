import requests
from bs4 import BeautifulSoup
import hashlib
from tinydb import TinyDB, Query 
import time
from datetime import datetime as dt
import uuid
from notifications import send_email



def get_product(url):
    headers = {
        'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 OPR/69.0.3686.77",
        'Cookie': '',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'gzip, deflate, br',
        'Connection':'keep-alive'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    product_title = soup.find(id='productTitle').text.replace('\n','').strip()
    try:
        price_str = soup.findAll("span","a-size-medium a-color-price")[0].text
    except Exception:
        price_str = soup.findAll("span","a-size-base a-color-price")[0].text
    price = ""
    currency = ""
    for i in price_str:
        if i.isdigit() or i==".":
            price += i
        else:
            currency += i
    currency = currency.replace('\n','').replace('\u00a0','').replace(',','')
    id = hashlib.sha256(product_title.encode("utf-8")).hexdigest()
    return {'product_price':price, 'product_title':product_title, 'previous_price':price,'id':id, 'currency':currency, 'url':url}


def track_prices_from_amzn():
    while True:
        user_db = TinyDB('json/product.json')
        user_product = user_db.all()
        search = Query()
        for prd in user_product:
            while True:
                status = True
                try:
                    result = get_product(prd['url'])
                except Exception:
                    status = False
                    pass
                if status:
                    break
            current_price = float(prd['product_price'])
            new_price = float(result['product_price'])
            if current_price - new_price > 0:
                price_drop = current_price - new_price
                user_db.update({'product_price':str(new_price), 'previous_price':str(current_price)}, search.id == prd['id'])
                send = user_db.search(search.id == prd['id'])
                
                send_data = [{
                    "Product Title": send[0]['product_title'],
                    "Price": send[0]['currency']+" "+send[0]['product_price'],
                    "Price Before": send[0]['currency']+" "+send[0]['previous_price'],
                    "URL":send[0]['url'],
                    'id':str(uuid.uuid1())
                }]
                
            notification_list = TinyDB("json/notification.json")
            notification_list.insert(send_data[0])

            email_list = TinyDB("json/email.json")
            email_user = email_list.all()
            for i in email_user:
                send_email(i['email'], send_data)
            time.sleep(60*60*24)    
                

        now = dt.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        set_db = TinyDB("json/setting.json")
        set_search = Query()
        set_db.update({'content':str(current_time)}, set_search.title == "time")
        print("Product Checked on - "+str(current_time))
        

        result = set_db.search(set_search.title == "sleep_time")
        sleep_time = result[0]['content']
        time.sleep(int(sleep_time))
        