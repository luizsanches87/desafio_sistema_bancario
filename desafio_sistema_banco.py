menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


while True:

    opcao = input(menu)
    opcao = opcao.lower()

    if opcao == "d":
        valor = input("Informe o valor do depósito: R$ ")
        valor_is_float = isfloat(valor)
        if valor_is_float:
            valor = float(valor)

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"

            else:
                print("Operação falhou! O valor informado é inválido.")
        else:
            print("Operação falhou! Informe um valor válido.")

    elif opcao == "s":
        valor = input("Informe o valor do saque: R$ ")
        valor_is_float = isfloat(valor)

        if valor_is_float:
            valor = float(valor)
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

            else:
                print("Operação falhou! O valor informado é inválido.")
        else:
            print("Operação falhou! Informe um valor válido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
