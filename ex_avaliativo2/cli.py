class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            print("---------------- MENU DE OPÇÕES ----------------")
            print("1 - Criar um professor")
            print("2 - Ler dados de um professor")
            print("3 - Deletar um professor")
            print("4 - Atualizar CPF de um professor")
            print("5 - Sair")
            print("------------------------------------------------")
            command = input("O que você gostaria de fazer? ")
            print("------------------------------------------------")
            if command == "5":
                print("Até mais!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando invalido! Tente novamente.")


class TeacherCLI(SimpleCLI):
    def __init__(self, teacherCRUD):
        super().__init__()
        self.teacherCRUD = teacherCRUD
        self.add_command("1", self.create)
        self.add_command("2", self.read)
        self.add_command("3", self.delete)
        self.add_command("4", self.update)

    def create(self):
        nome = input("Nome do professor: ")
        anoNasc = input("Ano de Nascimento: ")
        cpf = input("CPF: ")
        self.teacherCRUD.create(nome, anoNasc, cpf)

    def read(self):
        nome = input("Nome do professor: ")
        results = self.teacherCRUD.read(nome)
        if results:
            ano_nasc = results[0]["ano_nasc"]
            cpf = results[0]["cpf"]
            print(f"Ano de Nascimento: {ano_nasc}")
            print(f"CPF: {cpf}")
        else:
            print("Professor não encontrado!")

    def delete(self):
        nome = input("Nome do professor: ")
        self.teacherCRUD.delete(nome)
    
    def update(self):
        nome = input("Nome do professor: ")
        cpf = input("Novo CPF: ")
        self.teacherCRUD.update(nome, cpf)

        
    def run(self):
        print("Bem vindo!")
        super().run()
