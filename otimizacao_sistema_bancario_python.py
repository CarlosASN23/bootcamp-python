"""sistema-bancario-Python
otimização - Modularização + criação das funções criar usuario/conta
Sistema de deposito - saque - extrato com Python"""


def menu():
    """Criação do menu inicial - Sistema bancário"""
    menu_principal = """" \n
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

    return input(menu_principal)

def deposito(saldo,valor,extrato, /):
    """Função Deposito: Será pedido um valor do tipo float
       ao usuario, para que seja feito a operação de depósito"""
    if valor>0: #Verificação se o valor do deposito é maior que 0
        saldo += valor #acumulador dos valores
        #bloco para armazenar dado que será gerado no extrato
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print("Deposito realizado com sucesso!")
    else:
        print("Operação falhou: valor informado inválido!")

    return saldo,extrato
def saque (*, saldo,valor, extrato, limite, numero_saques,limite_saques):
    """Função Saque: Será pedido um valor do tipo float
          ao usuario, para que seja feito a operação de saque"""
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
    """Função Extrato: Será impresso a lista de operações
       realizadas pelo usuário"""

    print("\n ======== Extrato ========")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\n Saldo:\t\tR$ {saldo:.2f}")
    print("\n ============================")

def criar_usuario(usuarios):
    """Função Criar Usuario: função responsavel
       por criar novos usuários do sistema"""
    cpf = input("Entre com o seu CPF: ")
    usuario = usuarios_cadastrados(cpf,usuarios)

    if usuario:

        print("Já existe um usuário cadastrado com esse CPF")
        return
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite a data de seu nascimento: ")
    endereco = input("Entre com o seu endereço no seguinte formato - "
                     "logradouro, nº - bairro - cidade/sigla estado")
    usuarios.append({"Nome":nome,"data_nascimento":data_nascimento,"CPF":cpf,"endereço":endereco})
    print("Usuário cadastrado com sucesso!")

def usuarios_cadastrados(cpf,usuarios):
    """Função Usuarios cadastrados: função responsavel
       por verificar se o usuário esta cadastrado"""
    filtro_usuarios=[usuario for usuario in usuarios if usuario ["CPF"]==cpf]
    return filtro_usuarios[0] if filtro_usuarios else None

def criar_contas(agencia,numero_conta,usuarios):
    """Função Criar Contas: função responsavel
       por criar novas contas no sistema"""

    cpf = input("Entre com o seu CPF: ")
    usuario = usuarios_cadastrados(cpf,usuarios)

    if usuario:
        print("\n |||  Conta criada com sucesso  |||")
        return{"Agência":agencia,"Numero_conta":numero_conta,"Usuário":usuario} 
    print("\n Usuário não encontrado, digite um CPF válido!")

def contas_cadastradas(contas):
    """Função Filtrar contas cadastradas: 
       função responsavel por filtrar as
       contas cadastradas no sistema"""

    for conta in contas:

        cadastro = f"""\
        
                Agência:\t{conta['Agência']}
                C/C:\t\t{conta['Numero_conta']}
                Titular:\t{conta['Usuário']['Nome']}

                """
        print(cadastro)

def main():
    """Função Main: função responsavel
       por acessar o sistema"""

    usuarios = []
    contas =[]
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    agencia = "0001"

    while True:

        opcao = menu()

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
            conta = criar_contas(agencia,numero_conta,usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":

            contas_cadastradas(contas)

        elif opcao == "7":

            break
        else:
            print("Opção selecionada inválida, selecione uma opção válida!")

main()

