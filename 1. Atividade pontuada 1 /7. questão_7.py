import os 
os.system("clear")

#Entrada
descricao_produto = (input("Digite o produto: "))
quantidade_adiquirida = int(input("Digite a quantidade adquirida: "))
preço_unitario = float(input("Digite o preço unitário: "))
total = quantidade_adiquirida * preço_unitario

#Processamento
if quantidade_adiquirida <= 5:
    desconto = 0.2 * total
elif quantidade_adiquirida > 10:
    desconto = 0.5 * total
else:
    quantidade_adiquirida > 5 and quantidade_adiquirida <= 10
    desconto = 0.3 * total
total_pagar = total - desconto
#Saída
print(f"DESCRIÇÃO DO PRODUTO: {descricao_produto}")
print(f"QUANTIDADE ADQUIRIDA: {quantidade_adiquirida}")
print(f"PREÇO UNITÁRIO: {preço_unitario:.2f}")
print(f"TOTAL: {total:.2f}")
print(f"DESCONTO: {desconto:.2f}")
print(f"TOTAL A PAGAR: {total_pagar:.2f}")
   




