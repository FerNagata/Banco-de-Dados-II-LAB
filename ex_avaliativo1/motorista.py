from database import Database
from bson.objectid import ObjectId
from corrida import Corrida
from typing import List

class Motorista:
    def __init__(self, corrida:List[Corrida], nota: int):
        self.nota = nota
        self.corrida = corrida


class MotoristaDAO: # DAO - Data Access Object
    def __init__(self):
        self.db = Database(database="atlas-cluster", collection="Motorista")
    def criar(self, motorista:Motorista):
        try:
            res = self.db.collection.insert_one({
                "corrida": [{
                    "nota": motorista.corrida.nota,
                    "distancia": motorista.corrida.distancia,
                    "valor": motorista.corrida.valor,
                    "passageiro": {
                        "nome": motorista.corrida.passageiro.nome,
                        "documento": motorista.corrida.passageiro.documento
                    }
                }], 
                "nota": motorista.nota
                })
            print(f"Motorista criado com o id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Houve um erro ao tentar criar o motorista: {e}")
            return None

    def ler(self, id: str):
        try:
            res = self.db.collection.find({"_id": ObjectId(id)}, #filter 
                                              {"nota": 1, "corrida": 1, "passageiro": 1, "_id": 0}) #project - mostra a nota, corrida e passageiro, porém não mostra o id
            return res
        except Exception as e:
            print(f"Houve um erro ao tentar ler o motorista: {e}")
            return None

    def atualizar(self, id: str, nota:int): # atualiza a nota do motorista
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"nota": nota}})
            print(f"Motorista atualizado: {res.modified_count} documento(s) modificado")
            return res.modified_count
        except Exception as e:
            print(f"Houve um erro ao tentar atualizar o motorista: {e}")
            return None

    def deletar(self, id: str): # deleta o motorista
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deletado: {res.deleted_count} documento(s) deletado")
            return res.deleted_count
        except Exception as e:
            print(f"Houve um erro ao tentar deletar o motorista: {e}")
            return None
        
    def add_corrida(self, id:str, corrida:Corrida): # adiciona uma corrida ao motorista com o id informado
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$push": 
                                                                        {"corrida": {
                                                                            "nota": corrida.nota,
                                                                            "distancia": corrida.distancia,
                                                                            "valor": corrida.valor,
                                                                            "passageiro": {
                                                                                "nome": corrida.passageiro.nome,
                                                                                "documento": corrida.passageiro.documento
                                                                            }
                                                                        }}})
            print(f"Motorista atualizado: {res.modified_count} documento(s) modificado")
            return res.modified_count
        except Exception as e:
            print(f"Houve um erro ao tentar adicionar uma nova corrida: {e}")
            return None

        
