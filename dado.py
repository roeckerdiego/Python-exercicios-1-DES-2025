import random

input("Precione o enter para lançar o dado")

resultado = random.randint(1 , 6) 

print (f" O dado rolou : {resultado}" );

if resultado == 6:
    print("Uau, você tirou nota maxima.")
elif resultado <=2:
    print("Você tirou nota baixa.")
else:
    print("Sua nota foi intermediaria.")