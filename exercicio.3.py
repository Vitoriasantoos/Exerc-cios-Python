#Criar Usuário com nome, email e senha;
#Pesquisar e-mail e achar o nome;
#Fazer login

from dataclasses import dataclass

@dataclass
class Usuario:
    nome: str
    email: str
    senha: str

lista = []

def criar_usuario():
    nome = input("Qual o seu nome: ")
    email = input("Qual o seu email: ")
    senha = input("Qual a sua senha: ")
    usuario_digitado = Usuario(nome,email,senha)
    lista.append(usuario_digitado)
    print("Cadastro efetuado com sucesso")

def pesquisar_email():
    nome_digitado = input("Qual o seu nome: ")
    for usuario in lista:
        if usuario.nome == nome_digitado:
            print(f"email desse usuario -> {usuario.email}")
            
def fazer_login():
    login_email = input("Qual o seu email: ")
    login_senha = input("Qual a sua senha: ")
        
    for usuario in lista:
        if usuario.email == login_email:
            if usuario.senha == login_senha:
                print("Acesso autorizado")
            else:
                print("Email ou senha incorreto")
        else:
            print("Email ou senha incorreto")
def menu():
    print("1- Cadastro")
    print("2- Login")
    print("3- Buscar usuario com email")
    print("4- Sair")
    return input("\nDigite a opção: ")


while True:
    opcao = menu()
    if opcao == "1":
        criar_usuario()
    
    elif opcao == "2":
        fazer_login()
        
    elif opcao == "3":
        pesquisar_email()
        
    elif opcao == "4":
        break