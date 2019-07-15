def primo(number):

	i = 2
	result = 0 
	while i < number:
		if (number % i) == 0:
			result = result + 1
		i = i + 1
	return result	
# if result = 0 ee primo
def maior_primo(numero):
	j = 2
	primos = []
	while j <= numero:
		n_divisores = primo(j)	

		if n_divisores == 0:
			primos.append(j)	
			#primo
		j = j+1	
	tamanho = len(primos)	
	return primos[tamanho-1]


def teste():
	numero = int(input("Digite um número inteiro: "))
	print(maior_primo(numero)	)

	
