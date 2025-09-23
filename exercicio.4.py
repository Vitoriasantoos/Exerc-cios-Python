from dataclasses import dataclass
from datetime import datetime

# Definição da estrutura de dados para representar uma publicação

# Utiliza dataclass para facilitar a criação e manipulação dos objetos

@dataclass
class Publicacao:
conteudo: str
descricao: str
autor: str
data_hora: datetime
curtidas: int = 0

# Lista global que armazenará todas as publicações criadas

lista_publicacoes = []

# Função para criar uma nova publicação

# O usuário fornece conteúdo, descrição e nome do autor

# A data/hora é definida automaticamente como o momento atual

def criar_publicacao():
print(”\n=== CRIAR PUBLICAÇÃO===”)
conteudo = input(“Digite o conteúdo da publicação: “)
descricao = input(“Digite a descrição:”)
autor = input(“Digite o nome do autor: “)
data_hora = datetime.now()


nova_publicacao = Publicacao(conteudo, descricao, autor, data_hora)
lista_publicacoes.append(nova_publicacao)
print("Publicação criada com sucesso!")


# Função para incrementar o contador de curtidas de uma publicação

# Verifica se existem publicações disponíveis antes de permitir curtir

# O usuário seleciona a publicação pelo número no feed

def curtir_publicacao():
print(”\n=== CURTIR PUBLICAÇÃO ===”)
if not lista_publicacoes:
print(“Nenhuma publicação disponível.”)
return


visualizar_feed()
try:
    indice = int(input("Digite o número da publicação para curtir: ")) - 1
    # Valida se o índice está dentro do range válido da lista
    if 0 <= indice < len(lista_publicacoes):
        lista_publicacoes[indice].curtidas += 1
        print("Publicação curtida!")
    else:
        print("Publicação não encontrada.")
except ValueError:
    print("Número inválido.")


# Função para exibir todas as publicações disponíveis no feed

# Mostra um resumo com autor, curtidas, parte do conteúdo e data

def visualizar_feed():
print(”\n=== FEED ===”)
if not lista_publicacoes:
print(“Nenhuma publicação disponível.”)
return


# Enumera as publicações começando do 1 para facilitar a seleção pelo usuário
for i, pub in enumerate(lista_publicacoes, 1):
    print(f"{i}. {pub.autor} - {pub.curtidas} curtidas")
    print(f"   {pub.conteudo[:50]}...")  # Mostra apenas os primeiros 50 caracteres
    print(f"   {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
    print("-" * 40)


# Função para visualizar os detalhes completos de uma publicação específica

# Exibe todas as informações: autor, data, conteúdo completo, descrição e curtidas

def visualizar_publicacao_individual():
print(”\n=== VISUALIZAR PUBLICAÇÃO ===”)
if not lista_publicacoes:
print(“Nenhuma publicação disponível.”)
return


visualizar_feed()
try:
    indice = int(input("Digite o número da publicação: ")) - 1
    if 0 <= indice < len(lista_publicacoes):
        pub = lista_publicacoes[indice]
        print(f"\nAutor: {pub.autor}")
        print(f"Data: {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
        print(f"Conteúdo: {pub.conteudo}")
        print(f"Descrição: {pub.descricao}")
        print(f"Curtidas: {pub.curtidas}")
    else:
        print("Publicação não encontrada.")
except ValueError:
    print("Número inválido.")


# Função para filtrar e exibir publicações de um autor específico

# Utiliza list comprehension para filtrar publicações por nome do autor

# A comparação é case-insensitive (não diferencia maiúsculas de minúsculas)

def visualizar_publicacoes_por_autor():
print(”\n=== PUBLICAÇÕES POR AUTOR ===”)
if not lista_publicacoes:
print(“Nenhuma publicação disponível.”)
return


autor = input("Digite o nome do autor: ")
publicacoes_autor = [pub for pub in lista_publicacoes if pub.autor.lower() == autor.lower()]
        
if not publicacoes_autor:
    print(f"Nenhuma publicação encontrada para {autor}.")
    return
        
print(f"\nPublicações de {autor}:")
for pub in publicacoes_autor:
    print(f"- {pub.conteudo[:50]}... ({pub.curtidas} curtidas)")
    print(f" {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
    print("-" * 30)


# Função principal que controla o fluxo do programa

# Apresenta um menu interativo com todas as funcionalidades disponíveis

# Executa em loop até o usuário escolher sair (opção 0)

def menu():
while True:
print(”\n=== REDE SOCIAL ===”)
print(“1. Criar Publicação”)
print(“2. Curtir Publicação”)
print(“3. Visualizar Feed”)
print(“4. Visualizar Publicação Individual”)
print(“5. Visualizar Publicações por Autor”)
print(“0. Sair”)
opcao = input(“escolha uma opção: “)


    if opcao == "1":
        criar_publicacao()
    elif opcao == "2":
        curtir_publicacao()
    elif opcao == "3":
        visualizar_feed()
    elif opcao == "4":
        visualizar_publicacao_individual()
    elif opcao == "5":
        visualizar_publicacoes_por_autor()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")


# Inicia a execução do programa

menu()