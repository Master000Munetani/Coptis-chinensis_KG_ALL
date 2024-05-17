from MulticoreTSNE import MulticoreTSNE as TSNE

import pandas as pd
import numpy as np
import os
import csv

entity2id = {}
id2entity = {}
with open("C:/Users/15382/Downloads/entitiesR.tsv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', fieldnames=['id','entity'])
    for row_val in reader:
        id = row_val['id']
        entity = row_val['entity']

        entity2id[entity] = int(id)
        id2entity[int(id)] = entity

print("Number of entities: {}".format(len(entity2id)))


entity_emb = np.load("C:/Users/15382/Downloads/ALL_HuangLianDB_RESCAL_RESCAL_entity.npy")
print(entity_emb.shape)  

from matplotlib import cm
import matplotlib.pyplot as plt
from sklearn.utils import check_random_state
from MulticoreTSNE import MulticoreTSNE as TSNE


X_embedded = TSNE(n_components=2, n_jobs=40).fit_transform(entity_emb).T


#plt.savefig('entityation.png')

dataset_id = {}
for entity_name, i in entity2id.items():
    entity_key = entity_name.split('::')[0]
    if dataset_id.get(entity_key, None) is None:
        dataset_id[entity_key] = []
    dataset_id[entity_key].append(i)

p = cm.rainbow(int(255/2 * 1))
for key, val in dataset_id.items():
    val = np.asarray(val, dtype=int)

    plt.plot(X_embedded[0][val], X_embedded[1][val], '.', label=key)
    lgd = plt.legend(bbox_to_anchor=(1.0, 1.0))

plt.savefig('./finalPNG/TransR.png', bbox_extra_artists=(lgd,), bbox_inches='tight', format='png')

import pandas as pd
import numpy as np
import os
import csv

entity2id = {}
id2entity = {}
with open("C:/Users/15382/Downloads/entitiesR.tsv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', fieldnames=['id','entity'])
    for row_val in reader:
        id = row_val['id']
        entity = row_val['entity']

        entity2id[entity] = int(id)
        id2entity[int(id)] = entity

print("Number of entities: {}".format(len(entity2id)))


entity_emb = np.load("C:/Users/15382/Downloads/ALL_HuangLianDB_RESCAL_RESCAL_entity (1).npy")
print(entity_emb.shape)  

from matplotlib import cm
import matplotlib.pyplot as plt
from sklearn.utils import check_random_state
from MulticoreTSNE import MulticoreTSNE as TSNE


X_embedded = TSNE(n_components=2, n_jobs=40).fit_transform(entity_emb).T


#plt.savefig('entityation.png')

dataset_id = {}
for entity_name, i in entity2id.items():
    entity_key = entity_name.split('::')[0]
    if dataset_id.get(entity_key, None) is None:
        dataset_id[entity_key] = []
    dataset_id[entity_key].append(i)

p = cm.rainbow(int(255/2 * 1))
for key, val in dataset_id.items():
    val = np.asarray(val, dtype=int)

    plt.plot(X_embedded[0][val], X_embedded[1][val], '.', label=key)
    lgd = plt.legend(bbox_to_anchor=(1.0, 1.0))

plt.savefig('./finalPNG/TransR.png', bbox_extra_artists=(lgd,), bbox_inches='tight', format='png')
