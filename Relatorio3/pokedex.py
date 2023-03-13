from database import Database
from helper.writeAJson import writeAJson # é uma função que cria um log, em formato json

class Pokedex:
    def __init__(self, database:Database):
        self.database = database

    def nome(self, nome): #pesquisa um pokemon pelo nome dele
        pokemon_nome = self.database.collection.find_one({"name":nome})
        writeAJson(pokemon_nome, "pokemon")

    def tipo(self, tipo: list): #procura um pokemon com tipo(s) específico(s)
        pokemon_tipo = self.database.collection.find({"type": {"$in": tipo}})
        writeAJson(pokemon_tipo, "pokemons_by_type")

    def fraqueza(self, fraqueza: list): # procura um pokemon pela suas fraquezas
        pokemon_fraqueza = self.database.collection.find({"weaknesses": {"$all": fraqueza}})
        writeAJson(pokemon_fraqueza, "pokemons_by_weakness")

    def evolucao(self): #procura por pokemons que possuem apenas mais uma evolução
        pokemon_evolucao = self.database.collection.find({"next_evolution": {"$exists": True, "$size": 1}})
        writeAJson(pokemon_evolucao, "pokemons_has_evolucion")

    def spawn(self, min, max): #procura por pokemons que tem chance de spawn entre {min} e {max}
        pokemon_spawn = self.database.collection.find({"spawn_chance": {"$gt": min, "$lt": max}})
        writeAJson(pokemon_spawn, "pokemons_spawn")


'''
db = Database(database="pokedex", collection="pokemons")
pokedex = Pokedex(db) 
pokedex.nome("Charizard")
pokedex.tipo(["Flying"])
pokedex.fraqueza(["Electric", "Rock"])
pokedex.evolucao()
pokedex.spawn(0.5, 0.7)
'''