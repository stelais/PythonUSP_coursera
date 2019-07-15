#Fatorial loop com dois while
n = 1 
while n>=0:
	n = int(input("Digite um numero inteiro positivo: "))
	fatorial = 1
	while n >1:
		fatorial = fatorial * n
		n -= 1
	print(fatorial)	