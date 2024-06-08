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

menu = """
[d] Depositar
[s] Sacar
[e] Extrato 
[q] Sair
=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opção = input(menu)

    if opção == "d":
        print(f"\n================ OPERAÇÃO DE DEPOSITAR ================")
        valor = float(input("Informe o valor a depositar: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito.....................: R$ {valor:.2f}\n"        
            print(extrato)
        else:
            print(f"A operação falhou! O valor informado é inválido.")
    
    elif opção == "s":
        print(f"\n================ OPERAÇÃO SACAR ================")
        valor = float(input("Informa o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >=LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido")

        elif valor > 0:

            saldo -= valor
            extrato += f"Saque........................: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Operação falhou! O valor informado é inválido")

    elif opção == "e":
        print(f"\n=================== OPERAÇÃO EXTRATO ==================")
        print("Naõ foram realizados movimentações." if not extrato else extrato)
        print(f"\n------------------------ SALDO ------------------------")
        print(f"Saldo........................: R$ {saldo:.2f}")
        print("=======================================================")

    elif opção == "q":
        print(f"\n ================ OPERAÇÃO SAIR ================")
        break
    
else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")
