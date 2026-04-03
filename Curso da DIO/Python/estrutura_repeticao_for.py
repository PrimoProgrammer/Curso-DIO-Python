texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

#EXEMPLO UTILIZANDO UM ITERÁVEL (STRING)
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:      
    print()



#EXEMPLO UTILIZANDO A FUNÇÃO BUILT-IN RANGE
for numero in range(0, 51, 5):
    print(numero, end="-")

print("=" *20)

for num in range (1, 11):
    print(num, end=" ")
