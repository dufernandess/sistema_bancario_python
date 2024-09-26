def menu():
    menu = """
            Seja bem-vindo!
    Por favor, digite a opção desejada
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [cd] Cadastrar Cliente
    [lc] Listar Contas
    [q] Sair
    =>"""
    return input(menu)

def deposito(valor_deposito, saldo, extrato):
    
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato.append({"Deposito": valor_deposito})

    else:
        print("Erro! O valor é inválido!")

    return saldo, extrato

def saque(valor_saque, saldo, extrato, limite_saque, NUMERO_SAQUES, contagem_saque):

    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > limite_saque
    excedeu_saques = contagem_saque >= NUMERO_SAQUES

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")

    elif valor_saque > 0:
        saldo -= valor_saque
        contagem_saque += 1
        extrato.append({"Saque": valor_saque})

    else:
        print("Erro: O valor é inválido")

    return saldo, extrato, limite_saque, NUMERO_SAQUES, contagem_saque

def exibir_extrato(saldo, extrato):
    print("==========EXTRATO==========\n")
    if not extrato:
        print("Não foram realizadas movimentações.")
    for transacao in extrato:
        for tipo, valor in transacao.items():
            print(f"{tipo}: R$ {valor:.2f}")
    print(f"\nSaldo: R$ {saldo:.2f}\n")
    print("========================\n")
    print("Agrademos a sua preferência! Até mais!")
    
def cadastrar_cliente(AGENCIA, num_conta, clientes, conta_bancaria):
    cpf = input("Digite o cpf do usuário (somente números): ")
    
    usuario = confirmar_cpf(cpf, clientes)

    if(usuario):
        print("Usuário já cadastrado!")
        return

    nome = input("Digite o nome completo do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário no formato (AA/MM/DD): ")    
    endereco = input("Digite o endereco do usuário no formato (logradouro, nro, bairro, cidade/sigla estado): ")

    cliente = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
    clientes.append(cliente)

    conta_bancaria.append({"Agencia": AGENCIA, "Número da conta": num_conta, "Cliente": cliente})

    print("Usuário cadastrado com sucesso!")
    
def confirmar_cpf(cpf, clientes):
    for usuario in clientes:
        if usuario["cpf"] == cpf:
            return usuario
        return None

def listar_contas(conta_bancaria):
    for conta in conta_bancaria:
                print("Agência:", conta["Agencia"],"Nro Conta:", conta["Número da conta"],"Cliente:", conta["Cliente"]["nome"], "CPF:", conta["Cliente"]["cpf"])

def operacoes_menu():
    
    saldo = 0
    num_conta = 1
    limite_saque = 500
    extrato = []
    clientes = []
    conta_bancaria = []
    contagem_saque = 0
    AGENCIA = "0001"
    NUMERO_SAQUES = 3

    while True:
        opcao = menu()

        if opcao == "d":
            valor_deposito = float(input("Digite o valor que deseja depositar: "))
            saldo, extrato = deposito(valor_deposito, saldo, extrato)

        elif opcao == "s":
            valor_saque = float(input("Digite o valor que deseja sacar: "))
            saldo, extrato, limite_saque, NUMERO_SAQUES, contagem_saque = saque(valor_saque, saldo, extrato, limite_saque, NUMERO_SAQUES, contagem_saque)
            
        elif opcao == "e":
           exibir_extrato(saldo, extrato)
        
        elif opcao == "cd":
            cadastrar_cliente(AGENCIA, num_conta, clientes, conta_bancaria)
            num_conta += 1

        elif opcao == "lc":
            listar_contas(conta_bancaria)

        elif opcao == "q":
            break

        else:
            print("Opção inválida, por favor, tente novamente")

operacoes_menu()
