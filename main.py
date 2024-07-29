from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://kybavolodymyr:pnMZYLGcsYBsVHlQ@cluster1.09zlux5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1",
    server_api=ServerApi('1')
)

db = client.Book

def show_all_pets():
    all_pets = db.cats.find({})
    return [ pets for pets in all_pets ]

def find_by_name(pet_name):
    return db.cats.find_one({"name" : pet_name})

def update_pet_age(pet_name, new_age):
    return db.cats.update_one({"name" : pet_name}, {"$set": {"age": new_age}})

def update_pet_features(pet_name,new_features):
    return db.cats.update_one({"name" : pet_name},{"$push": {"features": {"$each": new_features}}}, upsert=True )

def delete_by_name(pet_name):
    return db.cats.delete_one({"name" : pet_name})

def delete_all_data():
    return db.cats.delete_many({})

if __name__ == "__main__":
    pass


    
   
