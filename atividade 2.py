
#Objetivo: Criar um programa que printe os numeros de uma lista e, depois, eles multiplicados por 2
#Bonus: Colocar os numeros multiplicados em uma outra lista e printa-la

lista = [2, 3, 7, 12, 2]
lista_multiplicada = []

for i in range(len(lista)):
    valor = lista[i]
    dobro = valor * 2
    lista_multiplicada.append(dobro)
    print(f"O {i+1}º valor da lista é {valor} e seu dobro é {dobro}")


print("Lista multiplicada:")
for valor in lista_multiplicada:
    print(valor)
