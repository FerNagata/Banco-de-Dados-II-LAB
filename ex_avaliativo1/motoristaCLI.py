from corrida import Corrida
from motorista import MotoristaDAO, Motorista
from passageiro import Passageiro
import pprint

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com um comando: ")
            print("---------------------------------------")
            if command == "sair":
                print("Até logo!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando invalido. Tente novamente.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, driver_model):
        super().__init__()
        self.driver_model = driver_model
        self.add_command("create", self.criar)
        self.add_command("read", self.ler)
        self.add_command("update", self.atualizar)
        self.add_command("delete", self.deletar)
        self.add_command("add", self.add_corrida)

    def criar(self):
        print("------------ PASSAGEIRO(A) ------------")
        nome = input("Nome: ")
        documento = input("Documento: ")
        print("--------------- CORRIDA ---------------")
        nota = int(input("Nota: "))
        distancia = float(input("Distancia: "))
        valor = float(input("Valor: "))
        print("-------------- MOTORISTA --------------")
        nota_motorista = int(input("Nota: "))

        passageiro = Passageiro(nome, documento)
        corrida = Corrida(nota, distancia, valor, passageiro)
        motorista = Motorista(corrida, nota_motorista)
        self.driver_model.criar(motorista)

    def ler(self):
        id = input("Entre com o id: ")
        motorista = self.driver_model.ler(id)
        if motorista: # caso exista um motorista ele mostrará seus elementos atraves do for 
            print(f"Motorista encontrado: ")
            for aux in motorista:
                 pprint.pprint(aux)


    def atualizar(self): # atualiza a nota do motorista
        id = input("Entre com o id: ")
        nota = int(input("Nova nota: "))
        self.driver_model.atualizar(id, nota)

    def deletar(self):
        id = input("Entre com o id: ")
        self.driver_model.deletar(id)
        
    def add_corrida(self):
        id = input("Entre com o id: ")
        print("------------ PASSAGEIRO(A) ------------")
        nome = input("Nome: ")
        documento = input("Documento: ")
        print("--------------- CORRIDA ---------------")
        nota = int(input("Nota: "))
        distancia = float(input("Distancia: "))
        valor = float(input("Valor: "))

        passageiro = Passageiro(nome, documento)
        corrida = Corrida(nota, distancia, valor, passageiro)
        self.driver_model.add_corrida(id, corrida)
        
    def run(self):
        print("------------- Bem vindos! -------------")
        print("       - Comandos disponiveis -\ncreate, read, update, delete, add, sair")
        print("---------------------------------------")
        super().run()
        