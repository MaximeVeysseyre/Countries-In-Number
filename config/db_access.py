from config.ressources import *
from pymongo import MongoClient
import random


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
        """
        Generic method to connect to a given collection in a given database
        If the database or the collection don't exist, it will be created
        Args:
            db_name (str): name of the database
            collection_name (str): name of the collection
        Returns:
            collection: the collection
        """
        return self.__client.get_database(db_name).get_collection(collection_name)


    def get_country_by_name(self, name):
        """
        Get a country by its given name
        Args:
            name (str): name of the country
        Returns:
            json: informations about the country
        """
        return self.__get_collection('client-roi', 'country').find_one({'country_name': name})
    

    def add_fake_country(self, fake_name):
        """
        Insert a fake country by its given name
        Args:
            fake_name (str): name of the fake country
        Returns:
            json: informations about the fake country
        """
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
    

    # def get_density_slice(self, name):

    #     density_1 = {}