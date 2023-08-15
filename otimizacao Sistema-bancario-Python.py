# Sistema-bancario-Python
# Otimização - Modularização + criação das funções criar usuario/conta
#Sistema de deposito - saque - extrato com Python

#Criação do menu inicial - Sistema bancário
def Menu():

    Menu = """" \n
 ========== Menu ==========

    [1]\tDeposito
    [2]\tSaque
    [3]\tExtrato
    [4]\tCriar usuário
    [5]\tCriar conta
    [6]\tContas
    [7]\tSair

 ==========================
    => """

    return input(Menu)

def deposito(saldo,valor,extrato, /):
    if valor>0: #Verificação se o valor do deposito é maior que 0 
            saldo += valor #acumulador dos valores
            extrato += f"Deposito: R$ {valor:.2f}\n" #bloco para armazenar dado que será gerado no extrato
            print("Deposito realizado com sucesso!")
    else:
        print("Operação falhou: valor informado inválido!")

    return saldo,extrato
    
def saque (*, saldo,valor, extrato, limite, numero_saques,limite_saques):
     
     if valor<0:
        print("\n Operação falhou: Valor informado inválido!")

     elif valor > limite: 
         print("\n Operação falhou, saldo extrapola o valor limite!")

     elif valor > saldo:
         print("\n Operação falhou, valor de saque maior que o saldo em conta!")

     elif numero_saques >= limite_saques:
         print("\n Operação falhou, numero de saques diários atendido!")

     elif valor>0:
         saldo = saldo - valor
         extrato += f"Saque:\t\tR${valor:.2f}"
         numero_saques = numero_saques + 1

         print("\nSaque realizado com sucesso!")

     else:
         print("\nOperação falhou, digite um valor válido!")

     return (saldo,extrato)

def exibir_extrato(saldo,/,*,extrato):

    print("\n ======== Extrato ========")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\n Saldo:\t\tR$ {saldo:.2f}")
    print("\n ============================")

def criar_usuario(usuarios):

    CPF = input("Entre com o seu CPF: ")
    usuario = usuarios_cadastrados(CPF,usuarios)

    if usuario:

        print("Já existe um usuário cadastrado com esse CPF")
        return
    
    Nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite a data de seu nascimento: ")
    endereco = input("Entre com o seu endereço no seguinte formato - logradouro, nº - bairro - cidade/sigla estado")

    usuarios.append({"Nome":Nome,"data_nascimento":data_nascimento,"CPF":CPF,"endereço":endereco})

    print("Usuário cadastrado com sucesso!")
    
def usuarios_cadastrados(CPF,usuarios):

    filtro_usuarios=[usuario for usuario in usuarios if usuario ["CPF"]==CPF]
    return filtro_usuarios[0] if filtro_usuarios else None

def criar_contas(Agencia,numero_conta,usuarios):

    CPF = input("Entre com o seu CPF: ")
    usuario = usuarios_cadastrados(CPF,usuarios)

    if usuario:
        print("\n |||  Conta criada com sucesso  |||")
        return{"Agência":Agencia,"Numero_conta":numero_conta,"Usuário":usuario}
    
    print("\n Usuário não encontrado, digite um CPF válido!")

def contas_cadastradas(contas):

    for conta in contas:

        cadastro = f"""\
        
                Agência:\t{conta['Agência']}
                C/C:\t\t{conta['Numero_conta']}
                Titular:\t{conta['Usuário']['Nome']}

                """
        
        print("=" * 100)
        print(cadastro)

def Main():

    usuarios = []
    contas =[]
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    Agencia = "0001"

    while True:

        opcao = Menu()

        if opcao == "1":

            valor = float(input("Informe o valor do deposito: "))

            saldo,extrato =deposito(saldo,valor,extrato)

        elif opcao == "2":

            valor = float(input("Entre com o valor a ser sacado: "))

            saldo,extrato = saque (
                saldo = saldo,
                limite = limite,
                extrato = extrato,
                numero_saques = numero_saques,
                limite_saques = limite_saques,
                valor = valor,
            )

        elif opcao == "3":

            exibir_extrato(saldo,extrato = extrato)

        elif opcao == "4":

            criar_usuario(usuarios)

        elif opcao == "5":

            numero_conta = len(contas) + 1
            conta = criar_contas(Agencia,numero_conta,usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":

            contas_cadastradas(contas)

        elif opcao == "7":

            break
        else: 
            print("Opção selecionada inválida, selecione uma opção válida!")

Main()
