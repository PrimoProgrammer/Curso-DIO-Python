MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Quantos anos você tem? "))

if idade >= MAIOR_IDADE:
    print("Você já pode tirar sua CNH!")

if idade < MAIOR_IDADE:
    print("Você ainda não pode tirar sua CNH, aguarde mais um pouco!")

if idade >= MAIOR_IDADE:
    print("Você já pode tirar sua CNH!")

else:
    print("Você ainda não pode tirar sua CNH, aguarde mais um pouco!")

if idade >= MAIOR_IDADE:
    print("Você já pode tirar sua CNH!")

elif idade == IDADE_ESPECIAL:
    print("Você só pode fazer aulas teóricas, mas não pode dirigir ainda!")
else:
    print("Você ainda não pode tirar sua CNH, aguarde mais um pouco!")