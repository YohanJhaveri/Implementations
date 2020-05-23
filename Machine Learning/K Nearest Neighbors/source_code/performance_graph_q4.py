import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

var_k = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
var_default = [85.83, 87.5, 86.67, 87.08, 86.88, 87.08, 85.83, 86.25, 86.04, 86.04, 86.04, 86.04 ,86.04]
var_standard = [87.92, 86.46, 86.67, 86.88, 87.5, 87.71, 88.54, 88.12, 88.33, 88.96, 88.33, 88.54, 88.75]
var_minmax = [82.92, 85.63, 87.29, 87.08, 86.67, 85.42, 85.21, 86.25, 85.83, 86.88, 87.08, 87.92, 87.29]
var_irrelevant = [76.25, 82.08, 84.79, 86.88, 86.25, 86.45, 86.25, 86.46, 86.46, 86.45, 86.45, 86.45, 86.45]

plt.plot(var_k, var_default, c='orange', marker='o', markerfacecolor='orange', markersize=5)
plt.plot(var_k, var_standard, c='skyblue', marker='o', markerfacecolor='skyblue', markersize=5)
plt.plot(var_k, var_minmax, c='salmon', marker='o', markerfacecolor='salmon', markersize=5)
plt.plot(var_k, var_irrelevant, c='lightgreen', marker='o', markerfacecolor='lightgreen', markersize=5)

legend_dict = { 'no preprocessing' : 'orange', 'standard scale' : 'skyblue', 'minmax scale' : 'salmon' , 'with irrelevant features' : 'lightgreen' }

patchList = []
for key in legend_dict:
    data_key = mpatches.Patch(color=legend_dict[key], label=key)
    patchList.append(data_key)

plt.legend(handles=patchList)

plt.title('Accuracy vs k')

plt.xticks(var_k)

plt.xlabel('k')
plt.ylabel('Accuracy (%)')



plt.show()
