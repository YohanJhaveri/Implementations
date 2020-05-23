import argparse
import numpy as np
import pandas as pd
import math

class Knn(object):
    k = 0    # number of neighbors to use

    def __init__(self, k):
        """
        Knn constructor

        Parameters
        ----------
        k : int
            Number of neighbors to use.
        """
        self.k = k
        self.data = 0

    def train(self, xFeat, y):
        """
        Train the k-nn model.

        Parameters
        ----------
        xFeat : nd-array with shape n x d
            Training data
        y : 1d array with shape n
            Array of labels associated with training data.

        Returns
        -------
        self : object
        """
        xFeat['y'] = y
        self.data = np.array(xFeat)

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
            Predicted class label per sample
        """
        yHat = [] # variable to store the estimated class label

        xFeat = np.array(xFeat)
        for i in range(len(xFeat)):
            distances = [self.euclidian_distance(list(xFeat[i]), list(self.data[j])) for j in range(len(self.data))] # find euclidian distance of point needed to be classified with other points in the dataset
            k_closest = self.find_k_min(distances) # stores the target value of the k closest data points
            yHat.append(max(k_closest, key=k_closest.count)) # finds the majority class from the k closest data points
        return yHat

    def euclidian_distance(self, x1, x2):
        return math.sqrt(sum([(x1[i] - x2[i]) ** 2 for i in range(len(x1))])) # finds the euclidian distance between two points

    # finds k closest data points from the distances list
    def find_k_min(self, distances):
        closest = []
        for x in range(self.k): # runs k times to find the k closest data points
            index = distances.index(min(distances)) # finds the index of the minimum element
            distances[index] = float('Inf') # changes the value of the min element so it that it isn't recounted as the minimum element while find the next smallest element in the array
            closest.append(self.data[index][-1]) # appends the target value of the next closest data point to the list closest
        return closest

def accuracy(yHat, yTrue):
    """
    Calculate the accuracy of the prediction

    Parameters
    ----------
    yHat : 1d-array with shape n
        Predicted class label for n samples
    yTrue : 1d-array with shape n
        True labels associated with the n samples

    Returns
    -------
    acc : float between [0,1]
        The accuracy of the model
    """

    n = len(yHat)
    acc = 0

    for i in range(n):
        acc += yHat[i] == yTrue[i]

    return float(acc) / n



def main():
    """
    Main file to run from the command line.
    """
    # set up the program to take in arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("k",
                        type=int,
                        help="the number of neighbors")
    parser.add_argument("--xTrain",
                        default="q3xTrain.csv",
                        help="filename for features of the training data")
    parser.add_argument("--yTrain",
                        default="q3yTrain.csv",
                        help="filename for labels associated with training data")
    parser.add_argument("--xTest",
                        default="q3xTest.csv",
                        help="filename for features of the test data")
    parser.add_argument("--yTest",
                        default="q3yTest.csv",
                        help="filename for labels associated with the test data")

    args = parser.parse_args()
    # load the train and test data
    xTrain = pd.read_csv(args.xTrain)
    yTrain = pd.read_csv(args.yTrain)
    xTest = pd.read_csv(args.xTest)
    yTest = pd.read_csv(args.yTest)
    # create an instance of the model
    knn = Knn(args.k)
    knn.train(xTrain, yTrain['label'])
    # predict the training dataset
    yHatTrain = knn.predict(xTrain)
    trainAcc = accuracy(yHatTrain, yTrain['label'])
    # predict the test dataset
    yHatTest = knn.predict(xTest)
    testAcc = accuracy(yHatTest, yTest['label'])
    print("Training Acc:", trainAcc)
    print("Test Acc:", testAcc)

if __name__ == "__main__":
    main()
