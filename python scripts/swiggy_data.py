import urllib.request
import json

import numpy as np

menuLink = 'https://www.swiggy.com/dapi/menu/v4/full?menuId='
def menus(id):
    link = f'https://www.swiggy.com/dapi/menu/v4/full?menuId={id}'
    rest_info = []
    with urllib.request.urlopen(link) as url:
        item_info1 = []

        information = json.loads(url.read().decode())
        data = information['data']
        name = data['name']
        item_info1.append(name)
        rating = data['avgRating']
        item_info1.append(rating)
        costfortwo = data["costForTwo"] / 100
        latLong = data["latLong"]

        item_info1.append(costfortwo)
        cuisines = data['cuisines']
        c = []
        for i in range(len(cuisines)):
            c.append(cuisines[i])

        item_info1.append(c)
        item_info1.append(latLong)
        # rest_info.append(name)
        rest_info.append(item_info1)
        items = data['menu']['items']
        for item in items:
            item_info = []
            item_info.append(items[item]['name'])
            item_info.append(items[item]['category'])
            item_info.append((items[item]['price'] / 100) + (items[item]['price'] % 100))
            item_info.append(items[item]['isVeg'])
            np.unique(item_info)
            rest_info.append(item_info)
    return rest_info


def fetchRestaurants(lat, lng, offset=0):
    link = f'https://www.swiggy.com/dapi/restaurants/list/v5?lat={lat}&lng={lng}&offset={offset}&sortBy=DELIVERY_TIME&pageType=SEE_ALL&page_type=DESKTOP_SEE_ALL_LISTING'
    print('fetching', link)

    restaurantIDs = []

    with urllib.request.urlopen(link) as url:
        data = json.loads(url.read().decode())
        cards = data['data']['cards']

        for card in cards:
            if card['cardType'] == 'seeAllRestaurants':
                moreCards = card['data']['data']['cards']

                for childCard in moreCards:
                    print(childCard['data']['name'])
                    restaurantIDs.append(childCard['data']['id'])
            elif card['cardType'] == 'restaurant':
                print(card['data']['data']['name'])
                restaurantIDs.append(card['data']['data']['id'])

    return restaurantIDs
total_restaurants=[]
restaurantIDs = []
menu_list = []
tot_res = 0
long=[28.5261,28.354  ,28.5261 ]
latidudes=[77.0800, 77.057,77.0800 ]
for i in range(len(long)):
    lon =long[i]
    lat =latidudes[i]
    for tot_res in range(10):
        restaurants = (fetchRestaurants(lon,lat, tot_res))
        for j in range(len(restaurants)):
            restaurantIDs.append(restaurants[j])
        tot_res = tot_res + len((restaurantIDs))
        print(tot_res)
    np.unique(restaurantIDs)
    print(len(restaurantIDs))
    total_restaurants.append(restaurantIDs)

print(total_restaurants)
print(len(total_restaurants[0]))
print(len(total_restaurants[1]))
print(len(total_restaurants[2]))
# print(np.unique(total_restaurants[0]))
print(len(np.unique(total_restaurants[0])))
# print(np.unique(total_restaurants[1]))
print(len(np.unique(total_restaurants[1])))
# print(np.unique(total_restaurants[2]))
print(len(np.unique(total_restaurants[2])))
list=[]
for i in range(len(total_restaurants)):
    for j in range(len(total_restaurants[i])):
        list.append(total_restaurants[i])

# print(list)
print(np.unique(list))
print(len(np.unique(list)))
list1 = np.unique(list)
print(list1.tolist())
