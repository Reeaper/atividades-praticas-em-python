print("Calculo da média")

n1 = int(input('Insira a nota do primeiro semestre: '))
n2 = int(input('Insira a nota do segundo semestre: '))

print("Calculando")
media=(n1+n2)/2
print("Nota final:",media)

if media > 6:
    print('Aluno Aprovado')
elif media >=4 and media <=5:
    print("Aluno terá que fazer exame de recuperação")
else:
    print('Aluno Reprovado')