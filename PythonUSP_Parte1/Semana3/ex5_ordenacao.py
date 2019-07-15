def main():
	a = int(input("Digite seu primeiro número: "))
	b = int(input("Digite seu segundo número: "))
	c = int(input("Digite seu terceiro número: "))
	def ordem(num1, num2, num3):
		if num1 <= num2 and num2 <= num3:
			print("crescente")
		else:
			print("não está em ordem crescente")	
	ordem(a,b,c)		
main()	