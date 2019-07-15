def tabuada():
    tab = 1
    while tab <= 10:
        print("Tabuada do", tab, ":", end="\t")
        i = 1
        while i <= 10:
            print(tab*i, end = "\t")
            i = i + 1
        print()
        tab = tab + 1
def tabuada2():
    tab = 1
    while tab <= 10:
        i = 1
        while i <= 10:
            print(tab,"x",i,"=",tab*i)
            i = i + 1
        print()
        tab = tab + 1
def tabuada3():
    tab = 0
    while tab < 10:
        tab = tab + 1
        i = 0
        while i < 10:
            i = i + 1
            print(tab,"x",i,"=",tab*i)
        print()

#5 e 4 nao funcionam
def tabuada4():
    tab = 1
    i = 1
    while tab <= 10 and i <= 10:
        print(tab,"x",i,"=",tab*i)
        i = i + 1
        tab = tab + 1
    print()

def tabuada5():
    tab = 1
    while tab <= 10:
        print("Tabuada do", tab, ":", end="\t")
        i = 1
        print(tab*i, end = "\t")
        i = i + 1
        print()
        tab = tab + 1    


def infinito():
	x = 2
	cont = 0
	while x >= 0:
	    y = 0
	    while y <= 4:
	        print("oi")#comando qualquer
	        y = y - 1
	    x = x - 1 
def exp():
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            print("\n",i,j,"\n")
            print(3 * i + j+1, end=" ")
            j = j + 1
        i = i + 1
def main():
	x = 1
	while x < 3:
	    y = 1
	    while y < 3:
	        print(x*y, end = "\t")
	        y = y + 1
	    x = x + 1



main()	     