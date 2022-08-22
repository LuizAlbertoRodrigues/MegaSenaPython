#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Programa da Megasena
# created by Luiz Alberto 

import random
# gerando 6 números aleatórios inteiros de 1 a 60
print("*** Programa da Megasena ***")
print("Números sorteados de hoje: ")
for x in range(0, 6):
    # Números aleatórios inteiros na faixa desejada
    print(random.randint(1, 60))

