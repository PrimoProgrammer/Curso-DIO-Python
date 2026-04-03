def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente para realizar o saque.")

    print("Obrigado por ser nosso cliente, volte sempre!")

def depositar(valor):
    saldo = 500
    saldo += valor

depositar(300)

sacar(510)


