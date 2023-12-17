## Desafio Modelando o Sistema Bancário em POO com Python 

# 1º Passo Criação da classe Cliente e sua classe filha PessoaFisica
from abc import ABC, abstractmethod, abstractproperty
import datetime
import textwrap


class Cliente():

    # Construtor com passagem de parâmetros
    def __init__(self,endereco):
        self.endereco = endereco
        self.contas = []

    
    # Criação do método Realizar transação(conta:Conta, transação: Transação)
    def realizar_transação(self,conta,transacao):
        transacao.registrar(conta)
        
        
    # Criação do método Adicionar Conta (conta:Conta)
    def adicionar_conta(self,conta):
        self.contas.append(conta)

    ## Criação da classe filha Pessoa Fisica
class PessoaFisica(Cliente):

    ## Construtor com passagem de parâmetros Endereço e Contas
    def __init__(self,cpf,nome,data_nascimento,endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

# 2º Passo criação da classe Conta e sua classe filha ContaCorrente
class Conta():

    # Construtor da classe conta com passagem de parâmetros
    def __init__(self, numero,cliente):

        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()


    ## Criação dos métodos
        
          ## Criação do método nova conta (cliente: Cliente, numero: int, Conta)
    @classmethod
    def nova_conta(cls,cliente,numero):
        
        return cls(numero,cliente)
    
        ## Criação do método saldo
    @property
    def saldo (self):

        return self._saldo

        ## Criação do método de acsso ao numero da conta
    @property
    def numero(self):

        return self._numero

        ## Criação do método de acsso ao agencia da conta
    @property
    def agencia(self):

        return self._agencia

        ## Criação do método de acsso ao cliente da conta
    @property
    def cliente(self):

        return self._cliente
    
    
        ## Criação do método de acsso ao historico da conta
    @property
    def historico(self):

        return self._historico
    
    ## Criação do metodo Sacar
    def sacar(self,valor):

        saldo = self.saldo
        valor_excedido = valor > saldo

            ## Bloco para tratamento de erro em caso de saldo insuficiente para saque
        if valor_excedido:
            print("\n Operação falhou! Saldo insuficiente")
            return False
        
        elif valor > 0:
            self._saldo -= valor
            print("\n Saque realizado com sucesso!")
            return True

        else:
            print("\n Operação falhou! Valor informado inválido")
            return False
        

    ## Criaçãop do método Depositar
    def depositar(self,valor):

        ## Bloco para verificação se valor a ser depositado é maior que zero
        if valor > 0:
            self._saldo  += valor
            print("\n Depósito realizado com sucesso!")
            return True

        else:
            print("\n Não foi possivel realizar o depósito, tente novamente!")
            return False
        
        

    ## Criação da classe filha ContaCorrente
class ContaCorrente(Conta):

    # Criação contrutor com passagem de parâmetros
    def __init__(self,numero,cliente,limite = 500, limite_sques = 3):
        super().__init__(numero,cliente)
        self.limite = limite
        self.limite_sques = limite_sques

    ## Criação do método Sacar
    def sacar(self,valor):
        # Bloco para verificar se a quantidade de saques realizados pelo cliente
        numero_saques = len([transacao for transacao in self.historico.transacoes
                             if transacao["tipo"]==Saque.__name__])

        # Bloco para inicialização das variaveis de valor excedido (Limite e Saques)
        limite_excedido = valor > self.limite
        saques_excedido = numero_saques >= self.limite_saques

        ## Bloco de decisão para Limite excedido
        if limite_excedido:
            print("\n Operação falhou! Valor informado excede o saldo em conta!")
            return False

        elif saques_excedido:
            print("\n Operação falhou! Limite de saques diários atingido")
            return False

        else:
            return super().sacar(valor)
    
    ## Método para informar as informações da conta
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            Conta Corrente:\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

# 3 Passo Criação da classe Historico
class Historico():

    ## Criação do construtor com passagem de parâmetros
    def __init__(self, adicionar_transacao):

        self._transacoes = []

    @property
    def transacoes(self):

        return self._transacoes
    
        ## Criação do historico de transações realizadas
    def adicionar_transacao(self,transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strtime("%d-%m-%Y %H:%M:%S"),
            }
        )

# 4º Passo criação da classe Interface (abstrato) Transação
class Transacao(ABC):

    @property
    @abstractproperty
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self,conta):
        pass

# 5º Passo criação das classes Saque e Deposito que são filhas da classe Transação

    ## Criação da classe Saque
class Saque(Transacao):

    ## Criação do construtor com passagem de parâmetros
    def __init__(self,valor):
        self._valor = valor

        ## Método Getters para acessar valor 
    @property
    def valor(self):

        return self._valor

        ## Criação do Método registrar para registrar transação de saque da conta
    def registrar(self,conta):
        transacao_realizada = conta.sacar(self.valor)

        if transacao_realizada:
            conta.historico.adicionar_transacao(self)

    ## Criação da classe Deposito
class Deposito(Transacao):

    ## Criação do Construtor com passagem de parâmetros
    def __init__(self,valor):
        self._valor = valor

        ## Método Getters para acessar valor 
    @property
    def valor(self):

        return self._valor
    
    ## Criação do Método registrar para registrar transação de saque da conta
    def registrar(self,conta):
        transacao_realizada = conta.depositar(self.valor)

        if transacao_realizada:
            conta.historico.adicionar_transacao(self)


## Parte extra onde será implementado parte do código desenvolvido no desafio anterior de sistema bancário

    ## Função Menu principal de acesso ao sistema bancário
def menu():

    menu = """\n
    ==================== Menu ====================
    [d]\tDeposito
    [s]\tSaque
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Constas
    [nu]\tNovo Usuário
    [q]\tSair
    ==> """
    return input(textwrap.dedent(menu))

    ## Função filtrar Clientes
def filtrar_clientes(cpf,clientes):

    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

    ## Função recuperar conta de clientes
def recuperar_conta_clientes(cliente):

    if not cliente.contas:
        print("\n Usuário não encontrado")
        return
    
    # FIXME: não permite que cliente escolha a conta
    return cliente.contas[0]

## Função depositar saldo na conta de clientes
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf,clientes)

    if not cliente:
        print("\n Não foi possivel localizar o CPF do cliente informado!")
        return
    
    valor = float(input("Informe o valor de deposito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_clientes(cliente)
    
    if not conta:
        return
    
    cliente.realizar_transação(conta,transacao)

## Função sacar saldo na conta de clientes
def sacar(clientes):

    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf,clientes)

    if not cliente:
        print("\n Não foi possivel localizar o CPF do cliente informado!")
        return
    
    valor = float(input("Informe o valor de saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_clientes(cliente)
    
    if not conta:
        return
    
    cliente.realizar_transação(conta,transacao)

## Função extrato da conta de clientes
def exibir_extrato(clientes):

    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf,clientes)

    if not cliente:
        print("\n Não foi possivel localizar o CPF do cliente informado!")
        return
    
    conta = recuperar_conta_clientes(cliente)
    
    if not conta:
        return
    
    print("\n==================== Extrato =====================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "\nNão foram realizadas movimentações"
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}"
    
    print(extrato)

## Função Criar Usuarios
def criar_clientes(clientes):

    cpf = input("Informe o numero do CPF do cliente: ")
    cliente = filtrar_clientes(cpf,clientes)

    if cliente:
        print("\nCPF informado já esta cadastrado")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input ("Informe sua data de nascimento (dd-mm-aa): ")
    endereco = input("Informe seu endereço (Rua / Numero / Bairro / Cidade / Estado): ")

    cliente = PessoaFisica(nome = nome, data_nascimento= data_nascimento, endereco= endereco, cpf = cpf)
    clientes.append(cliente)

    print("\ |||| Cliente cadastrado com sucesso! ||||")

## Função Criar Contas
def criar_conta(numero_conta,clientes,contas):

    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("\nCPF não encontrado, tente novamente!")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n |||| Conta criada com sucesso ||||")

## Função Listar Contas
def listar_contas(contas):

    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

## Função Principal
def main():

    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)
            
        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "nu":
            criar_clientes(clientes)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break
main()