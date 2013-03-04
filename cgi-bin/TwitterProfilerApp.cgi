#!/home2/cucharad/python/bin/python

try:
    import traceback, sys, os, cgi
    # The following makes errors go to HTTP client's browser
    # instead of the server logs.
    sys.stderr = sys.stdout
    #cgi.test()
except Exception, e:
    print 'Content-type: text/html\n'
    print
    print '&lt;html&gt;&lt;head&gt;&lt;title&gt;'
    print str(e)
    print '&lt;/title&gt;'
    print '&lt;/head&gt;&lt;body&gt;'
    print '&lt;h1&gt;TRACEBACK&lt;/h1&gt;'
    print '&lt;pre&gt;'
    traceback.print_exc()
    print '&lt;/pre&gt;'
    print '&lt;/body&gt;&lt;/html&gt;'

from PsychController import *
from AnalyzerResults import *
import json

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers

form = cgi.FieldStorage()
userName = form.getvalue("userName")

try:
    controller = PsychController(userName)
    emotionResults, psychopathyResults, spiritualResults, consumerResults, tweetCount, remainingApiHits = controller.getResults()

    jsonResponse = {'emotionResults': emotionResults.getDict(), 'psychopathyResults': psychopathyResults.getDict(), 
    'spiritualResults': spiritualResults.getDict(), 'consumerResults': consumerResults.getDict(),
    'tweetCount': tweetCount, 'remainingApiHits': remainingApiHits}

    jsonResponse = json.dumps(jsonResponse)

    print jsonResponse

except Exception, e:
    
    if e == 'Rate limit exceeded. Clients may not make more than 350 requests per hour.':
        reason = 'rateLimit'
    else:
        reason = 'userError'

    jsonResponse = {'error': reason}
    jsonResponse = json.dumps(jsonResponse)
    print jsonResponse
			