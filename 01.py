# Escreva um progrrama em python que peças as seguintes informações:
# - idade (um número inteiro)
# - Altura em centímetros (um número inteiro)
# - Tem autorização dos pais? (uma string: "sim"ou "não˜)
#
# O programa deve exibir "Acesso Liberado!" se o visitante puder andar no brinquedo,
# ou "Acesso Negado." caso contrário.
#
# Regra
# O visitante pode entrar se:
# - Tiver idade maior ou igual a 12 E altura maior ou igual a 140 OU
# - se tiver autorização igual a "sim".
# - se tiver idade maior ou igual a 18 não perguntar a idade

idade = int(input("Digite a sua idade: " ))
Altura = int(input("Digite a sua altura: " ))
autorizacao = ""

if Altura < 140:
    print("Acesso Negado!")

elif idade >= 18:
    autorizacao = "sim"  # Ignora a autorização para maiores de 18 anos
    print("Acesso Liberado!")
elif idade < 18:
    autorizacao = input("Você tem autorização dos seus pais? (sim/não): ").lower()

elif (idade >= 12 and Altura >= 140) and autorizacao.lower() == "sim":
    print("Acesso Liberado!")
else:
    print("Acesso Negado.")           