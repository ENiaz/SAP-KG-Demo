import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


Queries = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10"]
Datasets = ["Film", "Sport", "Person", "Drug", "Music", "History"]



array = np.array([[0.69, 0.98,0.57,1.0,1.0,0.45],
                    [0.97,1.0,1.0,0.64,1.0,1.0],
                    [1.0,1.0,0.78,0.86,0.95,0.64],
                    [0.8,0.87,1.0,0.97,0.99,0.78],
                    [0.95,0.89,1.0,0.74,0.96,0.99],
                    [0.97,0.8,0.85,0.74,0.86,0.97],
                    [1.0,0.84,0.98,0.82,0.99,1.0],
                    [0.88,0.99,0.86,0.97,0.8,0.79],
                    [0.86,0.94,0.97,0.67,1.0,0.86],
                    [0.93,0.96,0.89,0.83,1.0,0.95]])

sns.set(font_scale=1.6)
cmap = sns.cm.rocket_r
ax = sns.heatmap(array, cmap = 'cividis_r', linewidth=0.5, annot=array)
im = ax.imshow(array)


ax.set_xticks(np.arange(len(Datasets))+0.5)
ax.set_yticks(np.arange(len(Queries))+0.5)

ax.set_xticklabels(Datasets)
ax.set_yticklabels(Queries)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

plt.setp(ax.get_yticklabels(), rotation=0,
         rotation_mode="anchor")
# ax.set_title("")

fig = plt.gcf()
fig.set_size_inches(20.5, 14.5)

plt.title('Recall')
plt.savefig('RecallSAPKG.png', dpi=100)
plt.show()


