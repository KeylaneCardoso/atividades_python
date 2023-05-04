# Para identificar um número primo devemos dividi-lo sucessivamente por números primos como: 2, 3, 5. . . e verificar se a divisão é exata (em que o resto é zero)
# ou não exata (onde o resto é diferente de zero). Se o resto da divisão for zero o número não é primo. Se nenhum resto for zero, o número é primo.

n = int(input("Verificar números primos até: "))
lista_primos = []

for i in range(2, n+1):
    primo = True
    for j in range(2, int(i/2)+1):
        if i % j == 0:
            primo = False
            break
    if primo:
        lista_primos.append(i)

print(lista_primos)
print("O total de números primos foi de: " + str(len(lista_primos)))

#essa parte é para adicionar os numeros num arquivo de texto
with open('listaNumPrimos.txt', 'a') as arquivo:
    for numero in lista_primos:
        arquivo.write(str(numero) + '\n')
