import csv #comma separated value
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat
import pandas as pd

d = pd.read_csv("______") ##ENTER THE FILE PATH ON THE EMPTY SPACE
dn = d[d["ID"]=="S1"] #Select the id S1 in d
temp = dn["Temperature water continous"]
ox = dn["Oxygen dissolved continous"]
print("mean of temp: ",np.mean(temp))
print("median of oxygen: ",np.median(ox))
temp.hist()
plt.title("HISTOGRAM")
plt.xlabel("Temperature water continous")
plt.show()