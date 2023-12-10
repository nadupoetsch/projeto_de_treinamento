usuarios = {}  # Cria um dicionário vazio para armazenar informações de usuários
emails = ["xpot@xyz.com", "xkcd@phd.com"]  # Cria uma lista de emails

# Converte a lista de emails em uma lista de tuplas numeradas
# Usando a função enumerate para criar uma lista de tuplas em que o primeiro elemento da tupla é o índice da lista de emails e o segundo elemento é o próprio email.
tupla = list(enumerate(emails))

print(tupla)  # Exibe a lista de tuplas numeradas

# Loop for para preencher o dicionário com informações dos usuários
for chave in range(0, len(tupla)):
    print("Email: ", tupla[chave][1])  # Exibe o email atual
    usuarios[tupla[chave]] = [input("Digite o nome "), input("Digite o nível ")]  # Adiciona informações do usuário ao dicionário

# Loop for para exibir as informações de todos os usuários armazenados no dicionário
for chave, dado in usuarios.items():
    print("Usuário: ", chave[0])  # Exibe o índice da lista de emails, que é o mesmo que o índice original da tupla
    print("Email: ", chave[1])  # Exibe o email do usuário
    print("Nome: ", dado[0])  # Exibe o nome do usuário armazenado no dicionário
    print("Nível: ", dado[1])  # Exibe o nível do usuário armazenado no dicionário
