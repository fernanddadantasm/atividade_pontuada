import os 
os.system("clear")

#Um posto está vendendo combustíveis com a seguinte tabela de descontos
#Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível 
#(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
#sabendo-se que o preço do litro da gasolina é R$ 6,59 e o preço do litro do álcool é R$ 3,79.

#Entrada
litros_vendidos = int(input("Digite a quantidade de litros: "))
tipo_combustivel = (input("""
A - álcool
G - gasolina                 

Digite uma opção:             
""")) .upper()
preco_alcool = 3.79
preco_gasolina = 6.59
preco_sem_desconto_a = litros_vendidos * preco_alcool
preco_sem_desconto_g = litros_vendidos * preco_gasolina
#Processamento
match tipo_combustivel:
    case "A":
        if litros_vendidos <= 25:
          desconto_alcool = (preco_sem_desconto_a) * 0.2 
          valor_pago = preco_sem_desconto_a - desconto_alcool
          print(f"O valor total é: {valor_pago:.2f}")
        elif litros_vendidos > 25: 
           desconto_alcool = (preco_sem_desconto_a) * 0.4
           valor_pago = preco_sem_desconto_a - desconto_alcool 
           print(f"O valor total é: {valor_pago:.2f}")     
    case "G":
        if litros_vendidos <= 25:
          desconto_gasolina = (preco_sem_desconto_g) * 0.3 
          valor_pago = preco_sem_desconto_g - desconto_gasolina
          print(f"O valor total é: {valor_pago:.2f}")
        elif litros_vendidos > 25: 
           desconto_gasolina = (preco_sem_desconto_g) * 0.5
           valor_pago = preco_sem_desconto_g - desconto_gasolina 
           print(f"O valor total é: {valor_pago:.2f}")     
            