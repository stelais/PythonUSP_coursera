def minha():

	n = int(input("Digite um numero inteiro >1: "))

	fator = 2
	multiplicidade = 0

	while n>1:
		while n % fator == 0:
			multiplicidade += 1
			n = n/fator	
		#print("fator: ",fator, "multiplicidade", multiplicidade)	
			print(fator," *",end=" ")
		fator += 1
		multiplicidade = 0

def dele():
	n = int(input("Digite um numero inteiro >1: "))

	fator = 2
	multiplicidade = 0

	while n>1:
		while n % fator == 0:
			multiplicidade += 1
			n = n/fator
		if multiplicidade >0:		
			print("fator: ",fator, "multiplicidade", multiplicidade)	
		fator += 1
		multiplicidade = 0	

dele()			