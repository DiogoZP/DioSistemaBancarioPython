
from datetime import datetime
'''
Faça um programa que simule um sistema bancário, onde o usuário poderá escolher entre as opções:
Depósito, Saque e Extrato. O limite para cada saque é 500 reais. Só podem ser feitos 3 saques por dia.
'''



VALOR_MAXIMO_SAQUE = 500
LIMITADOR_SAQUES = 3

extratos:list = []
saldo:float = 0.00
quantidade_saques:int = 0


while True:
    print("""Escolha uma das opções abaixo:
        [1] - Depósito
        [2] - Saque
        [3] - Extrato
        [4] - Sair
        """)

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        deposito = float(input("Digite o valor do depósito: "))
        if deposito <= 0:
            print("Valor inválido!")
        else:
            saldo += deposito
            extratos.append(("Depósito", deposito, str(datetime.now())))
            print(f"Depósito realizado com sucesso! Seu saldo atual é de R$ {saldo:.2f}")
    elif opcao == 2:
        saque = float(input("Digite o valor do saque: "))
        if saque <= 0:
            print("Valor inválido!")
        elif saque > VALOR_MAXIMO_SAQUE:
            print(f"O valor máximo para saque é de R$ {VALOR_MAXIMO_SAQUE}")
        elif saque > saldo:
            print("Saldo insuficiente!")
        elif quantidade_saques >= LIMITADOR_SAQUES:
            print("Limite de saques diários atingido!")
        else:
            saldo -= saque
            extratos.append(("Saque", saque, str(datetime.now())))
            quantidade_saques += 1
            print(f"Saque realizado com sucesso! Seu saldo atual é de R$ {saldo:.2f}")
    elif opcao == 3:
        print("==== Extrato ====")
        for extrato in extratos:
            print(f"Operação: {extrato[0]} | Valor: {extrato[1]:.2f} | Data: {extrato[2]}")
    elif opcao == 4:
        print("Saindo do sistema...")
        break