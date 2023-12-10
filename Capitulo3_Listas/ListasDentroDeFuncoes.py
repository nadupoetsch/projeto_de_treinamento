palavras_chave_sim = ["SIM", "S"]
inventario=[]
resposta = "S"
while resposta == "S":
  equipamento=[input("Equipamento: "),
            float(input("Valor: ")),
            int(input("Número Serial: ")),
            input("Departamento: ")]
  inventario.append(equipamento)
  resposta = input("Digite \"S\" para continuar: ").upper()
  if resposta in palavras_chave_sim:
    print("cadastrado com sucesso!")
    print("cadastre um novo item:")
  else:
    break

for elemento in inventario:
  print("Nome.........: ", elemento[0])
  print("Valor........: ", elemento[1])
  print("Serial.......: ", elemento[2])
  print("Departamento.: ", elemento[3])

# localizar um item no inventario
busca=input("Digite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
  if busca==elemento[0]:
    print("Valor..: ", elemento[1])
    print("Serial.:", elemento[2])

# Depreciação
depreciacao=input("Digite o nome do equipamento que será depreciado: ")
for elemento in inventario:
  if depreciacao==elemento[0]:
    print("Valor antigo: ", elemento[1])
    elemento[1] = elemento[1] * 0.9
    print("Novo valor: ", elemento[1])

# Excluír itens
excluir = input("Deseja excluir algum item pelo serial? Digite 'sim' ou 'nao': ")

while excluir.lower() == "sim":
  serial = int(input("Digite o serial do equipamento que será excluído: "))
  for elemento in inventario:
    if elemento[2] == serial:
      inventario.remove(elemento)
      print(f"O equipamento {elemento[0]} foi excluído com sucesso!")
      break
  else:
    print("Equipamento não encontrado. Tente novamente.")

  excluir = input("Deseja excluir mais algum item pelo serial? Digite 'sim' ou 'nao': ")

for elemento in inventario:
  print("Nome.........: ", elemento[0])
  print("Valor........: ", elemento[1])
  print("Serial.......: ", elemento[2])
  print("Departamento.: ", elemento[3])

valores = []
for elemento in inventario:
  valores.append(elemento[1])
if len(valores) > 0:
  print("O equipamento mais caro custa: ", max(valores))
  print("O equipamento mais barato custa: ", min(valores))
  print("O total de equipamentos é de: ", sum(valores))






