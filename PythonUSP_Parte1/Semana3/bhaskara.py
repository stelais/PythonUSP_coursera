import math

def main():

	a = float(input("qual seu a? "))
	b = float(input("qual seu b? "))
	c = float(input("qual seu c? "))

	def bhaskara(a,b,c):
		#a*(x**2) + b*x + c = 0
		delta = b**2 - 4*a*c
		print ("delta:", delta)
		if delta > 0 :
			print("raizes reais")
			xmais = ((-b) + math.sqrt(delta))/(2*a)
			xmenos = ((-b) - math.sqrt(delta))/(2*a)	
		elif delta == 0 :	
			print("uma raiz real e única")
			xmais = ((-b) + math.sqrt(delta))/(2*a)
			xmenos = ((-b) - math.sqrt(delta))/(2*a)
		else:
			print("raizes complexas")	
			xmais = ((-b) + (math.sqrt(delta*(-1))*1j))/(2*a)
			xmenos = ((-b) - (math.sqrt(delta*(-1))*1j))/(2*a)
		return xmais, xmenos

	raiz1, raiz2 = bhaskara(a,b,c)
	print ("As raízes da sua equação são:", raiz1,"e",raiz2)		
main()	