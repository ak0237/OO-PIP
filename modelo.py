class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes
    
    def darLike(self):
        self.likes +=1

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temopradas = temporadas
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.likes +=1


vingadores = Filme('vingadores', 2019, 160)

got = Serie('Game of Thrones', 2011, 8)

#print(vingadores.ano)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Temporadas: {vingadores.duracao} - Likes: {vingadores.likes}')

print(f'Nome: {got.nome} - Ano: {got.ano} - Temporadas: {got.temopradas} - Likes: {got.likes}')