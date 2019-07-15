def multiplo(dividendo,divisor):
	""" Se n é múltiplo de (m+1), o computador deve ser "generoso"
	essa função retorna o resto de n dividido por m+1
	"""
	return (dividendo%divisor)

def computador_escolhe_jogada(n,m):
	"""Uma função computador_escolhe_jogada que recebe, como parâmetros, 
	os números n e m descritos acima e devolve um inteiro correspondente 
	à próxima jogada do computador de acordo com a estratégia vencedora.
	""" 
	resto = multiplo(n,m+1)
	if n <= m:
		pecas_depois = n
	
	elif resto>0:
		pecas_depois = resto
	else:
		pecas_depois = m	
		
	if pecas_depois == 1:
		print("\nO computador tirou uma peça.")
	else:
		print("\nO computador tirou",pecas_depois,"peças.")
	return pecas_depois		

def pecas_disponiveis_texto(pecas_disponivel):
	if pecas_disponivel != 1 and pecas_disponivel !=0:
		print("Agora restam", pecas_disponivel ,"peças no tabuleiro.")
	elif pecas_disponivel == 1:
		print("Agora resta apenas uma peça no tabuleiro.")	
	elif pecas_disponivel ==0:
		print("Fim do jogo! O computador ganhou!")	
	return None	

def usuario_escolhe_jogada(n,m):
	"""Uma função usuario_escolhe_jogada que recebe os mesmos parâmetros, 
	solicita que o jogador informe sua jogada e verifica se o valor informado é válido. 
	Se o valor informado for válido, a função deve devolvê-lo; caso contrário, 
	deve solicitar novamente ao usuário que informe uma jogada válida.

	"""  
	pecas = int(input("\nQuantas peças você vai tirar? "))

	while (pecas > m) or (pecas > n) or (pecas<=0):
		print("\nOops! Jogada inválida! Tente de novo.")
		pecas = int(input("\nQuantas peças você vai tirar? "))
	if pecas == 1:
		print("\nVocê tirou uma peça.")
	else:
		print("\nVocê tirou",pecas,"peças.")
	return pecas


def partida():
	"""Uma função partida que não recebe nenhum parâmetro, 
	solicita ao usuário que informe os valores de n e m e inicia o jogo, 
	alternando entre jogadas do computador e do usuário 
	(ou seja, chamadas às duas funções anteriores). 
	A escolha da jogada inicial deve ser feita em função 
	da estratégia vencedora, como dito anteriormente. 
	A cada jogada, deve ser impresso na tela o estado atual do jogo, 
	ou seja, quantas peças foram removidas na última jogada e quantas 
	restam na mesa. Quando a última peça é removida, essa função imprime 
	na tela a mensagem "O computador ganhou!" ou "Você ganhou!" conforme o caso.  
	"""
	n = int(input("\nQuantas peças? "))
	m = int(input("Limite de peças por jogada? "))
	resto = multiplo(n,m+1)
	if resto == 0:         
		print("\nVocê começa!")

	else:
		print("\nComputador começa!")   

	pecas_disponivel = n
	while pecas_disponivel > 0: 
		if resto == 0:  
			pecas = usuario_escolhe_jogada(pecas_disponivel,m)  
			pecas_disponivel = pecas_disponivel - pecas
			pecas_disponiveis_texto(pecas_disponivel)	
		 
			pecas_depois = computador_escolhe_jogada(pecas_disponivel,m)
			pecas_disponivel = pecas_disponivel - pecas_depois			
			pecas_disponiveis_texto(pecas_disponivel)	
	
		else:
			pecas = computador_escolhe_jogada(pecas_disponivel,m)  
			pecas_disponivel = pecas_disponivel - pecas
			pecas_disponiveis_texto(pecas_disponivel)	
			
			if pecas_disponivel != 0:
				pecas_depois = usuario_escolhe_jogada(pecas_disponivel,m)
				pecas_disponivel = pecas_disponivel - pecas_depois			
				pecas_disponiveis_texto(pecas_disponivel)	   			    						 
	return None

def campeonato():
	"""
	Como todos sabemos, uma única rodada de um jogo não é suficiente para definir 
	quem é o melhor jogador. Assim, uma vez que a função partida esteja funcionando,
	você deverá criar uma outra função chamada campeonato. Essa nova função deve 
	realizar três partidas seguidas do jogo e, ao final, mostrar o placar dessas três 
	partidas e indicar o vencedor do campeonato. O placar deve ser impresso na forma
	Placar: Você ??? X ??? Computador
	"""
	for i in range(1,4):
		print("\n**** Rodada ",i," ****")
		partida()
	#fazer tres vezes aqui e somar
	print ("\n**** Final do campeonato! **** \n \nPlacar: Você 0 X 3 Computador")
	return None


def main():
	modo = 0
	while modo != 1 and modo != 2:
		print("\nBem-vindo ao jogo do NIM! Escolha: \n")

		modo = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
		if modo == 1:
			print("\nVocê escolheu uma partida isolada!")
			partida()
		if modo == 2:
			print("\nVocê escolheu um campeonato!")
			campeonato()	
	return None		

main()    	
