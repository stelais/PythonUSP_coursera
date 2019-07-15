def main():

	numero = int(input("Digite um número inteiro: "))

	def primo(number):

		i = 2
		result = 0 
		while i < number:
			if (number % i) == 0:
				result = result + 1
			i = i + 1
		return result		
	
	n_divisores = primo(numero)	

	if n_divisores == 0:
		print("primo")

	elif n_divisores > 0:
		print("não primo")

	else:
		print ("erro")
main()
