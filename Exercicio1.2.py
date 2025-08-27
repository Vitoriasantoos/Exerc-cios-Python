def menu():
    print("\n--- Show do Filipe Ret ---")
    print(" - 2 vender ingressos")
    print(" - 3 Repor ingressos")
    print(" - 4 Ver ingressos disponiveis")
    print(" - 0 - sair")
    return input("Escolha uma opção ")
    
    
      #variaveis de controle
ingresso = None
quantidade = 0
      
while True:
    opcao = menu()
   
    if opcao == "1":
        produto = input ("ingresso")
        quantidade = 0
        print(f"ingresso '{ingresso}' cadastrado com sucesso!")
   
    elif opcao == "2":
        print("nenhum evento cadastrado ainda!")
    else:
        retirar = int(input())