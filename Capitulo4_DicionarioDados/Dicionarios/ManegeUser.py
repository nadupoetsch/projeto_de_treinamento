from Funcoes import *

usuarios = {}

# Função para carregar os dados do arquivo bd.txt para o dicionário usuarios
def carregar_dados():
    with open("bd.txt", "r") as arquivo:
        for linha in arquivo:
            chave, *valores = linha.strip().split(":")
            usuarios[chave] = [valor.strip() for valor in valores[0].split(",")]

# Carrega os dados do arquivo bd.txt (se existir)
carregar_dados()

opcao = perguntar()
while opcao != "N":
    if opcao == "I":
        inserir(usuarios)
    elif opcao == "P":
        pesquisar(usuarios)
    elif opcao == "E":
        excluir(usuarios)
    elif opcao == "L":
        listar(usuarios)
    else:
        print("Opção inválida.")

    input("Aperte Enter para continuar...")
    opcao = perguntar()