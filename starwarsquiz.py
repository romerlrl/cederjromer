'''
Algoritmo que fiz para praticar grafos e recursividade.
Baseado nisso: https://i.pinimg.com/564x/3f/e1/bb/3fe1bb5d42bd510aa7a1adfab897e560.jpg
'''

def abrequestao(num, vetor):
    if type(num) is tuple:   
        print(num[0])
        if len(num)-2:
            for i in range(1, len(num)):
                print(f"{i}. {(vetor[num[i]][0])}")
            entrada=int(input())
        else: entrada=1
        entrada=vetor[num[entrada]]
        abrequestao(entrada, vetor)
    else:
        print(num)
        return None


mapa =      [
    		#00	
			("Você se considera um rebelde?", 1, 2),

		#01	
			("PNC da sociedade!", 3),

		#02	
			("Eu peço permissão para ir ao banheiro", 4),

		#03	
			("Você pode lidar com o estresse de uma luta de sabres de luz?", 5, 6),

		#04	
			("Você pode dançar enquanto é apertado pelo pescoço?",7, 8, 9),

		#05	
			("Sem problemas, a Força... e calmantes são fortes na minha família", 32,

		#06	
			("Prefiro tocar dongo para o Jabba", 12),

		#07	
			("Eu nunca vou fazer isso de novo", 12),

		#08	
			("Essa pergunta me fez me sentir sujo e barato", 29),

		#09	
			("Eu chamo isso de uma terça feira típica", 33)

		#10	
			("Sim|O que você faria se Jar Jar começasse a forçar intimidade?", 17, 16),

		#11	
			("Eu sou um hippie paz e amor", 31),

		#12	
			("Você ficaria confortável matando a população de um planeta inteiro?", 30, 13),

		#13	
			("Só se eu puder usar um capacete bonito!", 29),

		#14	
			("Prefiro um uniforme", 27),

		#15	
			("Estou deboas e até aproveitaria o fresquinho", 28),

		#16	
			("Jogar essa mariposa estúpida em um campo de destroços e então cortá-lo ao meio com um sabre de luz", 23),

		#17	
			("Abraçá-lo", 24),

		#18	
			("Ooloo "*2, 24),

		#19	
			("Como desejar", 25),

		#20	
			("Não me importo com dinheiro", 26),

		#21	
			("Não, preciso esticar minhas pernas", 26),

		#22	
			("Definitivamente", 27),

		#23	
			("Aprendiz sith"),

		#24	
			("Chefe ewok"),

		#25	
			("Caçador de recompensa"),

		#26	
			("Cavaleiro Jedi"),

		#27	
			("Operador de Laser da Estrela da Morte"),

		#28	
			("Escrava do Jabba"),

		
			#Enxertos não previstos

		#29	
			("Você pode ficar sentado por muitas horas?", 26, 27),
		#30	
			("Não, not cool", 12),
		#31	
			("Você poderia capturar pessoas e aliens por dinheiro?", 15, 25, 26),
                #32
                        ("Você sofre com uma sede imensa de poder?", 10, 11),

                #33
                        ("Você se opõe a se vestir com lingerie espacial?", 14, 15),
]                                                

abrequestao(mapa[0], mapa)
