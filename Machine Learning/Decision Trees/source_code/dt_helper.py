import numpy as np
import math

def find_best_feature(data, criterion):
    features = data.columns[:-1]

    best_costs = []
    best_splits = []

    for feature in features:
        min_cost, min_split = find_best_split(feature, data, criterion)
        best_costs.append(min_cost)
        best_splits.append(min_split)

    best_cost = min(best_costs)
    best_index = best_costs.index(best_cost)

    return features[best_index], best_splits[best_index]

# O(n^2)
def find_best_split(feature, data, criterion):
    costs = []

    splits = find_split_testing_values(feature, data)

    for split in splits:

        T, F = get_split(feature, split, data)

        if criterion == 'entropy':
            cost_T = calculate_entropy(list(T['y']))
            cost_F = calculate_entropy(list(F['y']))

        elif criterion == 'gini':
            cost_T = calculate_gini(list(T['y']))
            cost_F = calculate_gini(list(F['y']))

        costs.append(((len(T) * cost_T) + (len(F) * cost_F)) / (len(T) + len(F)))

    min_cost = min(costs)
    min_split = splits[costs.index(min_cost)]

    return min_cost, min_split

# O(n)
def get_split(feature, split, data):
    x = np.array(data[feature])

    T, F = [], []

    for i in range(len(x)):
        if x[i] > split: T.append(i)
        else:            F.append(i)

    return data.iloc[T], data.iloc[F]

# O(n)
def calculate_entropy(classification):
    counts = {x: 0 for x in set(classification)}

    for x in classification:
        counts[x] += 1

    total = len(classification)

    entropy = 0

    for c in counts:
        count = counts[c]
        entropy += (- count / total) * math.log((count / total), 2)

    return entropy

# O(n)
def calculate_gini(classification):
    counts = {x: 0 for x in set(classification)}

    for x in classification:
        counts[x] += 1

    total = len(classification)

    gini = 0

    for c in counts:
        count = counts[c]
        p = count / total
        gini +=  p * (1-p)

    return gini

# O(n)
def find_split_testing_values(feature, data):
    x = np.array(data[feature])
    y = np.array(data['y'])

    current = 0

    splits = []

    for i in range(len(x)):
        if y[i] != current:
            current = y[i]
            average = (x[i] + x[i-1]) / 2
            splits.append(average)

    return splits
