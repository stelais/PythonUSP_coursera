#numeros adjacentes iguais?
def main():

	numero = int(input("Digite um número inteiro: "))
	num_str = str(numero)
	tam = len(num_str)

	def separando_em_vetor(number, tamanho):
		potencia = (tamanho - 1)
		a_dividir = numero
		array = []
		while potencia > -1:
			digito = a_dividir // (10**potencia)
			a_dividir = numero % (10**potencia)
			array.append(digito)
			digito = a_dividir
			potencia = potencia - 1
		return array
	
	def adjacente(vetor, tamanho):
		result = 0
		i = 0
		while i < tamanho-1:
			if vetor[i] == vetor[(i + 1)]:
				result = result + 1
			i = i + 1	
		return result		

	numeros_em_vetor = separando_em_vetor(numero, tam)

	if adjacente(numeros_em_vetor,tam) == 0:
		print("não")
	else:
		print("sim")	
	
main()		
