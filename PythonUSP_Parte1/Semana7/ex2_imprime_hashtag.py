def linha_inteira(largura):
	coluna = 1
	while coluna <= largura:
		print("#",end="")
		coluna += 1

def linha_vazia(largura):
	coluna = 1
	while coluna <= largura:	
		if coluna == 1 or coluna == largura:
			print("#",end="")
		else:
			print(" ",end="")
		coluna += 1	


def main():
	largura = int(input("digite a largura: "))
	altura = int(input("digite a altura: "))
	linha = 1
	while linha <= altura:
		if linha ==1 or linha==altura:
			linha_inteira(largura)
		else:
			linha_vazia(largura)
		print()	
		linha += 1
main()