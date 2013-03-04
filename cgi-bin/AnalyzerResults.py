class AnalyzerResults(object):

	def __init__(self, categories):
		self.results = {}
		self.finalScore = 0

		for category in categories:
			score = 0
			keyWords = {}
			attributes = {'score': score, 'keyWords': keyWords}
			self.results[category] = attributes

	def setFinalScore(self, finalScore):
		self.finalScore = finalScore

	def getFinalScore(self):
		return self.finalScore

	def getCategories(self):
		return self.results.keys()

	def getScore(self, category):
		return self.results[category]['score']

	def setScore(self, category, score):
		self.results[category]['score'] = score		

	def getKeyWords(self, category):
		return self.results[category]['keyWords']

	def addKeyWord(self, category, word):
		if not(word in self.results[category]['keyWords']):
			self.results[category]['keyWords'][word] = 1
		else:
			self.results[category]['keyWords'][word] = self.results[category]['keyWords'][word] + 1

	def getDict(self):
		 return {'results': self.results, 'finalScore': self.finalScore}
		

		


