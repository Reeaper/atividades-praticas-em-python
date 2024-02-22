# def calc_media(lista):
def calc_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return media

nums = [1,2,3,4,5,6,7,8,9]
media = calc_media(nums)
print(nums)
print("A média dos valores é:", media)
