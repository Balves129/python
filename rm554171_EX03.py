
alunos_impares =[]
alunos_pares = []

print("Digite a nota dos alunos impares: ")
# Aqui criamos um for com +2 para contar apenas numeros impares
for i in range (1,50,2):
    #A variavel nota recebe um input para imprimir as notas, e esse input é trasnformado em float
    nota = float(input(f"aluno {i}: ")) # i é a variavel que assumira os dados: 1, 3, 5...47, 49
    alunos_impares.append(nota)
    
print("Digite a nota dos alunos pares: ")
for p in range(2,51,2):
    nota_par= float(input(f"aluno {p}: "))
    alunos_pares.append(nota_par)
    
media_impar = sum(alunos_impares)/len(alunos_impares)  
media_pares = sum(alunos_pares)/ len(alunos_pares)


if alunos_impares > alunos_pares:
    print(f"Alunos impares tiveram uma média maior: {media_impar}",round(nota))
else:
    print(f"Alunos pares tiveram uma média maior: {media_pares}",round(nota))