#impares ate n
def main():

	numero = int(input("Digite o valor de n: "))

	def impar(n):
		i = 1
		while i < n+1:
			print (2*i-1)
			i = i + 1 

	impar(numero)
main()			 
