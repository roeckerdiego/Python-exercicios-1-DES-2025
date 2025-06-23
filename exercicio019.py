#Peça três números e exiba-os em ordem crescente.

n1 = float(input("digite o primeiro numero."))
n2 = float(input("Digite o segundo numero."))
n3 = float(input("Digite o terceiro numero."))

numeros = [n1, n2, n3]
numeros.sort()

print("Numeros em ordens crescentes:")
for numero in numeros:
    print(numero)