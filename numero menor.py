n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

menor = n1

if menor > n2:
	menor = n2

if menor > n3:
	menor = n3

print ('Menor:  %d ' %menor)