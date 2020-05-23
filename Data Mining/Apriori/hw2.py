import time
import numpy as np
import argparse
from collections import defaultdict

def apriori(input, support, output):

    # read data from input file
    input = open(input, "r")

    items = {}
    freqs = {}

    def sort_combination(combination):
        return tuple([str(i) for i in sorted([int(i) for i in list(combination)])])

    # finds the support of the given combination number of transactions
    # itemset represents the combination
    def find_count(itemset):
        # finds the index corresponding to the item number
        itemset = [items[i] for i in itemset]

        # performs row-wise multiplication on the len(transactions) * len(items) sized matrix
        # produces a len(transactions) * 1 sized vector that contains binary values
        # each value represents whether the itemset combination exists in that transaction or not
        # the entire vector is then summed to find the total number of transactions the itemset combination appears in
        return np.sum(np.prod(data[:, itemset], axis=1))

    # delete combinations that do not meet the support threshold
    def delete_keys(n):
        keys = list(freqs[n].keys())
        for key in keys:

            # if the count of the combinaion is less than the minimum support threshold, delete the combination from the dictionary
            if freqs[n][key] < support:
                del freqs[n][key]


    transactions = []
    dictionary_count = 0

    # add all transactions in the input file to a list named 'transactions'
    for i in input:
        transaction = i.split()
        transactions.append(transaction)

        # add all items in the input file as the key to a dictionary named 'items' with the value corresponding to its column index in the 2D array
        for item in transaction:
            if item not in items:
                items[item] = dictionary_count
                dictionary_count += 1

    # create 2D numpy array of items and transactions [transactions -> rows, items -> columns]
    data = np.zeros((len(transactions), len(items)))

    # populate 2D numpy array of items and transactions with binary values [0 -> item not present in transaction, 1 -> item present in transaction]
    for i, transaction in enumerate(transactions):
        for item in transaction:
            data[i, items[item]] = 1

    # initialize one-sized and two-sized combination frequencies as defaultdicts for cleaner code
    freqs[1] = defaultdict(int)
    freqs[2] = defaultdict(int)

    # find the transaction frequencies of one-item and two-item combinations in the data (how many transactions was the combination present in)
    for transaction in transactions:
        n = len(transaction)

        for i in range(n):
            key = (transaction[i], )
            freqs[1][key] += 1

            for j in range(i+1, n):
                key = sort_combination([transaction[i], transaction[j]])
                freqs[2][key] += 1

    # delete all combinations that do not meet the support threshold
    delete_keys(1)
    delete_keys(2)

    n = 2

    # if the length of the filtered combinations that meet the threshold is less than 2, no new combinations can be formed of higher order (n+1)
    while len(freqs[n]) > 2:
        freqs[n + 1] = {}
        keys = list(freqs[n].keys())

        # generate higher order combinations from the lower order combinations that met the support threshold
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                # generate a higher order combination from the union of two smaller order combinations and sort the combination tuple
                union = sort_combination(set(keys[i]).union(set(keys[j])))
                # if the combination freqeuncy has not already been calculated before and if it's length is equal to the size of the current item combinations being found
                if union not in freqs[n + 1] and len(union) == (n + 1):
                    freqs[n + 1][union] = find_count(union)

        # delete all combinations that do not meet the support threshold
        delete_keys(n + 1)
        n += 1

    # write frequencies to output file
    output = open(output, "w+")

    for x in freqs:
        for y in freqs[x]:
            output.write(' '.join([i for i in y]) + ' (' + str(int(freqs[x][y])) + ')\n')


def main():
    # set up the program to take in arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("input",
                        nargs='?',
                        default="T10I4D100K.txt")
    parser.add_argument("support",
                        type=int,
                        nargs='?',
                        default=500)
    parser.add_argument("output",
                        nargs='?',
                        default="result500.txt")

    args = parser.parse_args()

    start = time.time()

    # run function on input file with minimum support threshold to generate the output file
    apriori(args.input, args.support, args.output)


if __name__ == "__main__":
    main()
