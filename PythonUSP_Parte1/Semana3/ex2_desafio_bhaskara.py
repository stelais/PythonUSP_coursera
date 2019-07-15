import math

def main():

	a = float(input("qual seu a? "))
	b = float(input("qual seu b? "))
	c = float(input("qual seu c? "))

	def bhaskara(a,b,c):
		#a*(x**2) + b*x + c = 0
		delta = b**2 - 4*a*c
		if delta > 0 :
			xmais = ((-b) + math.sqrt(delta))/(2*a)
			xmenos = ((-b) - math.sqrt(delta))/(2*a)
			print("as raízes da equação são",xmenos, "e",xmais)
	
		elif delta == 0 :	
			x = ((-b) + math.sqrt(delta))/(2*a)			
			print("a raiz desta equação é", x)

		else:
			print("esta equação não possui raízes reais")	

	bhaskara(a,b,c)
	
main()	