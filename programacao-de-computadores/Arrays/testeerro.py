VetClasse = [0.0] * 10

Soma = 0
NotaAcima = 0

for X in range (10):
    VetClasse[X] = float(input(f'Nota {X+1}: '))

for X in range(10):
    Soma = Soma + VetClasse[X]

Media = Soma/10
for X in range(10):
    if VetClasse[X] >= Media:
        NotaAcima = NotaAcima + 1

print("A média das notas é: ", Media)
print("Número de notas acima da média: ", NotaAcima)
print("A maior nota é: ", max(VetClasse))
print("A menor nota é: ", min(VetClasse))

print(VetClasse)