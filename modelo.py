class Programa:                       ## Mãe
    def __init__(self, nome, ano):
        self._nome = nome.title()     ## Protegido
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes
    
    def darLike(self):
        self.likes +=1


class Filme(Programa): ## Declaração de filho
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) ## 'super()' chama a classe mãe
        self.duracao = duracao
        

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temopradas = temporadas


vingadores = Filme('vingadores', 2019, 160)

got = Serie('Game of Thrones', 2011, 8)


print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Temporadas: {vingadores.duracao} - Likes: {vingadores.likes}')

print(f'Nome: {got.nome} - Ano: {got.ano} - Temporadas: {got.temopradas} - Likes: {got.likes}')