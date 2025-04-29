print("Operações suportadas")
print("1 -> '+' ")
print("2 -> '-' ")
print("3 -> '/' ")
print("4 -> '*' ")
print("5 -> '**' ")

num1= float(input("Informe o primeiro número:"))

operacao = int(input("Informe o tipo de operação:"))

num2 = float(input("Informe o segundo número:"))


if (operacao == 1):
    print(f"O resultado é : {num1 + num2}")
elif (operacao == 2):
    print(f"O resultado é : {num1 - num2}")
elif (operacao == 3):
    print(f"O resultado é : {num1 / num2}")
elif (operacao == 4):
    print(f"O resultado é : {num1 * num2}")
elif (operacao == 5):
    print(f"O resultado é : {num1 ** num2}")
else:
    print("Operação não suportada")