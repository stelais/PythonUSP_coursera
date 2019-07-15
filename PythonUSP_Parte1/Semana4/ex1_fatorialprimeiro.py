def main():
	numero = int(input("Digite o valor de n: "))

	def fatorial(n):
		resultado = 1
		if n != 0:
			i = n
			while i != 0:
				resultado = resultado * i
				i = i - 1	
		return resultado
	

	print(fatorial(numero))

main()				
