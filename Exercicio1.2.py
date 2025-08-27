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
        retirar = int(input("Digite a quantidade a retirar:"))
        if retirar <= 0:
            print("A quantidade deve ser maior que zero!")
        elif retirar > quantidade:
            print("quantidade insuficiente no estoque!")
        else:
            quantidade -= retirar
           print(f"Retirado{retirar} unidade(s). Estoque atual: {Quantidade}")
                
    elif opcao == "3":
        if ingresso is None
          print("Nenhum ingresso cadastrado ainda!")
       else:
            adicionar = int(input(Digite a quantidade a adicionar"))
            if adicionar <= 0:
                print ("A quantidade deve ser maior que zero!")
            else:
                quantidade += adicionar
                print(f"Adicionado {adicionar} unidade(s). Estoque atual: {quantidade}")
                
     elif opcao == "4":
         if ingresso is None:
            print("Nenhum ingresso cadastrado ainda!")
            else:
                print(f"Ingresso: {ingresso} Quantidade em estoque:{quantidade}")
                          
                elif opcao == "4":
                    print("saindo do sistema...até mais!")
                    break
                
                else:
                    print("Opção inválida! tente novamente.")
                    
                        
        
        
        
            
