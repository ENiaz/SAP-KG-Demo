import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


Queries = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10"]
Datasets = ["Film", "Sport", "Person", "Drug", "Music", "History"]



array = np.array([[0.75, 0.92,0.59,0.89,0.85,0.42],
                    [1.0,0.84,0.89,0.52,0.95,0.93],
                    [1.0,0.99,0.72,0.8,0.85,0.6],
                    [0.82,0.77,0.87,0.92,1.0,0.64],
                    [0.84,0.79,0.98,0.75,0.89,0.91],
                    [0.9,0.76,0.88,0.7,0.75,0.87],
                    [0.86,0.8,1.0,0.74,0.64,0.96],
                    [0.67,0.89,0.88,0.78,0.68,0.7],
                    [0.76,0.95,0.86,0.61,0.87,0.8],
                    [0.73,0.92,0.82,0.75,0.98,0.87]])


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
plt.savefig('RecallBaseline.png', dpi=100)
plt.show()


