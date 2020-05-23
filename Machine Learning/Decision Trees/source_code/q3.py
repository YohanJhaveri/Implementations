import argparse
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.utils import shuffle
from q2 import kfold_cv

def find_best_knn_hyperparams(xFeat, y):
    testAucs = []

    for k in range(1,30):
        print(k)
        knn = KNeighborsClassifier(n_neighbors=k)
        trainAuc, testAuc, timeElapsed = kfold_cv(knn, xFeat, y, 10)
        testAucs.append((testAuc, k))

    bestAuc, best_k = max(testAucs)

    return best_k


def find_best_dt_hyperparams(xFeat, y):
    testAucs = []

    for max_depth in range(1,10):
        print(max_depth)
        for min_samples_leaf in range(1,50):
            dt = DecisionTreeClassifier(max_depth=max_depth, min_samples_leaf=min_samples_leaf)
            trainAuc, testAuc, timeElapsed = kfold_cv(dt, xFeat, y, 10)
            testAucs.append((testAuc, max_depth, min_samples_leaf))

    bestAuc, best_max_depth, best_min_samples_leaf = max(testAucs)

    return best_max_depth, best_min_samples_leaf


def generate_subset(xFeat, y, size):
    xFeat_copy, y_copy = shuffle(xFeat, y)
    index = round(size * len(xFeat))
    return np.array(xFeat_copy[:index]), np.array(y_copy[:index]).T[0]


def knn(xFeat, y, k):
    KNN = KNeighborsClassifier(n_neighbors=k)
    KNN.fit(xFeat, y)
    return KNN

def dt(xFeat, y, max_depth, min_samples_leaf):
    DT = DecisionTreeClassifier(max_depth=max_depth, min_samples_leaf=min_samples_leaf)
    DT.fit(xFeat, y)
    return DT

def main():
    # set up the program to take in arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("--xTrain",
                        default="q4xTrain.csv",
                        help="filename for features of the training data")
    parser.add_argument("--yTrain",
                        default="q4yTrain.csv",
                        help="filename for labels associated with training data")
    parser.add_argument("--xTest",
                        default="q4xTest.csv",
                        help="filename for features of the test data")
    parser.add_argument("--yTest",
                        default="q4yTest.csv",
                        help="filename for labels associated with the test data")

    args = parser.parse_args()
    # load the train and test data
    xTrain = pd.read_csv(args.xTrain)
    yTrain = pd.read_csv(args.yTrain)
    xTest = pd.read_csv(args.xTest)
    yTest = pd.read_csv(args.yTest)

    best_k = find_best_knn_hyperparams(xTrain, yTrain)

    print('knn ---------')
    print('k: ', best_k)
    print()

    best_max_depth, best_min_samples_leaf = find_best_dt_hyperparams(xTrain, yTrain)

    print('dt ---------')
    print('max depth: ', best_max_depth)
    print('min samples leaf:', best_min_samples_leaf)
    print()

    xFeat_100, y_100 = generate_subset(xTrain, yTrain, 1.00)
    xFeat_99, y_99 = generate_subset(xTrain, yTrain, 0.99)
    xFeat_95, y_95 = generate_subset(xTrain, yTrain, 0.95)
    xFeat_90, y_90 = generate_subset(xTrain, yTrain, 0.90)

    knn_100 = knn(xFeat_100, y_100, best_k)
    knn_99 = knn(xFeat_99, y_99, best_k)
    knn_95 = knn(xFeat_95, y_95, best_k)
    knn_90 = knn(xFeat_90, y_90, best_k)

    dt_100 = dt(xFeat_100, y_100, best_max_depth, best_min_samples_leaf)
    dt_99 = dt(xFeat_99, y_99, best_max_depth, best_min_samples_leaf)
    dt_95 = dt(xFeat_95, y_95, best_max_depth, best_min_samples_leaf)
    dt_90 = dt(xFeat_90, y_90, best_max_depth, best_min_samples_leaf)

    yHat_knn_100 = knn_100.predict(np.array(xTest))
    yHat_knn_99 = knn_99.predict(np.array(xTest))
    yHat_knn_95 = knn_95.predict(np.array(xTest))
    yHat_knn_90 = knn_90.predict(np.array(xTest))

    yHat_dt_100 = dt_100.predict(np.array(xTest))
    yHat_dt_99 = dt_99.predict(np.array(xTest))
    yHat_dt_95 = dt_95.predict(np.array(xTest))
    yHat_dt_90 = dt_90.predict(np.array(xTest))

    accuracy_knn_100 = metrics.accuracy_score(yTest, yHat_knn_100)
    accuracy_knn_99 = metrics.accuracy_score(yTest, yHat_knn_99)
    accuracy_knn_95 = metrics.accuracy_score(yTest, yHat_knn_95)
    accuracy_knn_90 = metrics.accuracy_score(yTest, yHat_knn_90)

    accuracy_dt_100 = metrics.accuracy_score(yTest, yHat_dt_100)
    accuracy_dt_99 = metrics.accuracy_score(yTest, yHat_dt_99)
    accuracy_dt_95 = metrics.accuracy_score(yTest, yHat_dt_95)
    accuracy_dt_90 = metrics.accuracy_score(yTest, yHat_dt_90)

    fpr, tpr, thresholds = metrics.roc_curve(yTest['label'], yHat_knn_100)
    testAuc_knn_100 = metrics.auc(fpr, tpr)

    fpr, tpr, thresholds = metrics.roc_curve(yTest['label'], yHat_knn_99)
    testAuc_knn_99 = metrics.auc(fpr, tpr)

    fpr, tpr, thresholds = metrics.roc_curve(yTest['label'], yHat_knn_95)
    testAuc_knn_95 = metrics.auc(fpr, tpr)

    fpr, tpr, thresholds = metrics.roc_curve(yTest['label'], yHat_knn_90)
    testAuc_knn_90 = metrics.auc(fpr, tpr)

    fpr, tpr, thresholds = metrics.roc_curve(yTest['label'], yHat_dt_100)
    testAuc_dt_100 = metrics.auc(fpr, tpr)

    fpr, tpr, thresholds = metrics.roc_curve(yTest['label'], yHat_dt_99)
    testAuc_dt_99 = metrics.auc(fpr, tpr)

    fpr, tpr, thresholds = metrics.roc_curve(yTest['label'], yHat_dt_95)
    testAuc_dt_95 = metrics.auc(fpr, tpr)

    fpr, tpr, thresholds = metrics.roc_curve(yTest['label'], yHat_dt_90)
    testAuc_dt_90 = metrics.auc(fpr, tpr)

    df_knn = pd.DataFrame([['100%', testAuc_knn_100, accuracy_knn_100],
                           ['99%', testAuc_knn_99, accuracy_knn_99],
                           ['95%', testAuc_knn_95, accuracy_knn_95],
                           ['90%', testAuc_knn_90, accuracy_knn_90]],
                   columns=['Subset proportion', 'TestAUC', 'Accuracy'])

    df_dt = pd.DataFrame([['100%', testAuc_dt_100, accuracy_dt_100],
                          ['99%', testAuc_dt_99, accuracy_dt_99],
                          ['95%', testAuc_dt_95, accuracy_dt_95],
                          ['90%', testAuc_dt_90, accuracy_dt_90]],
                  columns=['Subset proportion', 'TestAUC', 'Accuracy'])

    print('K Nearest Neighbors ---------------')
    print(df_knn)

    print('Decision Tree ---------------')
    print(df_dt)

if __name__ == "__main__":
    main()
