#n primos
def primo(number):
	i = 2
	result = 0 
	while i < number:
		if (number % i) == 0:
			result = result + 1
		i = i + 1
	if result == 0:
		return True	
	else:
		return False		

def n_primos(numero):
	resultado = 0
	while numero >= 2:
		if primo(numero):
			resultado += 1
		numero -= 1
	return resultado	



def main():
	numero = int(input("Digite um número inteiro: "))		
	print (n_primos(numero))

main()
