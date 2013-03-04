from AnalyzerResults import *
from TweetAnalyzer import *
from TweetApi import *

class PsychController(object):

	def __init__(self, userName):

		self.twApi = TweetApi(userName)
		try:
			self.tweets, self.tweetCount, self.remainingApiHits = self.twApi.getTweets(16)
		except:
			raise

		self.emotionAnalyzer = EmotionAnalyzer(self.tweets, 'Resources/EmotionAnalyzer.txt')
		self.emotionResults = self.emotionAnalyzer.getResults()

		self.psychopathyAnalyzer = PsychopathyAnalyzer(self.tweets, 'Resources/PsychopathyAnalyzer.txt')
		self.psychopathyResults = self.psychopathyAnalyzer.getResults()

		self.spiritualAnalyzer = SpiritualAnalyzer(self.tweets, 'Resources/SpiritualAnalyzer.txt')
		self.spiritualResults = self.spiritualAnalyzer.getResults()

		self.consumerAnalyzer = ConsumerAnalyzer(self.tweets, 'Resources/ConsumerAnalyzer.txt')
		self.consumerResults = self.consumerAnalyzer.getResults()
			

	def getResults(self):	
		return self.emotionResults, self.psychopathyResults, self.spiritualResults, self.consumerResults, self.tweetCount, self.remainingApiHits

