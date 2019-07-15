def main():
	numero = int(input("Digite seu numero: "))

	def divisivel_3(number):
		resto = number % 3
		if resto == 0:
			print("Fizz")
		else:
			print(number)

	divisivel_3(numero)
main()			