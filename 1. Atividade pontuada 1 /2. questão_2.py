import os
os.system("clear")


#Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. 
#Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos). 
#Por fim, mostre os dados do usuário.

#ENTRADA
nome = (input("Digite seu nome: "))
sexo = (input("""

F = Femnino 
M = Masulino
Digite seu sexo: 
""")).upper()
estado_civil = (input("Digite seu estado civil: ")) 


#PROCESSAMENTO

if sexo == "F" and estado_civil == "Casada":
    tempo_casada = int(input("Digite o tempo de casada em anos:  "))
    print(f"Nome: {nome}" )
    print(f"Sexo: {sexo}")
    print(f"Estado civil: {estado_civil}")
    print(f"Tempo de casada: {tempo_casada}")
else:
    print(f"Nome: {nome}" )
    print(f"Sexo: {sexo}")
    print(f"Estado civil: {estado_civil}")






    









#SAÍDA


