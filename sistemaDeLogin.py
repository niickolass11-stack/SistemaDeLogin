import random

dictCadastroDeUsuario: dict = {}

digitosParaSenhaAleatoria = ["a","b","c","d","e","1","2","3","4","5"]


def senhaAleatoria():
    
    senhaGerada = ""

    for senha in range(6):

        novaSenha = random.choice(digitosParaSenhaAleatoria)

        senhaGerada = senhaGerada + novaSenha
    
    return senhaGerada




    



def CadastroUsuarios():
    
    novoUsuario = str(input("Informe um nome de usuario: "))
    
    senhaUsuario = senhaAleatoria()
    print(f"Sua senha e {senhaUsuario}")
    dictCadastroDeUsuario[novoUsuario] = senhaUsuario
    print("Usuario Cadastrado com sucesso.")

def RemoverUsuarios():
    
    
    remover = str(input("Informe o usuario a ser removido: "))

    
    del dictCadastroDeUsuario[remover]
    print("Cadastro deletado do sistema.")

def Logar():

    contador: int = 3
    while contador >= 0:

        usuario = str(input("Informe o nome de usuario: "))
        senha = str(input("Informe a senha cadastrada: "))

        if (usuario, senha) in dictCadastroDeUsuario.items():

            print("Login realizado !")
            break
        
        elif (usuario, senha) not in dictCadastroDeUsuario.items() and contador > 0:
            print("Usuario ou senha incorretos")
            print("Tente novamente")
        
        else:
            
            print("Tentativas excedidas")
            print("Redirecionando a página inicial...")
    
        contador = contador - 1


def VerUsuariosCadastrados():

    for nome,senha in dictCadastroDeUsuario.items():

        print(f"Usuario: {nome} Senha: {senha}")


def Menu():
    
    print("--- SISTEMA DE LOGIN ---")

    while True:

        opcao = str(input('''Selecione uma opção\n
                            A - Cadastrar Usuario\n
                            B - Ver Usuarios\n
                            C - Remover usuario\n
                            D - Logar\n
                            X - Sair\n
                            --> ''')).upper()
        
        match opcao:

            case "A":
                
                CadastroUsuarios()
            
            case "B":
                
                VerUsuariosCadastrados()
            
            case "C":
                
                RemoverUsuarios()
            
            case "D":
                
                Logar()

            case "X":
                
                print("ENCERRANDO...")
                break

            case _:

                print("Opção Inválida.")
                
Menu()

