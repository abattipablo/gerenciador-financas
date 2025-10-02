from carteira import Carteira

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
                    carteira.adicionar_receita(valor)
                except ValueError:
                    print("Digite um valor numérico válido.")
            case 2:
                try:
                    valor = float(input("Qual o valor da despesa? "))
                    carteira.adicionar_despesa(valor)
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
