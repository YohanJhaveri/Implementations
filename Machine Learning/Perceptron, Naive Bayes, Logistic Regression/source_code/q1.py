import argparse
import numpy as np
import pandas as pd
from collections import defaultdict, Counter
from sklearn import preprocessing
from sklearn import model_selection
from sklearn.feature_extraction.text import CountVectorizer

class Q1:

	def __init__(self):
		self.file = open("spamAssassin.data")
		self.data = self.file.read()
		self.emails = self.data.split('\n')[:-1]

	def model_assessment(self):
		"""
		Given the entire data, decide how
		you want to assess your different models
		to compare perceptron, logistic regression,
		and naive bayes, the different parameters,
		and the different datasets.
		"""

		x, y = [], []

		for email in self.emails:
			x.append(email[2:])
			y.append(int(email[0]))

		return model_selection.train_test_split(x, y, test_size=0.3)



	def build_vocab_map(self, xTrain):

		vocab = defaultdict(int)

		for email in xTrain:
			words = email.split(' ')

			for word in set(words):
				vocab[word] += 1

		vocab = {word: vocab[word] for word in vocab if vocab[word] > 30}

		return list(vocab)


	def construct_binary(self, vocab, X):
		"""
		Construct the email datasets based on
		the binary representation of the email.
		For each e-mail, transform it into a
		feature vector where the ith entry,
		$x_i$, is 1 if the ith word in the
		vocabulary occurs in the email,
		or 0 otherwise
		"""

		binary = pd.DataFrame(0, index=list(range(len(X))), columns=vocab)

		for i, email in enumerate(X):

			words = set(email.split(' '))
			vocab = set(vocab)
			intersection = words.intersection(vocab)

			for word in intersection:
				binary[word][i] = 1

		return binary


	def construct_count(self, vocab, X):
		"""
		Construct the email datasets based on
		the count representation of the email.
		For each e-mail, transform it into a
		feature vector where the ith entry,
		$x_i$, is the number of times the ith word in the
		vocabulary occurs in the email,
		or 0 otherwise
		"""

		count = pd.DataFrame(0, index=list(range(len(X))), columns=vocab)

		for i, email in enumerate(X):

			words = set(email.split(' '))
			vocab = set(vocab)
			intersection = words.intersection(vocab)

			for word in intersection:
				count[word][i] = email.count(word)

		return count


	def construct_tfidf(self, vocab, X):
		"""
		Construct the email datasets based on
		the TF-IDF representation of the email.
		"""

		vectorizer = CountVectorizer(vocabulary=vocab)

		tfidf = pd.DataFrame(vectorizer.fit_transform(X).todense())

		return tfidf


def main():
	"""
	Main file to run from the command line.
	"""
	# set up the program to take in arguments from the command line
	parser = argparse.ArgumentParser()
	parser.add_argument("--data",
						default="spamAssassin.data",
						help="filename of the input data")
	args = parser.parse_args()

	q1 = Q1()

	xTrain, xTest, yTrain, yTest = q1.model_assessment()

	vocab = q1.build_vocab_map(xTrain)

	xTrainBinary = q1.construct_binary(vocab, xTrain)
	xTrainCount = q1.construct_count(vocab, xTrain)
	xTrainTfidf = q1.construct_tfidf(vocab, xTrain)

	xTestBinary = q1.construct_binary(vocab, xTest)
	xTestCount = q1.construct_count(vocab, xTest)
	xTestTfidf = q1.construct_tfidf(vocab, xTest)

	yTrainDF = pd.DataFrame()
	yTrainDF['y'] = yTrain

	yTestDF = pd.DataFrame()
	yTestDF['y'] = yTest

	yTrainDF.to_csv('./yTrain.csv', index=False)
	yTestDF.to_csv('./yTest.csv', index=False)


	xTrainBinary.to_csv('./xTrainBinary.csv', index=False)
	xTrainCount.to_csv('./xTrainCount.csv', index=False)
	xTrainTfidf.to_csv('./xTrainTfidf.csv', index=False)

	xTestBinary.to_csv('./xTestBinary.csv', index=False)
	xTestCount.to_csv('./xTestCount.csv', index=False)
	xTestTfidf.to_csv('./xTestTfidf.csv', index=False)

if __name__ == "__main__":
	main()
