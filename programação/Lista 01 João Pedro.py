#Entrada de dados e variáveis

#exercício 1

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

print(f"Olá, {nome}! Você tem {idade} anos!")

#exercicio 2

um = int(input("Digite o primeiro numero: "))
dois = int(input("Digite o segundo numero: "))

print(f"Soma = {um + dois}")

#exercicio 3

numero = int(input("Digite um número: "))

antecessor = numero - 1
sucessor = numero + 1

print("Antecessor:", antecessor)
print("Sucessor:", sucessor)

#exercicio 4

num = int(input("Digite um numero: "))

print(f" O dobro é {num * 2}")

#exercicio 5 

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"A média é {media}")

#Decisões if e else 

#exercicio 6

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

if idade >=18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

#exercicio 7 

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

media = (nota1 + nota2) /2

if media + nota2 >=7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")

#exercicio 8

numero = int(input("Digite um número: "))

if numero > 0:
    print("O número é positivo")
elif numero < 0:
    print("O número é negativo")
else:
    print("O número é zero")


#exercicio 9 

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero1 > numero2:
    print("O primeiro é maior")
else:
    print("O segundo é maior")

#exercicio 10 

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

if idade >=12:
    print("Entrada permitida.")
else:
    print("Entrada não permitida.")

#Repetição com for

#exercicio 11

for i in range(1,11):
    print(f"{i}")

#exercicio 12

numero = int(input("Digite um numero: "))
print(f"{numero}")

for contador in range(1, numero + 1):
    print(contador)

#exercicio 13

tabuada = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    resultado = tabuada * i
    print(f"{tabuada} * {i} = {resultado}")

#exercicio 14 

numero = int(input("Digite um numero: "))
print(f"{numero}")

for i in range(numero, -1, -1):
    print(f"{i}")

#exercicio 15 

numero = int(input("Digite um numero: "))
print(f"{numero}")

for i in range(2,numero + 1, 2):
    print(f"{i}")
