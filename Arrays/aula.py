#inicailização de um array vazio
array = []

#laço for para inserção dos valores do array
for i in range(4):
    valor = int(input("Digite o valor n° {} do vetor \n".format(i+1)))
    array.append(valor)

#ordenar vetor em ordem crescente
array_ordenado = sorted(array)

#mostra o array completo
print(array_ordenado)

#mostra o maior valor do array 
print("O maior número é o", max(array_ordenado))
#mostra o menor valor do array
print("O menor número é o", min(array_ordenado))
