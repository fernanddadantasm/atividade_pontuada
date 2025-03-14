import os
os.system("clear")

#Em uma loja de CD´s existem apenas quatro tipos de preços que estão associados a cores. 
#Assim os CD´s que ficam na loja não são marcados por preços e sim por cores.
#Desenvolva o algoritmo que a partir da entrada da cor o software mostre o preço.
#A loja está atualmente com a seguinte tabela de preços. 


#Entrada
cor = input ("Digite a cor do CD: ")
#Processamento
match cor:
    case "Verde":
        preco_cd = 10.00
        print(f"O preço do CD é R$10,00")
    case "Azul":
        preco_cd = 20.00
        print(f"O preço do CD é R$20,00")  
    case "Amarelo":
        preco_cd = 30.00
        print(f"O preço do CD é R$30,00")    
    case "Vermelho":
        preco_cd = 40.00
        print(f"O preço do CD é R$40,00")
    case _:
        print(f"A cor digita foi inválida")    
