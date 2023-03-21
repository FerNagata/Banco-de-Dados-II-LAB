from database import Database
from writeAJson import writeAJson

class ProductAnalyzer:
    def __init__(self, database:Database):
        self.database = database
    
    def totalVendas(self):
        result = self.database.collection.aggregate([
            {"$unwind": "$produtos"}, 
            {"$group": { "_id": "$data_compra", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
        ])
        return result
    
    def produtoMaisVendidos(self):
        result = self.database.collection.aggregate([
            {"$unwind":"$produtos"},
            {"$group": { "_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])
        return result

    def clienteMaisGastou(self):
        result = self.database.collection.aggregate([
            {"$unwind":"$produtos"},
            {"$group": { "_id": "$cliente_id","total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])
        return result
    
    def listaProdutos(self): 
        result = self.database.collection.aggregate([
            {"$unwind":"$produtos"},
            {"$group": { "_id": "$produtos.descricao","quantidade": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"quantidade": -1}},
            {"$match": {"quantidade": {"$gt":1}}}
        ])
        return result



