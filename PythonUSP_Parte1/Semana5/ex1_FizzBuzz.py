def fizzbuzz(number):	
	resto1 = number % 3
	resto2 = number % 5
	if resto1 == 0 and resto2 == 0:
		return "FizzBuzz"
	elif resto1 == 0:
		return "Fizz"
	elif resto2 == 0:
		return "Buzz"
	else:
		return number

def teste():
	numero = int(input("Digite seu numero: "))	
	fizzbuzz(numero)
