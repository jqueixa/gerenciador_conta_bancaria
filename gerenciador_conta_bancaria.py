saldo = 0
limite = 500
extrato = ""


while True:
    print("""
[1] Depositar
[2] Sacar
[3] Extrato
[S] Sair
""")
    opcao = input("Digite a opção desejada: ").upper()

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        if valor <= saldo and valor <= limite:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
        else:
            print("Operação falhou! Você não pode sacar mais que R$ 500,00 reais no dia!")

    elif opcao == "3":
        print(
    """
                \n=============EXTRATO==============
    """)
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n===============================")

    elif opcao == "S":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
