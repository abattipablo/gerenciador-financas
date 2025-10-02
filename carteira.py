class Carteira:
    def __init__(self):
        self.saldo = 0.0

    def adicionar_receita(self, valor: float):
        self.saldo += valor
        print(f"Receita de R${valor:.2f} adicionada com sucesso!")

    def adicionar_despesa(self, valor: float):
        self.saldo -= valor
        print(f"Despesa de R${valor:.2f} registrada com sucesso!")

    def ver_saldo(self):
        print(f"O seu saldo atual é: R${self.saldo:.2f}")
