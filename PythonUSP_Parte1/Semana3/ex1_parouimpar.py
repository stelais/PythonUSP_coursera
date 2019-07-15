def main():
	numero = float(input("Digite seu número: "))
	def par_ou_impar(number):
		resto = number % 2 
		if resto == 0: 
			print ("par")
		else:
			print("ímpar")			
	par_ou_impar(numero)
main()