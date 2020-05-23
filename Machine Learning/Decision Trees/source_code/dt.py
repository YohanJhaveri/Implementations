import argparse
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score

from dt_helper import find_best_feature, get_split

class Node:
    def __init__(self, feature, split, depth):
        self.left = None
        self.right = None
        self.feature = feature
        self.split = split
        self.depth = depth

    def test(self, value):
        return value > self.split

class Leaf:
    def __init__(self, classification):
        self.classification = classification

    def classify(self):
        return self.classification


class DecisionTree(object):
    maxDepth = 0       # maximum depth of the decision tree
    minLeafSample = 0  # minimum number of samples in a leaf
    criterion = None   # splitting criterion

    def __init__(self, criterion, maxDepth, minLeafSample):
        """
        Decision tree constructor

        splits
        ----------
        criterion : String
            The function to measure the quality of a split.
            Supported criteria are "gini" for the Gini impurity
            and "entropy" for the information gain.
        maxDepth : int
            Maximum depth of the decision tree
        minLeafSample : int
            Minimum number of samples in the decision tree
        """
        self.criterion = criterion
        self.maxDepth = maxDepth
        self.minLeafSample = minLeafSample
        self.data = None
        self.root = None

    def train(self, xFeat, y):
        """
        Train the decision tree model.

        splits
        ----------
        xFeat : nd-array with shape n x d
            Training data
        y : 1d array with shape n
            Array of labels associated with training data.

        Returns
        -------
        self : object
        """
        # TODO do whatever you need
        self.data = pd.DataFrame(xFeat)
        self.data['y'] = y

        self.root = self.build_tree(self.data, 0)

        return self


    def build_tree(self, data, depth):

        if depth <= self.maxDepth:

            outputs = list(data['y'])

            if depth < self.maxDepth and len(set(outputs)) > 1 and len(outputs) >= self.minLeafSample:

                feature, split = find_best_feature(data, self.criterion)

                T, F = get_split(feature, split, data)

                node = Node(feature, split, depth)

                if node.left == None:
                    node.left = self.build_tree(F, depth + 1)

                if node.right == None:
                    node.right = self.build_tree(T, depth + 1)

            else:
                node = Leaf(max(outputs, key=outputs.count))

            return node


    def predict(self, xFeat):
        """
        Given the feature set xFeat, predict
        what class the values will have.

        splits
        ----------
        xFeat : nd-array with shape m x d
            The data to predict.

        Returns
        -------
        yHat : 1d array or list with shape m
            Predicted class label per sample
        """
        yHat = [] # variable to store the estimated class label

        for index, point in xFeat.iterrows():
            current = self.root

            while not isinstance(current, Leaf):
                if current.test(point[current.feature]):
                    current = current.right
                else:
                    current = current.left

            yHat.append(current.classify())

        return yHat

def dt_train_test(dt, xTrain, yTrain, xTest, yTest):
    """
    Given a decision tree model, train the model and predict
    the labels of the test data. Returns the accuracy of
    the resulting model.

    splits
    ----------
    dt : DecisionTree
        The decision tree with the model splits
    xTrain : nd-array with shape n x d
        Training data
    yTrain : 1d array with shape n
        Array of labels associated with training data.
    xTest : nd-array with shape m x d
        Test data
    yTest : 1d array with shape m
        Array of labels associated with test data.

    Returns
    -------
    acc : float
        The accuracy of the trained knn model on the test data
    """
    # train the model
    dt.train(xTrain, yTrain['label'])
    # predict the training dataset
    yHatTrain = dt.predict(xTrain)
    trainAcc = accuracy_score(yTrain['label'], yHatTrain)
    # predict the test dataset
    yHatTest = dt.predict(xTest)
    testAcc = accuracy_score(yTest['label'], yHatTest)
    return trainAcc, testAcc


def main():
    """
    Main file to run from the command line.
    """
    # set up the program to take in arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("md",
                        type=int,
                        help="maximum depth")
    parser.add_argument("mls",
                        type=int,
                        help="minimum leaf samples")
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
    # create an instance of the decision tree using gini
    dt1 = DecisionTree('gini', args.md, args.mls)
    trainAcc1, testAcc1 = dt_train_test(dt1, xTrain, yTrain, xTest, yTest)
    print("GINI Criterion ---------------")
    print("Training Acc:", trainAcc1)
    print("Test Acc:", testAcc1)
    dt = DecisionTree('entropy', args.md, args.mls)
    trainAcc, testAcc = dt_train_test(dt, xTrain, yTrain, xTest, yTest)
    print("ENTROPY Criterion ---------------")
    print("Training Acc:", trainAcc)
    print("Test Acc:", testAcc)


if __name__ == "__main__":
    main()
