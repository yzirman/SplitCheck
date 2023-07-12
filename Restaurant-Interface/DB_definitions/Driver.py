import json

from feedb.db.DBConnection import MongoDBConnection

if __name__ == "__main__":

    CONNECTION_STRING = "mongodb+srv://Cluster16422:helloWorld@cluster0.x2xfr.mongodb.net/test"

    db = MongoDBConnection(CONNECTION_STRING)

    foods = db.get_foods_collection().find({})
    rest = db.get_restaurant_collection('Restaurant_03').find()

    print(type(foods))
    print(type(rest))

    with open('restjson.json') as f:
        data = json.load(f)

    res2 = 'Restaurant_03'
    db.add_restaurant(res2, data)

    print(db.get_restaurant_menu(res2))


