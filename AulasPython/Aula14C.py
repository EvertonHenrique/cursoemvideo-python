'''for c in range(1, 10):
    print(c)
print('Fim! ')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um núnero: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'Voce digitou {par} numeros PARES e {impar} numeros IMPARES ')