# palavras chave
palavras_chave_sim = ["SIM", "S"]
palavras_chave_nao = ["NAO", "N", "NÃO"]
palavras_chave_mulher = ["MULHER", "FEMININO", "F"]

# CADASTRO
while True:
    nome = input("Digite o nome: ")
    if all(letra.isalpha() or letra.isspace() for letra in nome) and nome.strip():
        break
    else:
        print("Erro: O nome deve conter apenas letras. Por favor, tente novamente.")
while True:
    try:
        idade = int(input("Digite a idade: "))
        break
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")

# PRIMEIRO PROBLEMA A SER RESOLVIDO
while True:
    doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa? ").upper()
    if doenca_infectocontagiosa.upper() in palavras_chave_sim:
        print("Encaminhe o paciente para sala AMARELA")
        break
    elif doenca_infectocontagiosa.upper() in palavras_chave_nao:
        print("Encaminhe o paciente para sala BRANCA")
        break
    else:
        print("Responda com SIM ou NAO")

# SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print("Paciente COM prioridade")
else:
    if idade > 10:
        genero=input("Digite o gênero do paciente: ").upper()
        if genero in palavras_chave_mulher:
            gravidez=input("A paciente está grávida? ").upper()
        if gravidez in palavras_chave_sim:
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")