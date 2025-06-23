#Peça ao usuário uma senha e verifique se ela contém pelo menos 8 caracteres.
#Exiba uma mensagem de "Senha válida" ou "Senha muito curta".

senha = input("Digite sua senha, que contenha pelo menos 8 digitos.")

digitos = len(senha)

if senha >= 8:
    print("senha correta.")
else:
    print("senha incorreta.")
    #finalizado