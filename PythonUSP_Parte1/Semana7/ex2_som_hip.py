#soma hipotenusa
def inteiro(n):
    return n % 1 == 0

def é_hipotenusa(x):
	import math
	i=1
	hipotenusas=[]
	while i < x:
		j = 1
		while j < x:
			hipotenusa = math.sqrt(j*j + i*i)
			if inteiro(hipotenusa):
				hipotenusas.append(hipotenusa)
			j += 1
		i += 1
	if x in hipotenusas:
		return True
	else:
		return False

def soma_hipotenusas(numero):
	count = numero
	soma = 0
	while count > 0:
		if é_hipotenusa(count):
			soma = soma + count
		else:
			pass
		count -= 1		
	return soma	
			


#def main():
#	numero = int(input("numero: "))
#	print(soma_hipotenusas(numero))
#main()
