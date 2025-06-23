# Uma empresa quer avaliar seus colaboradores com base em três metas atingidas.
# O programa deve calcular a média das três avaliações e exibir:

# Aprovado (>=7)
# Em treinamento (>=5 e <7)
# Reprovado (<5)


media1 = float(input("Digite a primeira media: "))
media2 = float(input("Digite a segunda media: "))
media3 = float(input("Digite a segunda media: "))

soma = media1 + media2 + media3

media = soma / 3

if media >=7:
    print("Aprovado")
elif media >=5:
    print("Recuperação")
else:
    print("Reprovado") 
    #finalizado