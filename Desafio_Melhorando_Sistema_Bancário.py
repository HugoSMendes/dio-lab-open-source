# Criar Sistema Bancário:

# Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar
# suas operações e para isso escolheu a linguagem Python. Para a primeira versão dos sistema devemos
# implementar apenas 3 operações: depósito, saque e extrato.,

# Operação de depósito deve ser possível depositar valores positivos para a minha conta bancária. A
# v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar
# qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável
# e exibidos na operação extrato.

# Operação de saque deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso 
# o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível 
# sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos
# na operação extrato. 

# Operação de extrato deve listar todos os depósitos e saques realizados na conta. No fim da listagem
# deve ser exibido o saldo atual da conta.

# Os valores devem ser exibidos utilizando o formato R$ xxx.xx
# Exemplo: 1500.45 = R$ 1500.45


# Mehorando Sistema Bancário:
#     Separar as funções existentes de saque, depósito e extrado em funções. Criar duas novas funções:
#     cadastrar usuário (Cliente) e cadastrar conta bancária.

#     Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações 
#     existentes: sacar, depositar e visualizar extrato. Além disso, para a versão 2 do nosso sistema
#     precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente
#     (vincular com o usuário).

#     Separação em funções:
#     Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos
#     neste módulo, cada função vai ter uma regra na passagem de agumentos. O retorno e a forma como 
#     serão chamadas, pode ser definida por você da forma que achar melhor.

import textwrap

# Depósito: A função depósito deve receber os argumentos apenas por posiçao (positional only). Sugestão
#           de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito.....................: R$ {valor:.2f}\n"
        print("""
              +++++++++++++++++++++++++++++++++++++++
              +   Depósito realizado com sucesso!   +
              +++++++++++++++++++++++++++++++++++++++
              """)
    else:
        print("""
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
              @  A operação falhou! O valor informado é inválido.   @
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
              """)
    
    return saldo, extrato

# Saque: A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos
#        saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestao de retorno: saldo e extrato.
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    print(f"\n================ OPERAÇÃO SACAR ================")
    valor = float(input("Informa o valor do saque: "))
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("""
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
              @  Operação falhou! Você não tem saldo suficiente.  @
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
              """)
    
    elif excedeu_limite:
        print("""
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
              @  Operação falhou! O valor do saque excede o limite.  @
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
              """)
    
    elif excedeu_saques:
        print("""
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
              @  Operação falhou! Número máximo de saques excedido.  @
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
              """)

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque........................: R$ {valor:.2f}\n"
        numero_saques += 1
        print("""
              ++++++++++++++++++++++++++++++++++++
              +   Saque realizado com sucesso!   +
              ++++++++++++++++++++++++++++++++++++
              """)

    else:
        print("""
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @  Operação falhou! O valor informado é inválido.  @
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        """)

    return saldo, extrato

# Extrato: A função extrato deve receber os argumentos por posição e nome (positional only e keyword only).
#          Argumentos posicionais: saldo, argumentos nomeados: extrato.
def exibir_extrato(saldo, /, *, extrato):
    print(f"\n=================== OPERAÇÃO EXTRATO ==================")
    print("Naõ foram realizados movimentações." if not extrato else extrato)
    print(f"\n------------------------ SALDO ------------------------")
    print(f"Saldo........................: R$ {saldo:.2f}")
    print("=======================================================")


# Criar usuário: O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome,
#                data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro,
#                numero - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. 
#                não podemos cadastrar 2 usuários com o mesmo CPF.
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("""
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
              @  Já existe usuário com este CPF!  @
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
              """)
        return

    nome = input("Informe o nome completo do usuário: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco":endereco})

    print(f"""
          +++++++++++++++++++++++++++++++++++
          +  Usuário cadastrado com sucesso +
          +++++++++++++++++++++++++++++++++++
          """)

# Criar conta: O programa deve armazenar contas em uma lista, uma conta é composta por: agência, 
#              numero de conta e usuário. O numero da conta é sequencial, iniciando em 1. O número
#              da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta 
#              pertence a somente um usuário:
def cadastrar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("""
              +++++++++++++++++++++++++++++++
              +  Conta criada com sucesso!  +
              +++++++++++++++++++++++++++++++
              """)
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("""
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
          @  Usuario não encontrado, cadastre este novo usuario.  @
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
          """)
    return None

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agência..........: {conta['agencia']}
        C/C..............: {conta['numero_conta']}
        Titular..........: {conta['usuario']['nome']}
        """
        print("="*100)
        print(textwrap.dedent(linha))

def menu():
    menu = """\n
    =============== MENU ===============
    [1] Cadastrar Cliente
    [2] Cadastrar Conta
    [3] Listar Contas
    [4] Depositar
    [5] Sacar
    [6] Extrato
    [7] Sair
    =>"""
    return input(textwrap.dedent(menu))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opção = menu()

        if opção == "4":
            print(f"\n================ OPERAÇÃO DE DEPOSITAR ================")
            valor = float(input("Informe o valor a depositar: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
       
        elif opção == "5":
            print(f"\n================ OPERAÇÃO SACAR ================")
            valor = float(input("Informa o valor do saque: "))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opção == "6":
            exibir_extrato(saldo, extrato=extrato)

        elif opção == "1":
            criar_usuario(usuarios)

        elif opção == "2":
            numero_conta = len(contas)+1
            conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opção == "3":
            listar_contas(contas)

        elif opção == "7":
            print(f"\n ================ OPERAÇÃO SAIR ================")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
