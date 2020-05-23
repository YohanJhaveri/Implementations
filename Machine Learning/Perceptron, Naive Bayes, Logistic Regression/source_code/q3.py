import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB, ComplementNB

def calc_mistakes(yHat, yTrue):
    """
    Calculate the number of mistakes
    that the algorithm makes based on the prediction.

    Parameters
    ----------
    yHat : 1-d array or list with shape n
        The predicted label.
    yTrue : 1-d array or list with shape n
        The true label.

    Returns
    -------
    err : int
        The number of mistakes that are made
    """
    return sum(np.array(yHat) != yTrue.flatten())



def file_to_numpy(filename):
    """
    Read an input file and convert it to numpy
    """
    df = pd.read_csv(filename)
    df = df.reindex(sorted(df.columns), axis=1)
    return df.to_numpy()



def build_model(model, dataset = 'binary'):

    if dataset == 'binary':
        xTrain = file_to_numpy("xTrainBinary.csv")
        xTest = file_to_numpy("xTestBinary.csv")

    if dataset == 'count':
        xTrain = file_to_numpy("xTrainCount.csv")
        xTest = file_to_numpy("xTestCount.csv")

    if dataset == 'tfidf':
        xTrain = file_to_numpy("xTrainTfidf.csv")
        xTest = file_to_numpy("xTestTfidf.csv")

    yTrain = file_to_numpy("yTrain.csv").flatten()
    yTest = file_to_numpy("yTest.csv").flatten()

    model.fit(xTrain, yTrain)
    yHat = model.predict(xTest)

    print("Number of mistakes on the test dataset")
    print(calc_mistakes(yHat, yTest))



def main():
    """
    Main file to run from the command line.
    """
    LR = LogisticRegression(random_state=0, solver='lbfgs', max_iter=2500)
    GNB = GaussianNB()
    BNB = BernoulliNB()
    MNB = MultinomialNB()
    CNB = ComplementNB()

    dataset = 'tfidf'

    build_model(LR, dataset)
    build_model(GNB, dataset)
    build_model(BNB, dataset)
    build_model(MNB, dataset)
    build_model(CNB, dataset)


if __name__ == "__main__":
    main()
