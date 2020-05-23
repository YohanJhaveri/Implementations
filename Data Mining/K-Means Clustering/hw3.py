import numpy as np
import argparse
import random
import math

# k-means clustering algorithm that detects clusters of data points in unlabeled data
def KMeansClustering(input, k, output):
    input = open(input, "r")

    # import data and populate data structure
    data = []
    for line in input:
        data.append([float(i) for i in line.split(',')[:-1]])
    data = np.array(data[:-1])

    # calculates the euclidian distance between any two vectors of the same length
    def euclidian_distance(x, y):
        return math.sqrt(sum([(x[i] - y[i])**2 for i in range(len(x))]))

    # finds the sum of SSE of all the clusters
    def variance(clusters, centroids):
        return sum([math.sqrt(sum([euclidian_distance(centroids[i], j)**2 for j in clusters[i]])) for i in clusters])

    # finds the silhouette coefficient of each cluster
    def silhouette(clusters, centroids):
        coefficient = 0

        for c1 in clusters:

            for i in clusters[c1]:
                a = sum([euclidian_distance(i, j) for j in clusters[c1]]) / (len(clusters[c1]) - 1)
                b = min([sum(([euclidian_distance(i, j) for j in clusters[c2]])) / len(clusters[c2]) for c2 in list(set(clusters) - {c1})])
                coefficient += (b - a) / max(a,b)

        return coefficient / len(data)



    # classifies data point into cluster group based on the euclidian distance metric
    def classify(centroids):
        clusters = {i:[] for i in range(len(centroids))}

        for d in data:
            # calculate distance of data point from each cluster centroid
            distances = [euclidian_distance(d, c) for c in centroids]

            # find the cluster centroid with the shortest distance to the data point
            closest = distances.index(min(distances))

            # add the data point to the cluster with the shortest centroid distance
            clusters[closest].append(d)

        return clusters


    # generates random cluster centroids to begin forming clusters with
    def select_random_centroids(k):
        indexes = []

        # genrate random list of indices of length k corresponding to the initial k cluster centroid data points
        while len(indexes) < k:
            number = random.randint(0, len(data)-1)
            if number not in indexes: indexes.append(number)

        return data[indexes]

    centroids = select_random_centroids(k)
    clusters = classify(centroids)

    # continue iterating over the clusters while they keep changing
    while True:

        flag1 = True

        # if any cluster has 0 data points, this will throw an error since the mean cannot be calculated for the next iteration
        # therefore, flag this situation to re-initialize the clusters if any cluster has zero data points
        for i in clusters:
            if len(clusters[i]) == 0:
                flag1 = False

        # preserving old cluster value in original
        original = clusters

        # find average centroid for each cluster
        if flag1: averages = [np.mean(clusters[i], axis=0) for i in range(k)]
        # clusters are re-initialized when a cluster has 0 data points
        else: averages = select_random_centroids(k)

        # generate new clusters using the new calculated averages as cluster centroids
        clusters = classify(averages)

        # if a cluster has not changed over an iteration, break out of the loop
        # comparing original cluster prior to iteration to new cluster post iteration
        bool = True
        try:                   np.testing.assert_equal(clusters, original)
        except AssertionError: bool = False
        if bool: break

    # invert the clusters dictionary for easier classification of data point cluster in output file
    inverse = {}

    for i in clusters:
        for j in clusters[i]:
            inverse[tuple(j)] = i

    output = open(output, "w+")

    # writing the corresponding cluster of each data point using the inverted clusters dictionary
    for d in data:
        output.write(str(inverse[tuple(d)]) + '\n')

    classes = []

    for d in data:
        classes.append(inverse[tuple(d)])

    # write evaluation metric scores (SSE and Silhouette Coefficient) to the last line of the file
    output.write('SSE: ' + str(variance(clusters, averages)) + ' Silhouette: ' + str(silhouette(clusters, averages)) + '\n')



def main():
    # set up the program to take in arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("input",
                        nargs='?',
                        default="iris.data")
    parser.add_argument("k",
                        type=int,
                        nargs='?',
                        default=3)
    parser.add_argument("output",
                        nargs='?',
                        default="iris_output.data")

    args = parser.parse_args()

    # run function on input file with the hyperparameter 'k' to generate the output file
    KMeansClustering(args.input, args.k, args.output)


if __name__ == "__main__":
    main()
