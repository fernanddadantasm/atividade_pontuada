import os
os.system("clear")

#Faça um programa que leia um código de operação (+,-,* ou /) e também dois valores inteiros A e B
#O programa deve calcular o resultado da operação escolhida aplicado a A e B.
#Por exemplo, se a operação escolhida foi * e A = 1 e B = 3  
# o programa deve fornecer como resultado o valor de 1*3, que é 3.



#Entrada 
a = int(input("Digite um número: "))
operador = input("Digite a operação que deseja (+ - * /): ")
b = int(input("Digite um número: "))

#Processamento

match operador:
    case "+":
        resultado = a + b
        
    case "-":
        resultado = a - b
    case "*":
        resultado = a * b
    case "/":
        resultado = a / b
    case _:
        resultado = "Opção inválida."

#Saída
print (f"\nResultado: {resultado}")
