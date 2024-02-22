print('Calculo de uma expressão matemática')
x = int(input("Insira um número: "))
y = int(input("Insira outro número: "))

z = (f'z =({x}**2+{y}**2)/({x}-{y})**2')
calc = (x**2+y**2)/(x-y)**2
print(f'A expressão',z,'é igual a:',calc)