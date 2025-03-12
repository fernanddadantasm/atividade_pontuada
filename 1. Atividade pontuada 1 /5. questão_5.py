import os
os.system("clear")


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
