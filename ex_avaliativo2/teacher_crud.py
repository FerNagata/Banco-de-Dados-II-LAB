from database import Database

class TeacherCRUD:
    def __init__(self):
        self.db = Database("bolt://3.236.36.178:7687", "neo4j", "sea-vibration-wines")
    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)
        print("Professor criado!")

    def read(self, name):
        query = "MATCH (t:Teacher{name: $name}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return results

    def delete(self, name):
        query = "MATCH (t:Teacher {name: $name}) DETACH DELETE t"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
        print("Professor deletado!")

    def update(self, name, newCpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $newCpf"
        parameters = {"name": name, "newCpf": newCpf}
        self.db.execute_query(query, parameters)
        print(f"Dados do professor {name} atualizado!")