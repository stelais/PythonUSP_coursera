def main():
    numero = 1
    lista=[]
    while numero != 0:
        numero = int(input("Digite um número: "))
        lista.append(numero)
    
    index = len(lista)
    while index > 1:
    	print(lista[index-2])
    	index -= 1

main()    	
        

