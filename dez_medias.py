def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

# Lista para armazenar as notas do aluno
notas_aluno = []

# Loop para solicitar as notas
for i in range(1, 11):
    nota = float(input(f"Digite a nota {i}: "))
    notas_aluno.append(nota)

# Calcular a média das notas
media = calcular_media(notas_aluno)

# Imprimir a média
print(f"Média Final: {media}")
if media > 6:
    print('Aluno Aprovado')
elif media >=4 and media <=5:
    print("Aluno terá que fazer exame de recuperação")
else:
    print('Aluno Reprovado')
