class Professor:
    def __init__(self, nome): #Método especial - CONSTRUTOR
        self.nome = nome
    def ministrar_aula(self, assunto):
        return f'O professor {self.nome} está ministrando uma aula sobre {assunto}'


class Aluno:
    def __init__(self, nome):
        self.nome = nome
    def presenca(self):
        return f'O aluno {self.nome} está presente'


class Aula:
    def __init__(self, professor, assunto, alunos=None):
        self.Professor = professor
        self.assunto = assunto
        self.alunos = alunos if alunos is not None else [] #caso não seja adicionado nenhum aluno ao inicializar a classe, ele apenas criará uma lista chamada alunos
    def adicionar_aluno(self, Aluno):
        self.alunos.append(Aluno.nome)
    def lista_presenca(self):
        return f'Presença na aula sobre {self.assunto}, ministrado pelo professor {self.Professor.nome}: \n {self.alunos}'

'''
professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
#aula = Aula(professor, "Programação Orientada a Objetos", ["Jõao"])
aula = Aula(professor, "Programação Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
print(aula.lista_presenca())
print(professor.ministrar_aula(aula.assunto))'''