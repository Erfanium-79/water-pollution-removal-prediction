import matplotlib.pylab as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('dataset.csv')
original_feature_name = ['Catalyst', 'pH', 'Catalyst dosage (g/L)', '[C0] MO (mg/L)', '[C0] 2,4-DCP (mg/L)', 'H2O2 (mM)', 'Time (min)', 'DE%'] #'DE%'
df.columns = original_feature_name

# HeatMap pdf
plt.figure(figsize=(21, 19))
ax = sns.heatmap(df.corr(), cmap='BrBG', annot=True, annot_kws={"size": 23, "weight": "bold"}, cbar=False)
# ax.tick_params(axis='both', which='major', labelsize=15, fontweight='bold')
plt.yticks(fontsize=20 , fontweight= 'bold', color= '#305f7f')
plt.xticks(fontsize=20 , fontweight= 'bold', color= '#305f7f')
# plt.savefig('heatmap.png', dpi=1500, bbox_inches="tight")
# Access the colorbar and set its tick label properties
colorbar = ax.figure.colorbar(ax.collections[0])
colorbar.ax.tick_params(labelsize=21, width=2, )  # Increase label size and thickness
# Rotate x-axis labels to vertical orientation
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
plt.savefig('heatmap.pdf', format="pdf", dpi=1700, bbox_inches="tight")

# HeatMap png
plt.figure(figsize=(21, 19))
ax = sns.heatmap(df.corr(), cmap='BrBG', annot=True, annot_kws={"size": 23, "weight": "bold"}, cbar=False)
# ax.tick_params(axis='both', which='major', labelsize=15, fontweight='bold')
plt.yticks(fontsize=20 , fontweight= 'bold', color= '#305f7f')
plt.xticks(fontsize=20 , fontweight= 'bold', color= '#305f7f')
# plt.savefig('heatmap.png', dpi=1500, bbox_inches="tight")
# Access the colorbar and set its tick label properties
colorbar = ax.figure.colorbar(ax.collections[0])
colorbar.ax.tick_params(labelsize=21, width=2, )  # Increase label size and thickness
# Rotate x-axis labels to vertical orientation
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
plt.savefig('heatmap.png', format="png", dpi=1300, bbox_inches="tight")