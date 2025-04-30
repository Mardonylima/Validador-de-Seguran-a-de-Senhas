from src.models.validacao import Validacao

def main():
    validacao = Validacao()

    while True:
        print("\nMENU:")
        print("1. Validar critérios da senha")
        print("2. Classificar força da senha")
        print("3. Gerar senha segura")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            senha = input("Digite uma senha: ")
            resultados = validacao.validar_criterios(senha)
            print("Critérios atendidos:")
            for criterio, atendido in resultados.items():
                print(f"- {criterio}: {'✔️' if atendido else '❌'}")

        elif opcao == "2":
            senha = input("Digite a senha: ")
            print("Força da senha:", validacao.classificar_forca(senha))

        elif opcao == "3":
            senha_segura = validacao.gerar_senha_segura()
            print(f'Senha gerada conforme os padrão de segurança:{senha_segura}')

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
