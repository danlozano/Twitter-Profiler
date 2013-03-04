import tweepy
import urlparse

class TweetApi(object):
    
	consumer_key = 'xoBcJ3vxOupUH4UU1qQ'
	consumer_secret = '7k6rMdwZiNt3HPTG9UDUBD4c12CS7gYjQl2k8yktsM'
	access_key = '41409259-JPgTHt9sTrraaS2n6xYvqg0G3PfLfUmlsxfCLSTPt'
	access_secret = '9rkpx8hBr8RaCIvsRti1opfrPJfWA3mYBlkiafEU'
    
	def __init__(self, userName):
        
		self.userName = userName
        
		self.auth = tweepy.OAuthHandler(TweetApi.consumer_key, TweetApi.consumer_secret)
		self.auth.set_access_token(TweetApi.access_key, TweetApi.access_secret)
		self.api = tweepy.API(self.auth)
        
		self.tweetCount = 0
		self.pageList = []
		self.tweetList = []

		self.remainingApiHits = self.api.rate_limit_status()['remaining_hits']
    
	def __encode__(self, text):
		return text.encode('utf-8')

	def __updateRemainingApiHits__(self):
		self.remainingApiHits = self.api.rate_limit_status()['remaining_hits']
    
	def getTweets(self, pageCount):

		self.__updateRemainingApiHits__()
		if self.remainingApiHits <= 16:
			raise Exception('Rate limit exceeded. Clients may not make more than 350 requests per hour.')

		try:
			for page in tweepy.Cursor(self.api.user_timeline, screen_name = self.userName, count = 200).pages(pageCount):
				self.pageList.append(page)
		except:
			raise
        
		for page in self.pageList:
			for tweet in page:
				tweetString = tweet.text
				newString = ''

				for i in tweetString.split():
					s, n, p, pa, q, f = urlparse.urlparse(i)

					if s and n:
						pass
					elif i[:1] == '@':
						pass
					elif i[:1] == '#':
						newString = newString.strip() + ' ' + i[1:]
					else:
						newString = newString.strip() + ' ' + i

				self.tweetList.append(self.__encode__(newString.lower()))
				self.tweetCount = self.tweetCount + 1
        
		return self.tweetList, self.tweetCount, self.remainingApiHits
		




