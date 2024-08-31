import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



avocado = pd.read_csv("Percentile.csv")["SimilarityValue"]
# avocado = pd.read_csv("q.csv")["support"]

p = np.percentile(avocado, 95) # return 95th percentile, e.g median.
print (p)



fig, ax = plt.subplots(figsize = (6,4))

# Plot
    # Plot histogram
avocado.plot(kind = "hist", density = True, alpha = 0.65, bins = 15, color='darkcyan') # change density to true, because KDE uses density
    # Plot KDE
avocado.plot(kind = "kde")

    # Quantile lines
# quant_5, quant_25, quant_50, quant_75, quant_95 = avocado.quantile(0.05), avocado.quantile(0.25), avocado.quantile(0.5), avocado.quantile(0.75), avocado.quantile(0.95)
# quants = [[quant_5, 0.6, 0.16], [quant_25, 0.8, 0.26], [quant_50, 1, 0.36],  [quant_75, 0.8, 0.46], [quant_95, 0.6, 0.56]]
quant_95 = avocado.quantile(0.95)
quants = [[quant_95, 0.6, 0.56]]


for i in quants:
    ax.axvline(i[0], alpha = i[1], ymax = i[2], linestyle = ":")


# X
ax.set_xlabel("Overlap Score")
    # Limit x range to 0-4
x_start, x_end = 0, 1.5
ax.set_xlim(x_start, x_end)

# Y
ax.set_ylim(0, 2)
ax.set_yticklabels([])
ax.set_ylabel("")

# Annotations
# ax.text(quant_5-.1, 0.17, "5th", size = 10, alpha = 0.8)
# ax.text(quant_25-.13, 0.27, "25th", size = 11, alpha = 0.85)
# ax.text(quant_50-.13, 0.37, "50th", size = 12, alpha = 1)
# ax.text(quant_75-.13, 0.47, "75th", size = 11, alpha = 0.85)
ax.text(quant_95-.25, 0.57, "95th Percentile", size = 10, alpha =.8)

# Overall
ax.grid(False)
# ax.set_title("Avocado Prices in U.S. Markets", size = 17, pad = 10)

    # Remove ticks and spines
ax.tick_params(left = False, bottom = False)
for ax, spine in ax.spines.items():
    spine.set_visible(False)
    
plt.show()

plt.savefig('Percentile-overlap.pdf', dpi=100)
