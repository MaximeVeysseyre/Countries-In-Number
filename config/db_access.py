from pymongo import MongoClient
import random

from config.ressources import *

from bson.int64 import Int64


class DatabaseManager:

    """
    Provide methods and connection to the MongoDb database
    """

    __CONNECTION_STRING = str.format(f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_SERVER}/{DB_NAME}?retryWrites=true&w=majority")
    __instance = None


    @staticmethod
    def getInstance():
        """ Static access method. """
        if DatabaseManager.__instance == None:
            DatabaseManager()
        return DatabaseManager.__instance


    def __init__(self):
        """ Virtually private constructor. """
        if DatabaseManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            DatabaseManager.__instance = self
            print(DatabaseManager.__CONNECTION_STRING)
            self.__client = MongoClient(DatabaseManager.__CONNECTION_STRING)


    def __get_collection(self, db_name, collection_name):
        
        return self.__client.get_database(db_name).get_collection(collection_name)


    def get_country_by_name(self, name):

        return self.__get_collection('client-roi', 'country').find_one({'country_name': name})
    

    def add_fake_country(self, fake_name):

        density = random.randint(10, 1000)
        land_area = random.randint(100000, 1000000)
        pop = random.randint(10000, 10000000)
        
        country={"country_name": fake_name, 
                    "pop": pop,
                    "density": density, 
                    "land_area": land_area,
                    }

        self.__get_collection('client-roi', 'country').insert_one(country)

        return self.__get_collection('client-roi', 'country').find_one({'country_name': fake_name})
    

    def get_density_slice(self):

        density_1 = {'density': {"$lt" : Int64(200)}}
        density_2 = {'density': {"$gt" : Int64(200), "$lt" : Int64(400)}}
        density_3 = {'density': {"$gt" : Int64(400), "$lt" : Int64(600)}}
        density_4 = {'density': {"$gt" : Int64(600)}}

        density_slice_1 = self.__get_collection('client-roi', 'country').find(density_1)
        density_slice_2 = self.__get_collection('client-roi', 'country').find(density_2)
        density_slice_3 = self.__get_collection('client-roi', 'country').find(density_3)
        density_slice_4 = self.__get_collection('client-roi', 'country').find(density_4)

        return {'Slice 1' : density_slice_1, 'Slice 2' : density_slice_2, 'Slice 3' : density_slice_3, 'Slice 4' : density_slice_4}
        