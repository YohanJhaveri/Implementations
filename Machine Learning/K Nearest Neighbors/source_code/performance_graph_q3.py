import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

var_k = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]
var_train = [100, 96, 95, 95, 94, 94, 93, 93, 93, 92, 93, 92, 92, 93, 93, 93, 93]
var_test = [90, 91, 92, 92, 91, 91, 92, 92, 92, 92, 92, 92 ,92 ,92 ,92, 92, 92]

plt.plot(var_k, var_train, c='orange', marker='o', markerfacecolor='orange', markersize=5)
plt.plot(var_k, var_test, c='blue', marker='o', markerfacecolor='blue', markersize=5)

legend_dict = { 'training data' : 'orange', 'testing data' : 'blue' }

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
