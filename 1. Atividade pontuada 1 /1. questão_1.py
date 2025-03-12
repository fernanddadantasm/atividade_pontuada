import os
os.system("clear")


#Faça um algoritmo que leia os valores A, B, C 
#e imprima na tela se a soma de A + B é menor que C
#caso contrário, imprima que a A + B é maior que C. 

#ENTRADA
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
soma = a + b 


#PROCESSAMENTO

if soma < c: 
    print(f" A + B É MENOR QUE C")
elif soma > c:
    print(f" A + B É MAIOR QUE C")
else:
    print(f"Opção inválida!")


