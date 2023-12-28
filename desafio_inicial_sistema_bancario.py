"""Sistema-bancario-Python
   Sistema de deposito - saque - extrato com Python"""

#Criação do menu inicial - Sistema bancário
MENU = """"
[1]:Deposito
[2]:Saque
[3]:Extrato
[4]:Sair

=> """

# inicialização das variaveis
SALDO = 0
LIMITE = 500
EXTRATO = ""
NUMERO_SAQUES = 0
LIMITE_SAQUES = 3
DEPOSITO = 0

# Calculo e operações

while True:

    opcao = input(MENU)

    if opcao == "1": #bloco para o calculo da opção de deposito

        deposito= float(input("Informe o valor do deposito: "))

        if deposito>0: #Verificação se o valor do deposito é maior que 0
            SALDO += deposito #acumulador dos valores
            EXTRATO += f"Deposito: R$ {deposito:.2f}\n"
            #bloco para armazenar dado que será gerado no extrato

        else:
            print("Operação falhou: valor informado inválido!") #bloco para a opção de erro

    elif opcao == "2": #bloco para o calculo da realização da operação de Saque

        saque = float(input("Informe o valor a ser sacado: "))

        if saque<0: #bloco para opção de erro ao tentar sacar valores menores que 0
            print("Operação falhou: Valor informado inválido!")

        elif saque>500: #bloco de opção de erro ao tentar saques maiores que R$500,00
            print("Operação falhou: Valor informado excede o valor de saque disponivel")
        #bloco de opção de erro ao tentar sacar valores que excedem o saldo disponivel
        elif deposito < saque:
            print("Operação falhou: Valor informado excede o saldo disponivel")

        elif NUMERO_SAQUES >=3: #bloco de opção de erro ao tentar sacar mais de 3x ao dia
            print("Operação falhou: Numero maximo de saques excedido")

        elif saque >0: #bloco para o calculo do saque e resultado do extrato
            SALDO -= saque
            EXTRATO += f"Saque R$ {saque:.2f}\n"
            NUMERO_SAQUES += 1
        else:
            print("Operação falhou: O valor informado é invalido!")

    elif opcao=="3": #bloco para a realização da operação de extrato
        print("\n ======== Extrato ========")
        print("Não foram realizadas movimentações" if not EXTRATO else EXTRATO)
        print(f"\n Saldo: R$ {SALDO:.2f}")
        print("\n ============================")

    elif opcao=="4":
        print("Obrigado, por utilizar nossos serviços!")
        break

    else:
        print("Operação invalida: volte ao Menu e informe uma opção válida")
