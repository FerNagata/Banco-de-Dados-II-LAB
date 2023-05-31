from database import Database

class Querys:
    def __init__(self, database):
        self.db = database
    
    def getTeacher(self, name):
        query = "MATCH (t:Teacher{name: $name}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        print(f'Nome: {name} \nAno de Nascimento: {results[0]["ano_nasc"]} \nCPF: {results[0]["cpf"]}')
    
    def getNameFirstLetter(self, letter):
        query = "MATCH (t:Teacher) WHERE t.name =~ $letter RETURN t.name AS name, t.cpf AS cpf"
        parameters = {"letter": f"^{letter}.*"}
        results = self.db.execute_query(query, parameters)
        print(f"Dados dos professores onde a primeira letra do seu nome é {letter}:")
        for result in results:
            print("-------------------")
            nome = result["name"]
            cpf = result["cpf"]
            print(f" - Nome: {nome}")
            print(f" - CPF: {cpf}")

    def allCities(self):
        query = "MATCH (c:City) RETURN c.name AS name"
        results = self.db.execute_query(query)
        print("Nome de todas as cidades: ")
        for result in results:
            nome = result["name"]
            print(f" - {nome}")
    
    def schoolNumber(self, maior, menor):
        query = "MATCH (s:School) WHERE s.number >= $maior AND s.number < $menor RETURN s.name AS name, s.address AS address, s.number AS number"
        parameters = {"maior": maior, "menor": menor}
        results = self.db.execute_query(query, parameters)
        for result in results:
            nome = result["name"]
            address = result["address"]
            number = result["number"]
            print(f"Nome: {nome}")
            print(f"Address: {address}")
            print(f"Number: {number}")
            print("-------------------")
        
    def teacherYear(self):
        query = "MATCH (t:Teacher) RETURN MIN(t.ano_nasc) AS maisVelho, MAX(t.ano_nasc) AS maisJovem"
        results = self.db.execute_query(query)
        print(f'Ano de nascimento do professor mais jovem - {results[0]["maisJovem"]} e do mais velho - {results[0]["maisVelho"]}')

    def avgPopulation(self):
        query = "MATCH (c:City) RETURN AVG(c.population) AS mediaPopulacao"
        results = self.db.execute_query(query)
        print(f'Media aritmética da população: {results[0]["mediaPopulacao"]}')
    
    def cep(self, cep):
        query = "MATCH (c:City{cep: $cep}) RETURN REPLACE(c.name, 'a', 'A') AS cityName"
        parameters = {"cep": cep}
        results = self.db.execute_query(query, parameters)
        print(f'Nome da cidade com o CEP - {cep}: {results[0]["cityName"]}')
    
    def caracter(self):
        query = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 3, 1) AS caracter"
        results = self.db.execute_query(query)
        print([result["caracter"] for result in results])

        

db = Database("bolt://3.236.36.178:7687", "neo4j", "sea-vibration-wines")
query = Querys(db)

## Questão 01
# 1. Busque pelo professor `“Teacher”` cujo nome seja **“Renzo”**, retorne o **ano_nasc** e o **CPF**.
query.getTeacher("Renzo")
print("----------------------------------------------\n")

# 2. Busque pelos professores `“Teacher”` cujo nome comece com a letra **“M”**, retorne o **name** e o **cpf**.
query.getNameFirstLetter("M")
print("----------------------------------------------\n")

# 3. Busque pelos nomes de todas as cidades `“City”` e retorne-os.
query.allCities()
print("----------------------------------------------\n")

# 4. Busque pelas escolas `“School”`, onde o number seja maior ou igual a 150 e menor ou igual a 550, retorne o nome da escola, o endereço e o número.
query.schoolNumber(150, 550)
print("----------------------------------------------\n")


## Questão 02
# 1. Encontre o ano de nascimento do professor mais jovem e do professor mais velho.
query.teacherYear()
print("----------------------------------------------\n")

# 2. Encontre a média aritmética para os habitantes de todas as cidades, use a propriedade **“population”**.
query.avgPopulation()
print("----------------------------------------------\n")

# 3. Encontre a cidade cujo **CEP** seja igual a **“37540-000”** e retorne o nome com todas as letras **“a”** substituídas por **“A”** .
query.cep("37540-000")
print("----------------------------------------------\n")

# 4. Para todos os professores, retorne um caractere, iniciando a partir da 3ª letra do nome.
query.caracter()
print("----------------------------------------------\n")

