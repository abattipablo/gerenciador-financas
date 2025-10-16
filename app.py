from carteira import Carteira

def escolher_categoria(categorias: list, tipo: str) -> str:
    print(f"\nCategorias de {tipo}:")
    for i, cat in enumerate(categorias, start=1):
        print(f"{i} - {cat}")
    print(f"{len(categorias)+1} - Outra categoria")

    while True:
        try:
            escolha = int(input("Escolha uma categoria: "))
            if 1 <= escolha <= len(categorias):
                return categorias[escolha-1]
            elif escolha == len(categorias)+1:
                nova = input("Digite o nome da nova categoria: ").strip().lower()
                return nova
            else:
                print("Escolha inválida, tente novamente.")
        except ValueError:
            print("Digite um número válido.")

def menu():
    carteira = Carteira()

    while True:
        print("\n===== MENU =====")
        print("1 - Adicionar receita")
        print("2 - Adicionar despesa")
        print("3 - Ver saldo")
        print("4 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite um número válido!\n")
            continue

        match opcao:
            case 1:
                try:
                    valor = float(input("Qual o valor da receita? "))
                    categoria = escolher_categoria(list(carteira.categorias_receita.keys()), "receita")
                    carteira.adicionar_receita(valor, categoria)
                except ValueError:
                    print("Digite um valor numérico válido.")
            case 2:
                try:
                    valor = float(input("Qual o valor da despesa? "))
                    categoria = escolher_categoria(list(carteira.categorias_despesa.keys()), "despesa")
                    carteira.adicionar_despesa(valor, categoria)
                except ValueError:
                    print("Digite um valor numérico válido.")
            case 3:
                carteira.ver_saldo()
            case 4:
                print("Saindo do programa. Até logo!")
                break
            case _:
                print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
