class Carteira:
    def __init__(self):
        self.saldo = 0.0
        self.categorias_receita = {
            "Salario": 0,
            "Bonus": 0,
            "Freelance": 0,
            "Renda_extra": 0,
            "Investimentos": 0,
            "Outros": 0
        }
        self.categorias_despesa = {
            "Moradia": 0,
            "Alimentacao": 0,
            "Transporte": 0,
            "Saude": 0,
            "Lazer": 0,
            "Investimentos": 0,
            "Outros": 0
        }

    def adicionar_receita(self, valor: float, categoria: str):
        self.saldo += valor
        if categoria not in self.categorias_receita:
            self.categorias_receita[categoria] = 0
        self.categorias_receita[categoria] += valor
        print(f"Receita de R${valor:.2f} adicionada na categoria '{categoria}'.")

    def adicionar_despesa(self, valor: float, categoria: str):
        self.saldo -= valor
        if categoria not in self.categorias_despesa:
            self.categorias_despesa[categoria] = 0
        self.categorias_despesa[categoria] += valor
        print(f"Despesa de R${valor:.2f} registrada na categoria '{categoria}'.")

    def ver_saldo(self):
        print(f"\nSaldo atual: R${self.saldo:.2f}")
        print("Receitas por categoria:")
        for cat, val in self.categorias_receita.items():
            print(f"  {cat}: R${val:.2f}")
        print("Despesas por categoria:")
        for cat, val in self.categorias_despesa.items():
            print(f"  {cat}: R${val:.2f}")
