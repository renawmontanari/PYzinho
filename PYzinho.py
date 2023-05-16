dados = []
id_atual = 1

def cadastrar():
    novo_dado = input("Digite o novo dado: ")
    dados.append({"id": id_atual, "dado": novo_dado})
    print(f"{novo_dado} cadastrado com sucesso!")
    id_atual += 1

def listar():
    for dado in dados:
        print(dado)

def buscar_por_id(id):
    for dado in dados:
        if dado["id"] == id:
            return dado
    return None

def alterar():
    id = int(input("Digite o ID do dado a ser alterado: "))
    novo_dado = input("Digite o novo dado: ")
    dado_encontrado = buscar_por_id(id)
    if dado_encontrado:
        dado_encontrado["dado"] = novo_dado
        print(f"Dado com ID {id} alterado para {novo_dado}!")
    else:
        print(f"Dado com ID {id} não encontrado!")

def excluir():
    id = int(input("Digite o ID do dado a ser excluído: "))
    dado_encontrado = buscar_por_id(id)
    if dado_encontrado:
        dados.remove(dado_encontrado)
        print(f"Dado com ID {id} removido com sucesso!")
    else:
        print(f"Dado com ID {id} não encontrado!")

def menu():
    while True:
        print("=== Menu ===")
        print("1. Cadastrar novo dado")
        print("2. Listar dados")
        print("3. Alterar dado")
        print("4. Excluir dado")
        print("0. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            alterar()
        elif opcao == "4":
            excluir()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()