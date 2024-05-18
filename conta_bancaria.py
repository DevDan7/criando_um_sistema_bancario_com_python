menu = ""

saldo = 0
extrato = ""
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    menu = int(input(" \n ****** MENU ******** \n\n [1] Deposito \n [2] Saque \n [3] Extrato \n [0] Sair \n\n --> " ))

    if menu == 1:
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\n Deposito realizado com sucesso \n")
            print("## OBRIGADO ##")
            
        else:
            print("O valor informado é inválido.\n")

             
    elif menu == 2:
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("O valor do saque excede o limite Diario.")

        elif excedeu_saques:
            print("Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\n Saque realizado com sucesso \n")
            print("## OBRIGADO ##")

        else:
            print("O valor informado é inválido.\n")

      

    elif menu == 3:
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo Atual: R$ {saldo:.2F}\n")
        print("## OBRIGADO ##")

    elif menu == 0:

        print("\n ## Operação Finalizada ## \n")
        print(" Obrigado pela Preferença  \n")
        
        break

    else:
        print("opçao \n")

    
    



