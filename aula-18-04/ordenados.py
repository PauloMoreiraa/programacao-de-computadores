vet = [0] * 10
for i in range(10):
    vet[i] = int(input(f'Número {i+1}: '))
print("Vetor lido:", vet)
vetord = sorted(vet)
print("Vetor ordenado: ", vetord)