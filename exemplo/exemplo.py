# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 22:11:20 2021

@author: leohe
"""
import pandas as pd
import spacy
spacy.cli.download("en_core_web_lg")
nlp = spacy.load('en_core_web_lg')

import spacysimilarityv2 as simi


## transforma o topico estraido do csv em uma lista de palavras
def process(docs):
  n_final = []
  for s in docs:
    n_final.append(["".join([w for w in s if w != '[' and w != ']' and w != ')' and w != '(' and w != "'" and w != " " ])])
  final = []
  for doc in n_final:
    aux = []
    for s in doc:
      #print(s)
      if (type(s) is float) == False: ## comparando pra ver se nao é NaN
        splt = s.split(",")
        for word in splt:
          # print(word)
          aux.append(word)
      final.append(aux)
  return final

ex1 = pd.read_csv('ex1.csv')
ex2 = pd.read_csv('ex2.csv')

ex1 = process(ex1.topicos)
ex2 = process(ex2.topicos)
  
result = simi.spacy_simi(ex1, ex2, nlp, rank_matters = True, absolute_value =  True)

for row in result:
    print(ex1[row[0]])
    print(ex2[row[1]])
    print('Valor: ', row[2])