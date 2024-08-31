import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


Queries = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10"]
Datasets = ["Film", "Sport", "Person", "Drug", "Music", "History"]



array = np.array([[1.0, 0.98,1.0,0.84,1.0,1.0],
                    [0.89,1.0,1.0,0.75,1.0,1.0],
                    [1.0,1.0,1.0,0.76,0.97,0.98],
                    [0.54,1.0,0.85,1.0,0.82,0.66],
                    [1.0,0.86,0.97,0.56,1.0,0.88],
                    [0.83,0.62,0.99,0.76,1.0,0.97],
                    [0.99,0.99,0.85,0.49,0.84,1.0],
                    [0.99,0.87,1.0,0.84,0.77,0.99],
                    [0.84,1.0,1.0,0.89,1.0,0.8],
                    [1.0,0.73,1.0,0.57,1.0,0.97]])

sns.set(font_scale=1.6)
cmap = sns.cm.rocket_r
ax = sns.heatmap(array, cmap = 'YlGnBu', linewidth=0.5, annot=array)
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

plt.title('Precision')
plt.savefig('PrecisionSAPKG.jpg', dpi=100)


