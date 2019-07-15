#Soma dos numeros nas casas, centenas, dezenas, unidade, etc
def main():
	entrada = int(input("Digite um número inteiro: "))
	ent_str = str(entrada)
	tam = len(ent_str)
	def somando_unidades(numero, tamanho):
		potencia = tamanho
		soma = 0 
		a_dividir = numero
		while potencia > -1:
			a_somar = a_dividir // (10**potencia)
			a_dividir = numero % (10**potencia)
			soma = soma + a_somar
			a_somar = a_dividir
			potencia = potencia - 1
		return 	soma
	print (somando_unidades(entrada, tam))
main()
