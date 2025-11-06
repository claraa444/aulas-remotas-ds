numero_str = input("Digite um número para ver sua tabuada.")
numero = int(numero_str)
print(f"Tabuada do {numero}:")
  for i in range(1,11):
    resultado = numero * i 
    print(f"{numero} X {i} = {resultado}")

