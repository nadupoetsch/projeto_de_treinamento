inventario=[]
resposta="S"
while resposta=="S":
  inventario.append(input("Equipamento: "))
  inventario.append(float(input("Valor: ")))
  inventario.append(int(input("Número Serial: ")))
  inventario.append(input("Departamento: "))
  resposta=input("Digite \"S\" para continuar: ").upper()
  if resposta == "S":
    print("cadastrado com sucesso!")
    print("cadastre um novo item:")
  else:
    break