from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# loads iris dataset and store it in the variable 'iris'
iris = load_iris()

# extracts the features and target of the data from iris and stores it in the respective variables
data = iris['data']
target = iris['target']

# list of features of the iris in order of the data values
features = ['sepal length', 'sepal width', 'petal length', 'petal width']

# initializing a dictionary to organize features of the iris by species
features_by_species = {x: np.zeros((50,3)) for x in features}

# fills features_by_species dictionary with respective feature values as described
for i, f in enumerate(features):
    for j in range(3):
        features_by_species[f][:,j] = data[:,i][target == j]

def boxplot(type):
    """
    Plot a boxplot for a particular feature of the iris for each species

    Parameters
    ----------
    type : string ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']
        Name of the feature for which a boxplot is wanted

    """
    # plots boxplots for a specific feature for each species of the iris
    plt.boxplot(features_by_species[type.lower()])

    # annotates the plot
    plt.title(type + ' for Iris Species')
    plt.xticks([1,2,3], ['setosa', 'versicolor', 'virginica'])
    plt.xlabel('Iris Species')
    plt.ylabel(type + ' (cm)')

def scatter(type):
    """
    Plot a scatter plot for either petal or sepal dimensions of the iris with each species distinguished by color

    Parameters
    ----------
    type : string ['Sepal', 'Petal']
        Name of the feature for which a scatter plot is wanted

    """
    # list of colors of the same dimensions as the target list with colors corresponding to target values
    colors = [['salmon', 'skyblue', 'lightgreen'][i] for i in target]

    # choosing the first two columns of the iris dataset if parameter 'type' is Sepal as the first two columns of the dataset are sepal length and sepal width
    x,y = (0,1) if type == 'Sepal' else (2,3)

    # plots a scatter plot of the length vs width of either a petal or sepal for all species of the iris with each species distinguished by color
    plt.scatter(data[:,x], data[:,y], c = colors, s=20)

    # annotates the plot
    plt.title(type + ' Length vs ' + type + ' Width for Iris species')
    plt.xlabel(type + ' Length (cm)')
    plt.ylabel(type + ' Width (cm)')


    # adds color legend to plot to designate species
    legend_dict = { 'setosa' : 'salmon', 'versicolor' : 'skyblue', 'virginica' : 'lightgreen' }

    patchList = []
    for key in legend_dict:
            data_key = mpatches.Patch(color=legend_dict[key], label=key)
            patchList.append(data_key)

    plt.legend(handles=patchList)

# boxplot('Sepal Length')
# boxplot('Sepal Width')
# boxplot('Petal Length')
# boxplot('Petal Width')
#
# scatter('Sepal')
# scatter('Petal')

plt.show()
