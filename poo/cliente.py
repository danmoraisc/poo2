class Cliente:
    def __init__(self, nome, conta=None, saldo_negativado=None, inadimplente=None):
        self.__nome = nome
        #self.__sobrenome = sobrenome
        self.__conta = conta
        self.__saldo_negativado = saldo_negativado
        self.__inadimplente = inadimplente

    @property
    def nome(self):
        return self.__nome.title()

    # def sobrenome(self):
    #     return self.__sobrenome.title()

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

if __name__ == '__main__':
    pass
