"""Desafio Modelando o Sistema Bancário em POO com Python"""
# 1º Passo Criação da classe Cliente e sua classe filha PessoaFisica
from abc import ABC, abstractmethod, abstractproperty
import textwrap


class Cliente():
    """Criação da classe Cliente com a criaçãos dos métodos
       Realizar TRansação e Adicionar Contas"""

    # Construtor com passagem de parâmetros
    def __init__(self,endereco):
        self.endereco = endereco
        self.contas = []
    # Criação do método Realizar transação(conta:Conta, transação: Transação)
    def realizar_transacao(self,conta,transacao):
        """Criação do método realizar transações (irá armazenar as infos)"""
        transacao.registrar(conta)
    # Criação do método Adicionar Conta (conta:Conta)
    def adicionar_conta(self,conta):
        """Criação do método adicionar contas (irá criar uma lista com as contas)"""
        self.contas.append(conta)

    ## Criação da classe filha Pessoa Fisica
class PessoaFisica(Cliente):
    """Criação da classe filha PessoaFisica"""

    ## Construtor com passagem de parâmetros Endereço e Contas
    def __init__(self,cpf,nome,data_nascimento,endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

# 2º Passo criação da classe Conta e sua classe filha ContaCorrente
class Conta():
    """Criação da classe Conta com a criação do 
       construtor com passagem de parâmentros
       e dos métodos referente as transações que serão
       realizadas pela usuário ao acessar sua conta"""

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
        """Método de Classe para a criação de uma nova conta"""
        return cls(numero,cliente)
        ## Criação do método saldo
    @property
    def saldo (self):
        """Método Get para acessar a variavel Saldo"""
        return self._saldo

        ## Criação do método de acsso ao numero da conta
    @property
    def numero(self):
        """Método Get para acessar a variavel Número da conta"""
        return self._numero

        ## Criação do método de acsso ao agencia da conta
    @property
    def agencia(self):
        """Médoto Get para acessar a variavel Agência"""
        return self._agencia

        ## Criação do método de acsso ao cliente da conta
    @property
    def cliente(self):
        """Médoto Get para acesso a variavel Cliente"""
        return self._cliente
        ## Criação do método de acsso ao historico da conta
    @property
    def historico(self):
        """Método Get para acessar o Historico de Movimentações da conta"""
        return self._historico
    ## Criação do metodo Sacar
    def sacar(self,valor):
        """ Métdo para realizar a opeção de saque pelo usuário
            ao informar um valor x do tipo float, também será
            verificado os casos em que houver erro humano de digitação
            do valor x"""

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
        """ Métdo para realizar a opeção de deposito pelo usuário
            ao informar um valor x do tipo float, também será
            verificado os casos em que houver erro humano de digitação
            do valor x"""

        ## Bloco para verificação se valor a ser depositado é maior que zero
        if valor > 0:
            self._saldo  += valor
            print("\n Depósito realizado com sucesso!")
            return True
        else:
            print("\nNão foi possivel realizar a operação")
            return False

    ## Criação da classe filha ContaCorrente
class ContaCorrente(Conta):
    """Criação da classe ContaCorrente que herda da classe
       Conta, com a criação do 
       construtor com passagem de parâmentros
       e dos métodos (Sacar) referente as transações que serão
       realizadas pela usuário ao acessar sua conta corrente"""

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
        saques_excedido = numero_saques >= self.limite_sques

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
class Historico:
    """Criação da classe Historico com a criação
       do construtor com passagem de parâmetros e 
       dos métodos @property Transações e Adicionar
       transações. Essa Classe foi criada para que fosse
       possivel a visualização dos historicos de transações
       feito por cada conta cadastrada no sistema"""

    ## Criação do construtor com passagem de parâmetros
    def __init__(self):

        self._transacoes = []

    @property
    def transacoes(self):
        """ Método @property para poder acessar as infos
            referentes as transãçoes """
        return self._transacoes
        ## Criação do historico de transações realizadas
    def adicionar_transacao(self,transacao):
        """Método @property adicionar transacao que permite
            adicionar as transações realizadas no historico"""
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
            }
        )

# 4º Passo criação da classe Interface (abstrato) Transação
class Transacao(ABC):
    """Criação da classe Interface Transação
       contendo os métodos abstractiones para 
        as variaveis valor e registrar"""

    @property
    @abstractproperty
    def valor(self):
        """Método abstrato valor, para retornar a variavel valor"""
    @abstractmethod
    def registrar(self,conta):
        """Método abstrato registrar, para retornar a variavel registrar"""

# 5º Passo criação das classes Saque e Deposito que são filhas da classe Transação

    ## Criação da classe Saque
class Saque(Transacao):
    """Classe filha Saque que herda da classe Transação
       com a criação do construtor com passagem de parâmetros
       e criação dos métodos para acessar as variaveis Valor e Registrar
       que registrará as transações feitas para a opção de Saque"""

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
    """Classe filha Saque que herda da classe Transação
       com a criação do construtor com passagem de parâmetros
       e criação dos métodos para acessar as variaveis Valor e Registrar
       que registrará as transações feitas para a opção de Deposito"""

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


# Parte extra onde será implementado parte do código desenvolvido
# no desafio anterior de sistema bancário
## Função Menu principal de acesso ao sistema bancário
def menu():
    """Implementação da função menu principal de acesso ao sistema bancário"""

    menu_principal = """\n
    ==================== Menu ====================
    [d]\tDeposito
    [s]\tSaque
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Constas
    [nu]\tNovo Usuário
    [q]\tSair
    ==> """
    return input(textwrap.dedent(menu_principal))

    ## Função filtrar Clientes
def filtrar_clientes(cpf,clientes):
    """Função para filtrar clientes e retorna-los ao usuário"""

    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

    ## Função recuperar conta de clientes
def recuperar_conta_clientes(cliente):
    """Função para recuperar as contas cadastradas"""

    if not cliente.contas:
        print("\n Usuário não encontrado")
        return
    return cliente.contas[0]

## Função depositar saldo na conta de clientes
def depositar(clientes):
    """Função para realizar a operação de deposito"""
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
    cliente.realizar_transacao(conta,transacao)

## Função sacar saldo na conta de clientes
def sacar(clientes):
    """Função Sacar, que retornará ao usuário
       o valor que se deseja retirar da conta
       e realizará o tratamento para os erros possiveis"""

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
    cliente.realizar_transacao(conta,transacao)

## Função extrato da conta de clientes
def exibir_extrato(clientes):
    """Criação da função Exibier extrato, que fará
       a operação de exibir as transações realizadas
       pelo cliente e salvas pelo métodos da classe
       Historico e Transação"""

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
    """ Criação da Função Criar Clientes
        retornara o método para o cadastro
        de novos clientes no sistema"""

    cpf = input("Informe o numero do CPF do cliente: ")
    cliente = filtrar_clientes(cpf,clientes)

    if cliente:
        print("\nCPF informado já esta cadastrado")
        return
    nome = input("Informe seu nome completo: ")
    data_nascimento = input ("Informe sua data de nascimento (dd-mm-aa): ")
    endereco = input("Informe seu endereço (Rua / Numero / Bairro / Cidade / Estado): ")

    cliente = PessoaFisica(nome = nome, data_nascimento= data_nascimento,
                           endereco= endereco, cpf = cpf)
    clientes.append(cliente)

    print(" |||| Cliente cadastrado com sucesso! ||||")

## Função Criar Contas
def criar_conta(numero_conta,clientes,contas):
    """Criação da Função Criar contas,
       permitirá aos usuários do sistema
       criar novas contas, através do cpf informado"""

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
    """Criação da Função Listar contas,
       permitirá aos usuários do sistema
       listar as contas, através do cpf informado"""

    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

## Função Principal
def main():
    """ Função Principal para acesso as operações
        a serem realizadas no sistema"""

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
