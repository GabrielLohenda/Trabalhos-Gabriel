
notas={}

qtd_estudantes=int(input("Digite a quantidade de estudantes que desejas registar:"))

for x in range(1, qtd_estudantes+1):
    print(f"Estudante N:{x}")
    nome=input("digite o nome: ")
    qtd_disciplina=int(input("Digite a quantidade de disciplina:"))
    lista_notas=[]

    for y in range(1, qtd_disciplina+1):
        nota=float(input(f"Nota {y}: "))
        lista_notas.append(nota)

    notas[nome]=lista_notas


#Iterando sobre um dicionario
for nome, notas in notas.items():
    print(f"{nome}: {notas}")



    #Gabriel Lohenda


