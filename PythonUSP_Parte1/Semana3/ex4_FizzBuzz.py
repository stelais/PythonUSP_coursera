def main():
	numero = int(input("Digite seu numero: "))

	def divisivel(number):
		resto1 = number % 3
		resto2 = number % 5
		if resto1 == 0 and resto2 == 0:
			print("FizzBuzz")
		else:
			print(number)

	divisivel(numero)

main()			