# Isabela está desenvolvendo um aplicativo de corrida que calcula a velocidade média do usuário.
# O programa deve receber a distância percorrida e o tempo gasto, calcular a velocidade e indicar se foi 
# lenta (<5 km/h), moderada (5 a 10 km/h) ou rápida (>10 km/h).

distancia = int(input("Digite a distancia"))
tempo = int(input("Digite o tempo"))
media = distancia / tempo
if media <5:
    print("Lento")
elif media >=5 and 10:
    print("Moderado")
else:
    print("Rapido")
    #finalizado