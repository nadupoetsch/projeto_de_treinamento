# arquivo = open("primeiro_arquivo.txt", "w")
#
# arquivo.write("Meu primeiro arquivo! Ai que festa!")
#
# arquivo.close()

# AULA 1: gravar arquivo
# with open("primeiro_arquivo.txt", "a") as arquivo: ## "w" = novo arquivo, "a" = continua escrevendo da onde parou
#     arquivo.write("\nHakuna Matata!")

# AULA 2: lendo o arquivo
with open("primeiro_arquivo.txt", "r") as arquivo: ## "r" = ler o arquivo
    for linha in arquivo.readlines():
        print(linha)

