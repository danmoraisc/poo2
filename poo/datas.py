class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        return print(f"{self.dia:02d}/{self.mes:02d}/{self.ano}")


if __name__ == '__main__':
    d = Data(16,8,1995)
    print(d.formatada())