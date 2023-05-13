class Game:
    def __init__(self, database):
        self.db = database
    
    def create_player(self, name): # id é criado automaticamente
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_match(self, name, namePlayer):
        query = "CREATE (:Match {name: $name, ganhou: $namePlayer})"
        parameters = {"name": name, "namePlayer": namePlayer}
        self.db.execute_query(query, parameters)

    # relação entre o player e o match, sendo assim, os jogadores que jogaram nessa partida
    def create_relacao(self, namePlayer, nameMatch):
        query = "MATCH (m:Match {name: $nameMatch}), (p:Player {name: $namePlayer}) CREATE (p)-[:JOGOU]->(m)"
        parameters = {"namePlayer": namePlayer, "nameMatch": nameMatch, "ganhou": namePlayer}
        self.db.execute_query(query, parameters)
    
    # Retorna todos os jogadores
    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]
    
    # Retorna as caracteristicas de uma partida específica
    def get_match(self, nameMatch):
        query = "MATCH (m:Match{name: $nameMatch}) RETURN m.name AS name, m.ganhou AS ganhou"
        parameters = {"nameMatch": nameMatch}
        results = self.db.execute_query(query, parameters)
        return f'Nome partida: ' + results[0]["name"] + '\nGanhador: ' + results[0]["ganhou"]
    
    # Retorna os jogadores que jogaram em uma partida especifica
    def get_participantes(self, nameMatch):
        query = "MATCH (m:Match{name: $nameMatch})<-[:JOGOU]-(p:Player) RETURN p.name AS name"
        parameters = {"nameMatch": nameMatch}
        results = self.db.execute_query(query, parameters)
        return [result["name"] for result in results]
    
    # Retorna as partidas jogadas por um player específico
    def get_partidas(self, namePlayer):
        query = "MATCH (p:Player{name: $namePlayer})-[:JOGOU]->(m:Match) RETURN m.name AS name"
        parameters = {"namePlayer": namePlayer}
        results = self.db.execute_query(query, parameters)
        return [result["name"] for result in results]

    # atualiza o nome dos jogadores
    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)
    
    def delete_player(self, namePlayer):
        query = "MATCH (p:Player {name: $namePlayer}) DETACH DELETE p"
        parameters = {"namePlayer": namePlayer}
        self.db.execute_query(query, parameters)

    def delete_match(self, nameMatch):
        query = "MATCH (p:Match {name: $nameMatch}) DETACH DELETE p"
        parameters = {"nameMatch": nameMatch}
        self.db.execute_query(query, parameters)


