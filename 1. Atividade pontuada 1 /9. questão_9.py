import os 
os.system("clear")

#Uma financeira usa o seguinte critério para conceder empréstimos
#o valor total do empréstimo deve ser até dez vezes o valor da renda mensal do solicitante
#e o valor da prestação deve ser no máximo 30% da renda mensal do solicitante
#Escreva um programa que leia a renda mensal de um solicitante, o valor total do empréstimo solicitado
#e o número de prestações que o solicitante deseja pagar e informe se o empréstimo pode 
# ou não ser concedido.



#Entrada 
renda_mensal = float(input("Digite o valor da sua renda mensal: "))
valor_total_emprestimo = float(input("Digite o valor do empréstimo: "))
numero_prestacoes = int(input("Digite o numero de prestações que deseja pagar: "))

condicao_emprestimo = 10 * renda_mensal
valor_prestacao =  valor_total_emprestimo / numero_prestacoes
condicao_prestacao = 0.3 * renda_mensal

#Processamento
if valor_total_emprestimo <= condicao_emprestimo and valor_prestacao <= condicao_prestacao: 
    print(f"Emprestimo concedido!")
else:
    print(f"Emprestimo não concedido!")





