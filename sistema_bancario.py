menu = """

        Seja bem-vindo!
Por favor, digite a opção desejada

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

=>"""

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor que deseja depositar: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato_deposito = f"Depósito: R$ {valor_deposito:.2f}"
            extrato.append(extrato_deposito)

        else:
            print("Erro! O valor é inválido!")

    elif opcao == "s":
        valor_saque = float(input("Digite o valor que deseja sacar: "))

        if valor_saque <= 500:

            if valor_saque > saldo:
                print("Não há saldo disponível para o saque!")

            elif valor_saque < saldo and valor_saque > limite:
                print("O limite de saque é de até R$500.00")

            elif valor_saque < saldo and valor_saque < limite and numero_saques >= LIMITE_SAQUES:
                print("Você já excedeu o limite de saques diários!")

            elif valor_saque < saldo and valor_saque < limite and numero_saques < LIMITE_SAQUES:
                saldo -= valor_saque
                numero_saques += 1
                extrato_saque = f"Saque: R$ {valor_saque:.2f}"
                extrato.append(extrato_saque)

        else:
            print("Erro: O valor é inválido")

    elif opcao == "e":
        print("==========EXTRATO==========\n")
        for item in extrato:
            print(item)
        print(f"\nSaldo: R$ {saldo:.2f}\n")
        print("========================\n")
        print("Agrademos a sua preferência! Até mais!")

    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor, tente novamente")
