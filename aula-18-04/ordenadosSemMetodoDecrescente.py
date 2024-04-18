# Inicializa uma lista chamada vet com 10 elementos, todos inicializados como zero.
vet = [0] * 10

# Loop para ler 10 números do usuário e armazená-los na lista vet.
for i in range(10):
    vet[i] = int(input(f'Número {i+1}: '))

# Imprime a lista vet lida.
print("Vetor lido:", vet)

# Loop para ordenar a lista vet em ordem crescente usando o algoritmo de seleção.
for i in range(0, 9, 1):
    maior = i
    # Loop interno para encontrar o menor elemento não ordenado.
    for j in range(i+1, 10, 1):
        if vet[j] > vet[maior]:
            maior = j
    # Troca o menor elemento encontrado com o elemento na posição atual do loop externo.
    aux = vet[i]
    vet[i] = vet[maior]
    vet[maior] = aux
    # Imprime a lista vet após cada passo do processo de ordenação.
    print(vet)

# Imprime a lista vet completamente ordenada.
print("Vetor ordenado: ", vet)
