# spacy-similarity-2.0
Função para verificar similaridade entre duas listas da palavras em python

## COMO USAR 
Primeiramente é preciso ter a biblioteca do spacy instalada https://spacy.io

**Faça a importação da biblioteca do spacy**

import spacy

spacy.cli.download("en_core_web_lg")

nlp = spacy.load('en_core_web_lg')

**Faça a importação desse arquivo .py**

import spacySimilarityV2

**Como usar a função**

teste1 =[['car', 'motor', 'gas', 'bike', 'transit', 'carriage', 'jeep', 'loaner', 'backseat', 'truck'], ['home', 'family', 'mansion', 'toilet', 'living_room', 'room', 'attic', 'door', 'cabin']]

teste2 = [['room', 'restaurant', 'house', 'grill', 'wood', 'laundry', 'stove', 'cooking', 'closet', 'bed'],['gasoline' , 'engine', 'cart', 'volvo', 'motorcycle', 'driver', 'radiator', 'taxi', 'suzuki'], ]

medias = spacy_simi(teste1, teste2, nlp, rank_matters = True, absolute_value = True)

for l in medias:

  print(teste1[l[0]])
  
  print(teste2[l[1]])
  

