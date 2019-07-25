# perfeitos.py

n = int(input('Digite o número a ser testado: '))
teste = 0
for i in range(1,n):
	if n % i == 0:
		teste=teste+i
	if teste == n:
		print(n, 'é um número perfeito')
	else:
		print(n, 'não é um número perfeito')
