# Criar um sistema de login onde o usuario pode digitar um nome de usuario e senha
# caso o usuario exista o sistema pode recomendar um nome de usuario

listaNomeDeUsuario: list = []

def AdicionarUsuario():

    novoUsuario = str(input("Informe um nome de usuario: "))
    listaNomeDeUsuario.append(novoUsuario)
    print("Usuario Cadastrado com sucesso.")