#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import re
import random
import sys

def get_dishes(cafe):
    r = requests.get("http://nambafood.kg/%s" % cafe)
    dishes = []
    for div in BeautifulSoup(r.content, 'html.parser').findAll('div', {"class": "dish-item"}):
        for price_div in div.findAll("div", {'class': 'price'}):
            price = re.sub('\D+', '', price_div.getText())
            dish_title = ""
            if int(price) <= 200:
                for dish_div in div.findAll('div', {'class': 'dish-description-title'}):
                    dish_title = " ".join(dish_div.getText().split())
                    dishes.append({
                        'title': dish_title,
                        'price': price
                        })
    return dishes


if __name__ == '__main__':
    try:
        cafe = sys.argv[1]
    except IndexError:
        print "I have no cafe in arguments"
        sys.exit(2)
    else:
        dishes = get_dishes(cafe)
        dish = random.choice(dishes)
        print "Your Choice"
        print dish.get('title'), dish.get('price')
