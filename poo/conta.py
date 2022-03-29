class Conta:
    def __init__(self, numero, titular, saldo, limite=1000, historico=None):  # função construtora
        """

        :type   numero, saldo, limite: int
                titular: str
        """
        print(f"Construindo objeto... {self}")
        self.__numero = numero  # dois underscore irá privar meu parâmetro
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__historico = historico

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def titular(self):
        return self.__titular

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite
        return print("Limite alterado!")

    @property
    def historico_cliente(self):
        return self.__historico


    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    # @historico_cliente.setter
    # def

    def extrato(self):
        print("O saldo da conta do(a) {} é: {} reais".format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__pode_sacar(valor):
                self.__saldo -= valor
        else:
            print("Esta operação não pode ser feita, saldo e limite insuficiente.")

    @staticmethod
    def codigo_banco():
        return "001"

    # def sacar2(self, valor):
    #     if valor > self.__saldo:
    #         if valor <= (self.__saldo + self.__limite):
    #             self.__saldo = 0
    #             limite_excedente = valor - self.__saldo
    #             self.__limite = self.__limite - limite_excedente #erro:  conta1 = Conta(147,"Gustavo", 100, 200); conta1.sacar2(299), salod =  0  mas limite -99
    #
    #         else:
    #             print("Esta operação não pode ser feita, saldo e limite insuficiente.")
    #             pass
    #     else:
    #         self.saldo -= valor

    def information(self):
        return print(
            f"Numero da conta: {self.__numero}\nTitular: {self.__titular}\nSaldo: {self.__saldo}\nLimite: {self.__limite}")

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        return print("Transferência concluída!")


if __name__ == '__main__':
    conta1 = Conta(7747, "Mario", 100)
    conta2 = Conta(1154, "Gustavo", 50)
    # conta.information(conta)
    # conta.extrato()
    # print('saldo:',conta._Conta__saldo)
    # conta._Conta__saldo = 500
    # print('saldo alterado',conta._Conta__saldo)
    # conta1.transferir(10, conta2)
    # conta2.extrato()

"""
Falamos nessa aula sobre a coesão que é ligado ao principio de responsabilidade única. Aprendemos que uma classe deve ter 
apenas uma responsabilidade (ou deve ter apenas uma razão para existir). Em outras palavras, ela não deve assumir responsabilidades 
que não são delas.

Além desse princípio de responsabilidade única existem outras que foram definidos através do Robert C. Martin no início dos anos 2000 
e são conhecidos pelo acrônimo SOLID:

S - Single responsibility principle
O - Open/closed principle
L - Liskov substitution principle
I - Interface segregation principle
D - Dependency inversion principle

Na Alura temos cursos específicos sobre o SOLID, mas fique tranquilo, na medida que você avança no mundo OO esses princípios 
ficam mais claros e fáceis de se entender.
"""
