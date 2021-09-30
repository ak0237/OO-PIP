class Funcionario:
    def __init__(self, nome):
        self.nome = nome
    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


class Hipster:  ## Mixin
    def __str__(self):
        return f'Hipster, {self.nome}'
        

class Junior (Alura):
    pass

class Pleno (Alura, Caelum):
    pass

class Senior (Alura, Caelum, Hipster):
    pass


kleber = Junior('kleber')
kleber.busca_perguntas_sem_resposta()

karlee  = Pleno('karlee')
karlee.busca_perguntas_sem_resposta()
karlee.busca_cursos_do_mes()

epofasio = Senior('epofasio')
print(epofasio)


## filha > mãe 1 > vó 1 > mãe 2 > vó 2 > [...]   se (vó 1 = vó 2)  { filha > mãe 1 > mãe 2 > vó 2 }