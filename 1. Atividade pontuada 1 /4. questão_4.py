import os 
os.system("clear")

#Se o cliente comprar a partir de 10 Kg em frutas ou o valor total da compra ultrapassar R$ 15,00
#receberá ainda um desconto de 10% sobre este total.
#Escreva um algoritmo para ler a quantidade (em Kg) de morangos
#e a quantidade (em Kg) de maçãs adquiridas e escreva o valor a ser pago pelo cliente.

#Entrada
frutas = float(input("""
1. MORANGO
2. MAÇA


Digite uma opção:             
"""))

match frutas: 
    case 1: 
        quantidade_frutas = float(input("Digite a quantidade de MORANGO: "))
        if quantidade_frutas <= 5:
           valor_compra = quantidade_frutas * 2.50
           print(f"Valor da compra: {valor_compra}")
        elif quantidade_frutas >= 10:
             desconto = (quantidade_frutas * 2.20) * 0.1
             print(f"Valor da compra: {quantidade_frutas - desconto}")
        elif quantidade_frutas > 5: 
             valor_compra = quantidade_frutas * 2.20
             print(f"Valor da compra: {valor_compra}")
    case 2: 
        quantidade_frutas = float(input("Digite a quantidade de MAÇA: "))
        if quantidade_frutas <= 5:
           valor_compra = quantidade_frutas * 1.80
           print(f"Valor da compra: {valor_compra}")
        elif quantidade_frutas >= 10:
             desconto = (quantidade_frutas * 1.50) * 0.1
             print(f"Valor da compra: {quantidade_frutas - desconto}")
        elif quantidade_frutas > 5: 
             valor_compra = quantidade_frutas * 1.50
             print(f"Valor da compra: {valor_compra}")
   

              

            
            


