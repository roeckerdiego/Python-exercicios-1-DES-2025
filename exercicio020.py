#Simule um login com nome de usuário "admin" e senha "1234".
#Caso os dados estejam corretos, exiba "Acesso concedido", senão "Acesso negado".

usuario = input("Digite o usuario")
senha = input("Digite a senha.")

if usuario == ("admin") and ("1234"):
    print("Acesso concedido")
else:
    print("Acesso negado")
    #finalizado