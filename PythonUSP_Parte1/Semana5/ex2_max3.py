def maximo(a,b,c):
	if a > b:
		if a > c:
			return a
		else:
			return c	
	else:
		if b >c:
			return b
		else:
			return c


def teste_maximo():
	num1= int(input("qual seu num1? "))
	num2 = int(input("qual seu num2? "))
	num3 = int(input("qual seu num3? "))
	print(maximo(num1, num2,num3))
