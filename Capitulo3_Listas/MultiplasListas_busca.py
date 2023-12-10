palavras_chave_sim = ["SIM", "S"]
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta in palavras_chave_sim:
    equipamentos.append(input("Equipamento: ").lower())
    valores.append(float(input("Valor: ").replace(',', '.')))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: ").lower())
    resposta = input("Digite \"S\" para continuar: ").upper()
    if resposta in palavras_chave_sim:
        print("cadastrado com sucesso!")
        print("cadastre um novo item:")
    else:
        break

busca = ""
while busca != "sair":
    busca = input("Digite o nome do equipamento que deseja buscar (ou 'SAIR' para sair): ").lower()
    if busca in equipamentos:
        indice = equipamentos.index(busca)
        print("Valor..: R$ {:.2f}".format(valores[indice]))
        print("Serial.:", seriais[indice])
    elif busca == "sair":
        break
    else:
        print("Equipamento não encontrado. Tente novamente.")
