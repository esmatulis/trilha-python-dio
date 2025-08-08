menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[nu] Cadastrar usuário
[nc] Cadastrar conta
[lc] Listar contas

=> """

AGENCIA = "0001"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Usuário já cadastrado!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
    endereco = input("Informe o endereço: ")

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if not usuario:
        print("Usuário não encontrado! Cadastre o usuário primeiro.")
        return None
    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    print("Conta criada com sucesso!")
    return conta

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    print("\n=== CONTAS CADASTRADAS ===")
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Titular: {conta['usuario']['nome']}")
    print("==========================\n")

def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += "Depósito: R$ {:.2f}\n".format(valor)
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def saque(*, saldo, valor, extrato, numero_saques, limite_saques):

    if (valor > saldo):
        print("Operação falhou! Você não tem saldo suficiente.")
    elif (valor > limite):
        print("Operação falhou! O valor do saque excede o limite.")
    elif (numero_saques >= limite_saques):
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += "Saque: R$ {:.2f}\n".format(valor)
        numero_saques += 1
        print("Saque realizado com sucesso!")
        
    return saldo, extrato, numero_saques


def extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================\n")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================\n")


while True:

    opcao = input(menu)

    if opcao == "d":
    #    Depositar
        valor = float(input("Informe o valor a depositar: "))
        saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
            
    elif opcao == "s":
       
        valor = float(input("Informe o valor a sacar: "))
        saldo, extrato, numero_saques = deposito(saldo=saldo, valor=valor, extrato=extrato, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
       
    elif opcao == "e":
        extrato(saldo, extrato=extrato)

    elif opcao == "nu":
        criar_usuario(usuarios)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == "lc":
        listar_contas(contas)
       
    elif opcao == "q":
        break

    else:
        print("Opção inválida! Por favor, selecione uma opção válida.")
       