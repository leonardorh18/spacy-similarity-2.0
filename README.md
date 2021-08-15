# spacy-similarity-2.0
Função para verificar similaridade entre duas listas de palavras em python

## COMO USAR 
Primeiramente é preciso ter a biblioteca do spacy instalada https://spacy.io

**Faça a importação da biblioteca do spacy**

import spacy

spacy.cli.download("en_core_web_lg")

nlp = spacy.load('en_core_web_lg')

**Faça a importação desse arquivo .py**

from spacysimilarity import SpacySimilarity 

**Como usar**

simi = SpacySimilarity(nlp)


simi.spacy_simi(lista1, lista1, probLista1, probLista2, include_prob = True, rank_matters = True)

**Por padrão, probLista1 e probLista2 são dicionarios vazios, caso queira incluir a probabilidade das palavras basta usar o metodo make_dict() para criar dicionario com a palavra
e a probabilidade:**

list1 = (lista com listas que contem palavras)

list2 = (lista com lsitas que contem palavras)

prob1 = (lista com listas que contem a probabilidade das palavras da list1, respectivamente)

prob2 = (lista com listas que contem a probabilidade das palavras da list2, respectivamente)

probLista1 = simi.make_dict(list1, prob1)

probLista2 = simi.make_dict(list2, prob2)

o parametro include_prob deve ser True para incluir as probabilidades

o metodo spacy_simi() retorna uma matriz Nx3 onde N é a quantidade de tópicos da primeira lista (list1)

[topico lista1, melhor "match" topico lista2, valor]






  

