VetLido = [0.0] * 10
VetDes = [0.0] * 10

for X in range(10):
    VetLido[X] = float(input(f'Valor {X+1}: '))

MediaLido = sum(VetLido)/10

for X in range(10):
    VetDes[X] = abs(VetLido[X] - MediaLido)

MediaDes = sum(VetDes)/10

print(f'Média aritmética: {MediaLido:.2f}' )
print(f'Desvio médio absoluto: {MediaDes:.2f}')
