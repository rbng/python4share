import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

N = 1000
idcli = map(str.__add__,['ID']*N, np.array(range(N), str))
age = np.random.randint(20,80,N)
geo = np.array(np.random.randint(1,9,N), str)

geo_value = ['1', '2', '3', '4', '5', '6', '7', '8']
geo_area = ['N', 'E', 'S', 'W', 'NE', 'SE', 'SW', 'NW']

for j in range(len(geo_value)):
    geo[geo == geo_value[j]] = geo_area[j]

ctv = np.array(np.random.normal(100000,30000,N), int)
ctv[ctv <= 0] = np.random.randint(1,100000,1)
ninstr = np.array(np.random.normal(20,8,N), int)
ninstr[ninstr <= 0] = np.random.randint(1,30,1)

df = pd.DataFrame({'ID': idcli, 'AGE': age, 'GEO': geo, 'N_INSTR': ninstr, 'AMOUNT': ctv})
