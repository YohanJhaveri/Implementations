import argparse
import numpy as np
import pandas as pd

from sklearn.tree import DecisionTreeClassifier


class RandomForest(object):
    nest = 0           # number of trees
    maxFeat = 0        # maximum number of features
    maxDepth = 0       # maximum depth of the decision tree
    minLeafSample = 0  # minimum number of samples in a leaf
    criterion = None   # splitting criterion

    forest = []

    def __init__(self, nest, maxFeat, criterion, maxDepth, minLeafSample):
        """
        Decision tree constructor

        Parameters
        ----------
        nest: int
            Number of trees to have in the forest
        maxFeat: int
            Maximum number of features to consider in each tree
        criterion : String
            The function to measure the quality of a split.
            Supported criteria are "gini" for the Gini impurity
            and "entropy" for the information gain.
        maxDepth : int
            Maximum depth of the decision tree
        minLeafSample : int
            Minimum number of samples in the decision tree
        """
        self.nest = nest
        self.maxFeat = maxFeat
        self.criterion = criterion
        self.maxDepth = maxDepth
        self.minLeafSample = minLeafSample


    def train(self, xFeat, y):
        """
        Train the random forest using the data

        Parameters
        ----------
        xFeat : nd-array with shape n x d
            Training data
        y : 1d array with shape n
            Array of responses associated with training data.

        Returns
        -------
        stats : object
            Keys represent the number of trees and
            the values are the out of bag errors
        """

        stats = {}
        self.forest = []

        for i in range(self.nest):

            samples = np.random.randint(len(xFeat), size=len(xFeat))
            xBoot = xFeat[samples]
            yBoot = y[samples]

            tree = DecisionTreeClassifier(
                        criterion=self.criterion,
                        max_depth=self.maxDepth,
                        min_samples_leaf=self.minLeafSample,
                        max_features=self.maxFeat
                    )

            tree.fit(xBoot, yBoot)
            self.forest.append(tree)

            yHat = self.predict(xFeat)
            yTrue = np.array(y).flatten()

            stats[i + 1] = sum([yHat[i] != yTrue[i] for i in range(len(yHat))]) / len(yHat)

        return stats

    def predict(self, xFeat):
        """
        Given the feature set xFeat, predict
        what class the values will have.

        Parameters
        ----------
        xFeat : nd-array with shape m x d
            The data to predict.

        Returns
        -------
        yHat : 1d array or list with shape m
            Predicted response per sample
        """
        yHat = []

        predictions = []

        for tree in self.forest:
            predictions.append(tree.predict(xFeat))

        predictions = np.array(predictions)

        yHat = np.round(predictions.sum(axis=0) / len(predictions))

        return yHat


def file_to_numpy(filename):
    """
    Read an input file and convert it to numpy
    """
    df = pd.read_csv(filename)
    return df.to_numpy()


def main():
    """
    Main file to run from the command line.
    """
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
    parser.add_argument("--seed", default=334,
                        type=int, help="default seed number")
    parser.add_argument("--nest", default=50,
                        type=int, help="default seed number")
    parser.add_argument("--maxFeat", default=4,
                        type=int, help="default seed number")
    parser.add_argument("--criterion", default='gini',
                        type=str, help="default seed number")
    parser.add_argument("--maxDepth", default=15,
                        type=int, help="default seed number")
    parser.add_argument("--minLeafSample", default=10,
                        type=int, help="default seed number")

    args = parser.parse_args()
    # load the train and test data assumes you'll use numpy
    xTrain = file_to_numpy(args.xTrain)
    yTrain = file_to_numpy(args.yTrain)
    xTest = file_to_numpy(args.xTest)
    yTest = file_to_numpy(args.yTest)

    np.random.seed(args.seed)

    # errors = {}
    #
    # i = 0
    #
    # criterion = 'gini'
    #
    # for nest in [25, 50, 100]:
    #     for maxFeat in [2, 4, 6]:
    #         for maxDepth in [5, 10, 15]:
    #             for minLeafSample in [10, 20, 30]:
    #                     RF = RandomForest(nest, maxFeat, criterion, maxDepth, minLeafSample)
    #                     RF.train(xTrain, yTrain)
    #                     yHat = RF.predict(xTest)
    #                     yTest = np.array(yTest).flatten()
    #                     accuracy = sum([yHat[i] == yTest[i] for i in range(len(yHat))]) / len(yHat)
    #                     error = 1 - accuracy
    #
    #                     errors[i] = [error, nest, maxFeat, criterion, maxDepth, minLeafSample]
    #                     i += 1
    #
    # errors = pd.DataFrame(errors).T.to_csv('./performance_rf.csv', index=False)

    # OPTIMAL HYPERPARAMETERS: (50, 4, 'gini', 15, 10)
    # nest = 50
    # criterion = 'gini'
    # maxFeat = 4
    # maxDepth = 15
    # minLeafSample = 10

    RF = RandomForest(args.nest, args.maxFeat, args.criterion, args.maxDepth, args.minLeafSample)
    trainStats = RF.train(xTrain, yTrain)
    print(trainStats)

    yHat = RF.predict(xTest)
    yTest = yTest.flatten()

    accuracy = sum([yHat[i] == yTest[i] for i in range(len(yHat))]) / len(yHat)
    error = 1 - accuracy
    print(error)

if __name__ == "__main__":
    main()
