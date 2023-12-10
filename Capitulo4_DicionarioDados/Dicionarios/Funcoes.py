def perguntar():
    return input("O que deseja realizar?\n" +
            "<I> - Para Inserir um usuário\n"+
            "<P> - Para Pesquisar um usuário\n"+
            "<E> - Para Excluir um usuário\n"+
            "<L> - Para Listar os usuários\n"+
            "<N> - Para Sair\n"+
            "Qual das opções você deseja?\n").upper()

def inserir(usuarios):
    usuarios[(input("Digite o login: ").upper())] = [input("Digite o nome: ").upper(),
    input("Digite a última data de acesso: "),
    input("Qual a última estação acessada: ").upper()]
    print("Dados salvos com sucesso!")
    input("Aperte Enter para continuar...")
    salvar(usuarios)

def pesquisar(usuarios):
    if not usuarios:
        print("Não é possível pesquisar um usuário devido à lista estar vazia.")
        input("Aperte Enter para continuar...")
    else:
        while True:
            login = input("Digite o login do usuário que deseja pesquisar: ").upper()
            if login in usuarios:
                print("Dados do usuário:")
                print("Login:", login)
                print("Nome:", usuarios[login][0])
                print("Última data de acesso:", usuarios[login][1])
                print("Última estação acessada:", usuarios[login][2])
            else:
                print("Usuário não encontrado.")

            opcao_pesquisa = input("Deseja pesquisar por outro usuário? (S/N): ").upper()
            if opcao_pesquisa == "N":
                break
            elif opcao_pesquisa != "S":
                print("Opção inválida.")

def excluir(usuarios):
    if not usuarios:
        print("Não é possível excluir um usuário devido à lista estar vazia.")
        input("Aperte Enter para continuar...")
    else:
        login = input("Digite o login do usuário que deseja excluir: ").upper()
        if login in usuarios:
            del usuarios[login]
            salvar(usuarios)
            print("Usuário excluído com sucesso.")
        else:
            print("Usuário não encontrado.")

def listar(usuarios):
    if not usuarios:
        print("Não é possível listar pois a Lista está vazia")
    else:
        print("Lista de usuários:")
        for login, dados in usuarios.items():
            print("Login:", login)
            print("Nome:", dados[0])
            print("Última data de acesso:", dados[1])
            print("Última estação acessada:", dados[2])
            print("------------------------")

def salvar(dicionario):
    with open("bd.txt", "w") as arquivo:
        for chave, valor in dicionario.items():
            linha = chave + ":" + ",".join(valor)
            arquivo.write(linha + "\n")
