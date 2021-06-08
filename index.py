# buscar o texto 
texto_tmp = open('./computacao.txt', mode="r", encoding="utf-8")
texto, palavras,s_palavras, quantidade = '', '',[],[]

## lendo texto e guardando na variavel texto
for i in texto_tmp:
	texto += i
## tratando o texto armazenado na mesma variavel 
texto = texto.upper().replace('\n', '').replace('.', '').replace(',', '') # removendo espaços, virgulas e espaçadores como \n , e tranasformando o texto em caixa alta

# separa as palavras por espaço
## guardando as palavras, separando o texto tratado por espaços
palavras = texto.split(' ')
		
# guardar as palavras unicamente em uma lista
for i in palavras:
	if i not in s_palavras:
		s_palavras.append(i)
# comparar palavras com o texto contar e armazenar na variavel qtd
for i in s_palavras:
	quantidade.append(texto.count(i))

# iniciando variacel que ira guardar a concatenação entre as palavras e as quantidades
sd = []

from operator import itemgetter
# tratando os dados
for d in range(len(s_palavras)):
	sd.append((s_palavras[d],quantidade[d]))

# ordenando a lista de acordo com a quantidade
tmp = sorted(sd, key=itemgetter(1), reverse=True)

# mostrando os tops no range definido abaixo
for i in range(0,100):
	print('{} {}: {}'.format('Top:', i+1 , tmp[i][0]))

""" for k,v in sd[].items():
	print(k)
	print(v)
 """

