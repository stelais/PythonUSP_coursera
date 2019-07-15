def main():
	numero = int(input("Digite seu numero: "))

	def divisivel_5(number):
		resto = number % 5
		if resto == 0:
			print("Buzz")
		else:
			print(number)

	divisivel_5(numero)
main()			