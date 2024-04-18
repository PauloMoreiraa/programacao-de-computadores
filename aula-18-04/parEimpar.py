vetLido = [0] * 10
vetPar = [0] * 10
vetImpar = [0] * 10

for x in range(10):
    vetLido[x] = int(input(f'Número {x + 1}: \n'))

p=0
i=0

for x in range(10):
    if vetLido[x] % 2 == 0:
        vetPar[p] = vetLido[x]
        p += 1
    else:
        vetImpar[i] = vetLido[x]
        i += 1
print(f'Vetor lido: {vetLido}')
print(f'Vetor par, tamanho {p}: {vetPar[0:p]}')
print(f'Vetor ímpar, tamanho {i}: {vetImpar[0:i]}')
