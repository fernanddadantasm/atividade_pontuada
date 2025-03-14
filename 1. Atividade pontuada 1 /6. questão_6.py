import os 
os.system("clear")


primeira_nota = float(input("Digite  a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))


media = (primeira_nota + segunda_nota) / 2

if media >= 6:
    print(f"APROVADO, PARABÉNS!")
elif media  >= 4:
    print("RECUPERAÇÃO")
elif media < 4:
    print("REPROVADO!")