import os 
os.system("clear")

#Faça um algoritmo que leia dois valores inteiros A e B 
#se os valores forem iguais deverá se somar os dois,caso contrário multiplique A por B. 
#Ao final de qualquer um dos cálculos deve-se atribuir 
# o resultado para uma variável C e mostrar seu conteúdo na tela.

a = int(input("Digite um número: "))
b = int(input("Digite o segundo número: "))

if a == b:
   c = a + b
   print(f"C: {c}")
else:
   c = a * b
   print(f"C: {c}")    
