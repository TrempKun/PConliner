
from email.mime import image
import requests


def parce(price):
    
    price = str(round(float(price))) + ".00"
    url = f'https://catalog.onliner.by/sdapi/catalog.api/search/desktoppc?price[to]={price}&desktoppc_type[0]=desktop&desktoppc_type[operation]=union&group=1'
    url = url.format(price)
       
    r = requests.get(url)
    products = r.json()["products"]

    
    return [{'text': {"name": product["extended_name"],
    "price": float(product["prices"]["price_min"]["amount"]),
    "description": product['description'],
    'html_url': product['html_url']}, "image": product["images"]["header"]} for product in products if product["prices"] != None]



def take_popular_price(price):
    all_products = parce(price)
    return all_products[:5]

def take_value(price):
    close_price = take_popular_price(price)
    for i in close_price:
       i['text'] = (f"Название: {i['text']['name']} \n\n Цена: {i['text']['price']} BYN \n\n Описание: {i['text']['description']} \n\n Ссылка: {i['text']['html_url']}")
       i['image'] = 'https:'+ i['image']
    return close_price

print(take_value(530))


