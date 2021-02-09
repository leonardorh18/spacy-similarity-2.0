# spacy-similarity-2.0
Função para verificar similaridade entre duas listas de palavras em python

## COMO USAR 
Primeiramente é preciso ter a biblioteca do spacy instalada https://spacy.io

**Faça a importação da biblioteca do spacy**

import spacy

spacy.cli.download("en_core_web_lg")

nlp = spacy.load('en_core_web_lg')

**Faça a importação desse arquivo .py**

import spacySimilarityV2 as simi

**Como usar a função**
Você deve passar duas listas que contém listas de palavras, quanto mais palavras melhor o resultado

## EXEMPLO

list1 = [['car', 'truck', 'seat'], ['home', 'floor', 'stairs'], ['school', 'book', 'pencil']]

list2 = [['bike', 'gas', 'seat'], ['room', 'toilet', 'bed'], ['teacher', 'read','university']]

result = simi.spacy_simi(list1, list2, nlp, rank_matters = True, absolute_value = True)

_Seguindo a ordem,a função vai comparar a similaridade da primeira lista com da segunda e vai retornar uma lista com o indice correspondente da lista mais similar_

**Por exemplo (valores ficticios)**

Supondo que você passou duas listas para a função (list1 e list2) a função retorna uma lista (matriz) como essa [[0,1,0.05],[1, 1, 0.03],[2, 2, 0.04]]

pegando o primeiro indice, [0, 1, 0.05]

usando o exemplo, significa que a lista list1[0] teve similaridade de 0.05 com list2[1]

pegando o segundo indice, [1, 1, 0.03]

significa que a lista list1[1] teve similaridade de 0.03 com list2[1]

pegando o terceiro indice, [2, 2, 0.04]

significa que a lista list1[2] teve similaridade de 0.04 com list2[2]

_Quanto mais próximo de zero mais fraca é a similaridade e quanto maior que zero mais forte é a similaridade_

# Parametros

**rank_matters**: leva em consideração a posição da palavra para calcular a similaridade. _boolean_ (True ou False)

**absolute_value**: a função original do spacy em alguns casos retorna similaridade negativa, com isso, caso o valor seja **True**, valores negativos passarão a ser considerados em seu valor positivo. _boolean_ (True ou False)




  

