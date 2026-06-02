dictCadastroDeUsuario: dict = {}

def CadastroUsuarios():
    
    novoUsuario = str(input("Informe um nome de usuario: ")).upper()
    senhaUsuario = str(input("Informe a senha a ser cadastrada: ")).upper()
    dictCadastroDeUsuario[novoUsuario] = senhaUsuario
    print("Usuario Cadastrado com sucesso.")

def RemoverUsuarios():

    remover = str(input("Informe o usuario a ser removido: ")).upper()
    del dictCadastroDeUsuario[remover]
    print("Cadastro deletado do sistema.")

def Logar():

    contador: int = 3
    while contador >= 0:

        usuario = str(input("Informe o nome de usuario: ")).upper()
        senha = str(input("Informe a senha cadastrada: ")).upper()

        if (usuario, senha) in dictCadastroDeUsuario.items():

            print("Login realizado !")
            break
        
        elif (usuario, senha) not in dictCadastroDeUsuario.items() and contador > 0:
            print("Usuario ou senha incorretos")
            print("Tente novamente")
        
        
        else:
            
            print("-- ERROR --")
    
    contador = contador - 1


def VerUsuariosCadastrados():

    print(dictCadastroDeUsuario)


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

