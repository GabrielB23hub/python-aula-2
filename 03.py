# Escreva um programa em Python que receba as seguintes informações de usuário:
# - Renda Mensal: (um número float)
# - Score de Crédito (um número inteiro de 0 a 1000)
# - Possui Bens como Garantia? (uma string: "sim"ou "não)
# - Tem Histórico de inadimplência? (uma string: "sim" ou "não)
#
# O empréstimo será APROVADO se o cliente cumprir uma das duas regra abaixo:
# Regra 1: Ter renda mensal maior ou igual a R$ 3.000,00
#          E score de crédito maior ou igual a 600
#          E NÃO ter histórico de inadimplência.
# Regra 2: Independente da renda ou score,
#          se o cliente NÃO tiver histórico de inadimplência
#          E possuir bens como garantia, ele tamabém é aprovado.
# Se o cliente não se encaixar em nenhuma das duas regra,
# o empréstimo será REPROVADO

RendaMensal = float(input("Qual a renda mensal? "))
score = int(input("Qual o seu score? "))
bens = input("Há bens como garantia? ")
historico = input("Tem histórico de indimplência? ")

if RendaMensal >= 3000 and score >= 600 and historico.lower() == "nao":
    print("Empréstimo Aprovado")
elif historico.lower() == "nao" and bens.lower() == "sim":
    print ("APROVADO")
else:
    print("Reprovado")