menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()

    if opcao == "d":
        valor = input("Informe o valor do depósito: ")

        if not valor.isdigit():
            print("Operação falhou! O valor deve ser um número.")
        else:
            valor = float(valor)
       
            if valor > 0:
                saldo += float(valor)
                extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("Operação falhou! O valor deve ser um número positivo.")
        

    elif opcao == "s":
        valor = input("Informe o valor do saque: ")

        if not valor.isdigit():
            print("Operação falhou! O valor deve ser um número positivo.")
        else:
            valor = float(valor)
        
            if valor <= 0:
                print("Operação falhou! O valor deve ser um número positivo.")
            elif valor > saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif valor > limite:
                print(f"Operação falhou! O valor do saque excede o limite de R${limite}.")
            elif numero_saques >= LIMITE_SAQUES:
                print("Operação falhou! Número máximo de saques excedido.")
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "q":
        print("Obrigado por utilizar o nosso sistema.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
