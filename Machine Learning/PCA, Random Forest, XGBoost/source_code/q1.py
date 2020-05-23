import argparse
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA, NMF
from sklearn.metrics import roc_curve

import matplotlib.pyplot as plt

def main():
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

    xTrain = pd.read_csv(args.xTrain)
    yTrain = pd.read_csv(args.yTrain)
    xTest = pd.read_csv(args.xTest)
    yTest = pd.read_csv(args.yTest)

    scaler = StandardScaler(with_mean=False)
    xTrain = scaler.fit_transform(xTrain)
    xTest = scaler.fit_transform(xTest)

    pca = PCA(n_components=9)
    xTrainPCA = pca.fit_transform(xTrain)
    xTestPCA = pca.fit_transform(xTest)
    print(sum(pca.explained_variance_ratio_))
    print(pca.components_)

    nmf = NMF(n_components=9)
    xTrainNMF = nmf.fit_transform(xTrain)
    xTestNMF = nmf.fit_transform(xTest)
    print(nmf.components_)

    LR = LogisticRegression(solver='lbfgs')
    LR.fit(xTrain, yTrain)
    yHat = LR.predict_proba(xTest)[:,1]
    yTest = np.array(yTest).flatten()
    fpr, tpr, thresholds = roc_curve(yTest, yHat)
    plt.plot(fpr, tpr, label='NOR')

    LR = LogisticRegression(solver='lbfgs')
    LR.fit(xTrainPCA, yTrain)
    yHat = LR.predict_proba(xTestPCA)[:,1]
    yTest = np.array(yTest).flatten()
    fpr, tpr, thresholds = roc_curve(yTest, yHat)
    plt.plot(fpr, tpr, label='PCA')

    LR = LogisticRegression(solver='lbfgs')
    LR.fit(xTrainNMF, yTrain)
    yHat = LR.predict_proba(xTestNMF)[:,1]
    yTest = np.array(yTest).flatten()
    fpr, tpr, thresholds = roc_curve(yTest, yHat)
    plt.plot(fpr, tpr, label='NMF')

    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.title('ROC curve')
    plt.legend(loc='best')
    plt.show()


if __name__ == "__main__":
    main()
