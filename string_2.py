nome = "Luan"
idade = 34
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Luan", "idade": 34, "profissao": "Programador", "linguagem": "Python"}

print("Nome: %s idade: %d profissão: %s linguagem %s" %(nome, idade, profissao, linguagem))

print("Nome: {} idade: {} profissão: {} linguagem {}".format(nome, idade, profissao, linguagem))

print("Nome: {3} idade: {2} profissão: {1} linguagem {0}".format(linguagem, profissao, idade, nome))

print(f"Nome: {nome} idade: {idade} profissão: {profissao} linguagem {linguagem}")

print("Nome: {nome} idade: {idade} profissão: {profissao} linguagem {linguagem}".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print("nome: {nome} idade: {idade} profissão: {profissao} linguagem: {linguagem}".format(**dados))

print(f"Saldo: {saldo:10.2f}")