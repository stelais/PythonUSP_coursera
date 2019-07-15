########
import re

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)
#####

def main():
	#salva textos como arrays
	textos = le_textos()
	i=0	
	sentencas_array = {}
	frases_sent = {}
	frases_array = {}
	palavras_array = {}
	while i < len(textos):
		print(textos[i])
		sentencas_array[i] = []
		frases_sent[i] = []		
		frases_array[i] = []
		palavras_array[i] = []

		sentencas = separa_sentencas(textos[i])	
		sentencas_array[i] += sentencas
		j=0
		while j < len(sentencas):
			print(sentencas[j])
			frases = separa_frases(sentencas[j])
			frases_sent[i].append(frases)
			k = 0
			while k < len(frases):			
				frases_array[i].append(frases[k])
				print(frases[k])
				palavras = separa_palavras(frases[k])	
				l = 0
				while l < len(palavras):
					palavras_array[i].append(palavras[l])
					print(palavras[l])
					l += 1
				k += 1
			j += 1
		i += 1
	print ('fim',textos)
	print(sentencas_array, frases_sent, frases_array, palavras_array)
	return sentencas_array, frases_sent, frases_array, palavras_array
def tamanho_medio_de_palavra(palavras_array):
	total_de_caracteres = 0
	for i in palavras_array:
		caracteres = len(i)
		total_de_caracteres += caracteres
	media = total_de_caracteres/len(palavras_array)    
	return media
def Type_Token(palavras_array):
	numero_diferentes = n_palavras_diferentes(palavras_array)
	tt = numero_diferentes/len(palavras_array)
	return tt
def Hapax_Legomana(palavras_array):
	numero_unicas = n_palavras_unicas(palavras_array)
	hl = numero_unicas/len(palavras_array)
	return hl
def tamanho_medio_de_sentenca(sentencas_array):
	total_de_caracteres = 0
	for i in sentencas_array:
		caracteres = len(i)		
		total_de_caracteres += caracteres	
	media = total_de_caracteres/len(sentencas_array)    
	return media
def complexidade_media_da_sentenca(frases_sent):
	total_de_frases = 0
	for i in frases_sent:
		frases = len(i)		
		total_de_frases += frases	
	media = total_de_frases/len(frases_sent)    
	return media
def tamanho_medio_de_frase(frases_array):
	total_de_caracteres = 0
	for i in frases_array:
		caracteres = len(i)	
		total_de_caracteres += caracteres	
	media = total_de_caracteres/len(frases_array)    
	return media

sentencas_array, frases_sent, frases_array, palavras_array = main()
print('tamanhao medio palavra',tamanho_medio_de_palavra(palavras_array[0]))
print('tamanhao medio sentenca',tamanho_medio_de_sentenca(sentencas_array[0]))
print('tamanhao medio frase',tamanho_medio_de_frase(frases_array[0]))
print('cimplexidade', complexidade_media_da_sentenca(frases_sent[0]))
print('tt', Type_Token(palavras_array[0]))
print('hl', Hapax_Legomana(palavras_array[0]))
