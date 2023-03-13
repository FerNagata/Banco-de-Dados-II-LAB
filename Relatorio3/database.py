from typing import Collection
import pymongo
from dataset.pokemon_dataset import dataset

class Database:
    def __init__(self, database, collection):
        self.connect(database, collection) #está conectando com o banco de dados

    def connect(self, database, collection):
        try:
            connectionString = "localhost:27017"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True #evita alguns erros
            )
            self.db = self.clusterConnection[database] #abstração dentro do python do bd
            self.collection = self.db[collection] #abstração da collection
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)

    def resetDatabase(self):
        try: 
            self.db.drop_collection(self.collection)
            self.collection.insert_many(dataset)
            print("Banco de dados resetado com sucesso!")
        except Exception as e:
            print(e)