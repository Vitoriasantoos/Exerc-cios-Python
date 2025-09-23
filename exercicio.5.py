# Lista para guardar os agendamentos
agendamentos = []

def agendar():
    print("Barbearia TH, Seja bem vindo!")
    nome = input("qual é o seu nome?(usuário...): ") 
    celular = input("qual é o seu numero?(13 99999999): ")
    horario = input("qual horario voce quer agendar?(ex: 13:30): ")
    email = input("qual é o seu gmail?(usuario@gmail.com): ")
    data = input("qual dia voce quer agendar?(ex: 17/08): ")
    
    # Mostra os serviços
    servicos()
    servico = input("escolha o serviço (digite 1, 2, 3 ou 4): ")
    if servico == "1":
        servico_nome = "corte + barba (R$35)"
    elif servico == "2":
        servico_nome = "barba completa (R$20)"
    elif servico == "3":
        servico_nome = "corte simples (R$25)"
    elif servico == "4":
        servico_nome = "corte social (R$30)"
    else:
        servico_nome = "serviço inválido"
    
    # Guarda o agendamento
    agendamento = {
        "nome": nome,
        "celular": celular,
        "email": email,
        "data": data,
        "horario": horario,
        "servico": servico_nome
    }
    agendamentos.append(agendamento)
    print("agendamento salvo!")

def servicos():
    print("corte + barba (R$35)")
    print("barba completa (R$20)")
    print("corte simples (R$25)")
    print("corte social (R$30)")

def ver_agendamentos():
    if  agendamentos:  
        print("Nenhum agendamento.")
    else:
            print("agendamento")
            print(f"Nome")
            print(f"Celular")
            print(f"Email")
            print(f"Data")
            print(f"Horario")
            print(f"Serviço")

def menu():
    while True:
        print("\n=== Barbearia TH ===")
        print("1. Agendar")
        print("2. Ver agendamentos")
        print("0. Sair")
        opcao = input("Escolha: ")
        
        if opcao == "0":
            print("Tchau!")
            break
        elif opcao == "1":
            agendar()
        elif opcao == "2":
            ver_agendamentos()
        else:
            print("Opção inválida!")

print(" Barbearia TH - Iniciando...")
menu()