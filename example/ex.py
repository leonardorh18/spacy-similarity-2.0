from spacysimilarity import SpacySimilarity 

import spacy
import pandas as pd
import numpy as np
import re
#spacy.cli.download("en_core_web_lg") YOU MUST DOWNLOAD IT
nlp = spacy.load('en_core_web_lg')

ex = pd.read_csv('example.csv')

t1 = ex.topicsOne
t2 = ex.topicsTwo

## just a quick pre-processing to separate words and probabilities

for line in range(len(t1)):
    t1[line] = re.sub('\[', '', t1[line])
    t1[line] = re.sub('\]', '', t1[line])
    t1[line] = re.sub('\(', '', t1[line])
    t1[line] = re.sub('\)', '', t1[line])
    t1[line] = re.sub("'", '', t1[line])
    t1[line] = re.sub(" ", '', t1[line])
for line in range(len(t2)):
    t2[line] = re.sub('\[', '', t2[line])
    t2[line] = re.sub('\]', '',t2[line])
    t2[line] = re.sub('\(', '',t2[line])
    t2[line] = re.sub('\)', '', t2[line])
    t2[line] = re.sub("'", '', t2[line])
    t2[line] = re.sub(" ", '', t2[line])

list1 = []
prob1 = []
for i in range(len(t1)):
    splt = t1[i].split(',')
    list1.append([splt[j] for j in range(0, len(splt), 2)])
    prob1.append([float(splt[j]) for j in range(1, len(splt), 2)])

list2 = []
prob2 = []
for i in range(len(t2)):
    splt = t2[i].split(',')
    list2.append([splt[j] for j in range(0, len(splt), 2)])
    prob2.append([float(splt[j]) for j in range(1, len(splt), 2)])

################## FINISH PRE-PROCESSING ########################

simi = SpacySimilarity(nlp)

probDict1 = simi.make_dict(list1, prob1)
probDict2 = simi.make_dict(list2, prob2)

matrix = simi.spacy_simi(list1, list2, probDict1, probDict2, include_prob = True, rank_matters = False)

for line in matrix:
    print('----------', line[2])
    print(list1[line[0]])
    print(list2[line[1]])


#### OR

print("\n\nWITHOUT PROB\n\n")

matrix = simi.spacy_simi(list1, list2, include_prob = False, rank_matters = False)
for line in matrix:
    print('----------', line[2])
    print(list1[line[0]])
    print(list2[line[1]])