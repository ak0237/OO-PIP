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

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.likes}'


class Filme(Programa): ## Declaração de filho
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) ## 'super()' chama a classe mãe
        self.duracao = duracao

    def __str__(self): ## "Stringa" o retorno. Quando faz print('nome da classe'), é printado tudo que for string
        return f'{self._nome} - {self.ano} - {vingadores.duracao} min - {self._likes} likes'   


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temopradas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {got.temopradas} temporadas - {self._likes} likes'


class Playlist():  ## Playlist herda as propriedades de list
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas  ## Cria uma lista com programas 

    def __getitem__(self, item):  ## Cria uma lista dentro da classe Playlist, duck typing (ñ sou, mas me comporto como)
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho (self):
        return len(self._programas)

    def __len__(self): ## Outro duck typing
        return len(self._programas)



vingadores = Filme('vingadores', 2019, 160)
got = Serie('Game of Thrones', 2011, 8)
hp = Filme('harry potter', 2001, 120)
st = Serie('stranger things', 2016, 3)


filmes_e_series = [vingadores, got, hp, st]

tedio = Playlist('tedio', filmes_e_series)

print(f'Tamanho da playlist: {len(tedio)}') 

for programa in tedio:
    print(programa)

print(f'Tá ou não tá? {got in tedio}')