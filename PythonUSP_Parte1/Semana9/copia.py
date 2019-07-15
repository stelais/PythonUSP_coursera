import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

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

def separando_todo_mundo_em_arrays(texto): 
    sentencas_array = []
    frases_sent = []     
    frases_array= []
    palavras_array = []

    sentencas = separa_sentencas(texto) 
    sentencas_array += sentencas
    j=0
    while j < len(sentencas):
        frases = separa_frases(sentencas[j])
        frases_sent.append(frases)
        k = 0
        while k < len(frases):          
            frases_array.append(frases[k])
            palavras = separa_palavras(frases[k])   
            l = 0
            while l < len(palavras):
                palavras_array.append(palavras[l])
                l += 1
            k += 1
        j += 1
    return sentencas_array, frases_sent, frases_array, palavras_array

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    similaridade = 0   
    for i in range(0,len(as_a)):
        valor = as_a[i] - as_b[i]
        if (valor < 0): 
            valor *= -1
        else:
            pass          
        similaridade += valor
    grau_de_similaridade = similaridade/len(as_a)        
    return grau_de_similaridade

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    sentencas_array, frases_sent, frases_array, palavras_array = separando_todo_mundo_em_arrays(texto)   
    
    #Cada argumento da assinatura
    wal = tamanho_medio_de_palavra(palavras_array)
    ttr = Type_Token(palavras_array) 
    hlr = Hapax_Legomana(palavras_array)
    sal = tamanho_medio_de_sentenca(sentencas_array)
    sac = complexidade_media_da_sentenca(frases_sent)  
    pal = tamanho_medio_de_frase(frases_array)
   
    return [wal, ttr, hlr, sal, sac, pal]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista_de_assinatura = []
    for texto in textos:
        n_assinatura = calcula_assinatura(texto)
        lista_de_assinatura.append(n_assinatura)
    lista_similaridade = []
    for i in range(0,len(lista_de_assinatura)):    
        grau_de_similaridade = compara_assinatura(lista_de_assinatura[i], ass_cp)    
        lista_similaridade.append(grau_de_similaridade)
    similaridade_copia = lista_similaridade[0]
    for i in range(0,(len(lista_similaridade)-1)):
        if similaridade_copia > lista_similaridade[i]:
            similaridade_copia = lista_similaridade[i]
            numero_copia = i+1
        else:
            pass    
    return numero_copia

def main():
    assinatura_modelo = le_assinatura()
    #assinatura_modelo = [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]
    textos = le_textos()

    texto_copia = avalia_textos(textos, assinatura_modelo)
    print("O autor do texto {} esta infectado com COH-PIAH".format(texto_copia))

main()  