class Funcionario:
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


class Junior (Alura):
    pass

class Pleno (Alura, Caelum):
    pass

kleber = Junior()
kleber.busca_perguntas_sem_resposta()

karlee  = Pleno()
karlee.busca_perguntas_sem_resposta()
karlee.busca_cursos_do_mes()


## filha > mãe 1 > vó 1 > mãe 2 > vó 2 > [...]   se (vó 1 = vó 2)  { filha > mãe 1 > mãe 2 > vó 2 }