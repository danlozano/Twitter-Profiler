from AnalyzerResults import *
import re

class TweetAnalyzer(object):

	def __init__(self, tweets, fileName):
		self.tweets = tweets
		self.keyWordCount = 0
		self.tweetCount = 0
		self.finalScore = 0

		self.dictionary = {}
		self.__parseFile__(fileName)

		self.results = AnalyzerResults(self.dictionary.keys())
		self.__analyze__()	

	def __parseFile__(self, fileName):
		f = open(fileName,'r')
		for line in f:
			if line[:1] == '+':
				category = line[1:].rstrip()
				keyWords = set()
				self.dictionary[category] = keyWords
			elif line[:1] == '-':
				self.dictionary[category].add(line[1:].rstrip())
			else:
				pass

		f.close()

	def __findWholeWord__(self, word):
		return re.compile(r'\b({0})\b'.format(word), flags=re.IGNORECASE).search

	def getResults(self):
		return self.results
		

class EmotionAnalyzer(TweetAnalyzer):
 
	def __analyze__(self):
		for tweet in self.tweets:
			for category in self.dictionary.keys():
				for keyWord in self.dictionary[category]:
					if keyWord in tweet:
						self.results.setScore(category, (self.results.getScore(category) + 1))
						self.results.addKeyWord(category, keyWord)
						self.keyWordCount = self.keyWordCount + 1
		
		for category in self.dictionary.keys():
			if self.results.getScore(category) > 0:
				gradedScore = (float(self.results.getScore(category)) / float(self.keyWordCount)) * 100
				self.results.setScore(category, int(gradedScore))	


class PsychopathyAnalyzer(TweetAnalyzer):

	def __analyze__(self):
		for tweet in self.tweets:
			self.tweetCount = self.tweetCount + 1
			for category in self.dictionary.keys():
				for keyWord in self.dictionary[category]:
					if category == 'Disfluencies' or 'Narcisism':
						if self.__findWholeWord__(keyWord)(tweet) != None:
							self.results.setScore(category, (self.results.getScore(category) + 1))
							self.results.addKeyWord(category, keyWord)
							self.keyWordCount = self.keyWordCount + 1
					else:
						if keyWord in tweet:
							self.results.setScore(category, (self.results.getScore(category) + 1))
							self.results.addKeyWord(category, keyWord)
							self.keyWordCount = self.keyWordCount + 1

		for category in self.dictionary.keys():
			if self.results.getScore(category) > 0:
				self.finalScore = self.finalScore + self.results.getScore(category)

		self.finalScore = (float(self.finalScore) / float(self.tweetCount)) * 100

		self.results.setFinalScore(self.finalScore)


class SpiritualAnalyzer(TweetAnalyzer):

	def __analyze__(self):
		for tweet in self.tweets:
			self.tweetCount = self.tweetCount + 1
			for category in self.dictionary.keys():
				for keyWord in self.dictionary[category]:
						if keyWord in tweet:
							self.results.setScore(category, (self.results.getScore(category) + 1))
							self.results.addKeyWord(category, keyWord)
							self.keyWordCount = self.keyWordCount + 1

		for category in self.dictionary.keys():
			if self.results.getScore(category) > 0:
				self.finalScore = self.finalScore + self.results.getScore(category)


		self.results.setFinalScore(self.finalScore)


class ConsumerAnalyzer(TweetAnalyzer):

	def __analyze__(self):
		for tweet in self.tweets:
			self.tweetCount = self.tweetCount + 1
			for category in self.dictionary.keys():
				for keyWord in self.dictionary[category]:
						if keyWord in tweet:
							self.results.setScore(category, (self.results.getScore(category) + 1))
							self.results.addKeyWord(category, keyWord)
							self.keyWordCount = self.keyWordCount + 1

		


		




		