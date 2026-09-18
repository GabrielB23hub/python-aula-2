# Escreva um programa em Python que pergunte três informações ao usuário:
# - É estudante? (uma string: "sim" ou "não")
# - Dia da semana? (uma string: "terça" ou "outro")
# - Tipo de sala (uma string: "vip"ou "comum")
#
# O programa deve exibir "Desconto Aplicado!""
# Ou "Valor Integral"
#
# Regra
# O cliente ganha o desconto
# se for estudante OU for terca
# E a sala for comum.

estudante = input("Você é estudante? ")
dia_da_semana = input("Que dia da semana é hoje? ")
sala = input("Que tipo de sala é?")

if estudante.lower() == "sim" or dia_da_semana.lower() == "terça" and sala.lower() == "comum":
   print("Valor Aplicado")
else:
   print("Valor Integral")