from pymongo import MongoClient

from feedb.db.restaurant.menu.Food import Food
from feedb.db.restaurant.menu.Menu import Menu


class MongoDBConnection(object):

    def __init__(self, connection) -> None:
        self.db = MongoClient(connection)

    def get_restaurant_db(self):
        return self.db['Restuarant']

    def get_foods_db(self):
        return self.db['Foods']

    def get_foods_collection(self):
        return self.get_foods_db()['Foods']

    def get_restaurant_collection(self, name):
        return self.get_restaurant_db()[name]

    def add_restaurant(self, name, data):
        if not self.contains_restaurant(name):
            self.create_restaurant_db_collection(name)
            self.get_restaurant_collection(name).insert_one(data)

    def contains_restaurant(self, name):
        return self.get_restaurant_db().list_collection_names().__contains__(name)

    def create_restaurant_db_collection(self, name):
        self.get_restaurant_db().create_collection(name)

    def get_restaurant_menu(self, restaurant):
        menu = Menu()
        for f in self.get_restaurant_collection(restaurant).find_one({"_id": "res01"}, {"menu": 1})['menu']:
            print(f)
            food = Food(f['id'], f['name'], f['price'])
            menu.addFood(food)
        return menu

    def print_restaurants(self):
        for r in self.get_restaurant_db().list_collection_names():
            print(r)