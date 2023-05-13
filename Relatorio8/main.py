from database import Database
from game_database import Game

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
 #bolt URL, username, password
db = Database("bolt://44.195.91.131:7687", "neo4j", "exercises-bandages-recognition")
db.drop_all()

# Criando uma instância da classe Game para interagir com o banco de dados
game_db = Game(db)

# Criando players
game_db.create_player("João")
game_db.create_player("Maria")
game_db.create_player("José")
game_db.create_player("Ana")

# Criando partidas
game_db.create_match("Partida1", "João")
game_db.create_match("Partida2", "Maria")
game_db.create_match("Partida3", "Ana")

# Relacionando quem jogou tal partida
game_db.create_relacao("João", "Partida1")
game_db.create_relacao("José", "Partida1")
game_db.create_relacao("Maria", "Partida2")
game_db.create_relacao("Ana", "Partida2")
game_db.create_relacao("João", "Partida3")
game_db.create_relacao("Ana", "Partida3")
game_db.create_relacao("Maria", "Partida3")
game_db.create_relacao("José", "Partida3")

#Atualizando jogador
game_db.update_player("José", "Alfredo")

# Mostrando lista de jogadores
print("Lista de jogadores: ")
print(game_db.get_players())
print("---------------------------------")

# Mostra informações de uma partida específica
print(game_db.get_match("Partida1"))
print(f"Participantes dessa partida:")
print(game_db.get_participantes("Partida1"))
print("---------------------------------")

# Mostra as partidas jogadas por um player específico
print("Histórico de partidas jogadas pelo jogador escolhido: ")
print(game_db.get_partidas("Maria"))

#Deletando player
game_db.delete_player("Alfredo")

#Deletando Match
game_db.delete_match("Partida1")

db.close()