conta_normal = False
conta_universitaria = False
conta_especial = True
saldo = 2000
cheque_especial = 800
saque = int(input("Digite o valor do saque: "))

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o uso do cheque especial!")
    else: 
        print("Não foi possível realizar o saque. Saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente para realizar o saque.")
elif conta_especial:
    print("Adicionado uma conta especial")
else:
    print("Sistema não reconheceu seu tipo de conta. Entre em contato com o seu gerente do banco para mais informações.")
