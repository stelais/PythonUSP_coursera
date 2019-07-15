def main():
	import math

	a = float(input("digite seu primeiro x: "))
	b = float(input("digite seu primeiro y: "))
	c = float(input("digite seu segundo x: "))
	d = float(input("digite seu segundo y: "))	

	def distancia(x1,y1,x2,y2):
		dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
		return dist
	
	distance = distancia(a,b,c,d)

	if distance >= 10:
		print("longe")
	else:
		print("perto")		

main()	