import argparse
import numpy as np
import pandas as pd

from xgboost import XGBClassifier

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
    parser.add_argument("--learningRate", default=0.1,
                        type=int, help="default seed number")
    parser.add_argument("--maxDepth", default=13,
                        type=int, help="default seed number")
    parser.add_argument("--numRounds", default=1,
                        type=int, help="default seed number")

    args = parser.parse_args()
    # load the train and test data assumes you'll use numpy
    xTrain = file_to_numpy(args.xTrain)
    yTrain = file_to_numpy(args.yTrain)
    xTest = file_to_numpy(args.xTest)
    yTest = file_to_numpy(args.yTest)

    yTrain = np.ravel(yTrain)
    yTest = np.ravel(yTest)

    errors = {}

    i = 0

    for max_depth in range(1,20):
        for learning_rate in [0.01, 0.1, 1]:
            for num_rounds in range(1,10):
                xgb = XGBClassifier(learning_rate = learning_rate, max_depth = max_depth, num_rounds = num_rounds)

                xgb.fit(xTrain, yTrain)
                yHat = xgb.predict(xTest)
                yTest = yTest.flatten()

                error = 1 - (sum([yHat[i] == yTest[i] for i in range(len(yHat))]) / len(yHat))

                errors[i] = [error, max_depth, learning_rate]
                i += 1

    errors = pd.DataFrame(errors).T.to_csv('./performance_xgboost.csv', index=False)
    # print(errors)

    # OPTIMAL HYPERPARAMETERS: (50, 4, 'gini', 15, 10)
    # max_depth = 13
    # learning_rate = 0.1
    # num_rounds = 1

    xgb = XGBClassifier(learning_rate = args.learningRate, max_depth = args.maxDepth, num_rounds = args.numRounds)

    xgb.fit(xTrain, yTrain)
    yHat = xgb.predict(xTest)
    yTest = yTest.flatten()

    print(xgb.predict(xTest))

    error = 1 - (sum([yHat[i] == yTest[i] for i in range(len(yHat))]) / len(yHat))
    print(error)

if __name__ == "__main__":
    main()
