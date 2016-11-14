"""
a simple command line application that consumes a Public API using a HTTP client library
"""

#import statements
from googlemaps import GoogleMaps
from HTMLParser import HTMLParser
from sys import argv

class MLStripper(HTMLParser):
	def __init__(self):
		self.reset()
		self.fed = []
	
	def handle_data(self, d):
		self.fed.append(d)
		
	def get_data(self):
		return ''.join(self.fed)
		
def strip_tags(html):
	s = MLStripper()
	s.feed(html)
	return s.get_data()

class GoogleMapsError(Exception):
	"""Base class for errors in the :mod:`googlemaps` module.
    Methods of the :class:`GoogleMaps` raise this when something goes wrong.
    """
    G_GEO_SUCCESS               = 200
    G_GEO_SERVER_ERROR          = 500
    G_GEO_MISSING_QUERY         = 601
    G_GEO_UNKNOWN_ADDRESS       = 602
    G_GEO_UNAVAILABLE_ADDRESS   = 603
    G_GEO_BAD_KEY               = 610
    G_GEO_TOO_MANY_QUERIES      = 620   

    _STATUS_MESSAGES = {
        G_GEO_SUCCESS               : 'G_GEO_SUCCESS',
        G_GEO_SERVER_ERROR          : 'G_GEO_SERVER_ERROR',
        G_GEO_MISSING_QUERY         : 'G_GEO_MISSING_QUERY',
        G_GEO_UNKNOWN_ADDRESS       : 'G_GEO_UNKNOWN_ADDRESS',
        G_GEO_UNAVAILABLE_ADDRESS   : 'G_GEO_UNAVAILABLE_ADDRESS',
        G_GEO_BAD_KEY               : 'G_GEO_BAD_KEY',
        G_GEO_TOO_MANY_QUERIES      : 'G_GEO_TOO_MANY_QUERIES',
}
	def __init__(self, status, url+None, response=None):
		Exception.__init__(self, status)
		self.status = status
		self.response = response
		self.url = url
	
	def __str__(self):
		if self.status in self.__STATUS_MESSAGES:
			if self.response is not None and 'responseDetails' in self.response:
				retrival = 'Error %d: %s' %(self.status, self.response['responseDetails'])
			else:
                                retrival = 'Error %d: %s' % (self.status, status._STATUS_MESSAGES[self.status])
			else:
				retrival = str(self.status)
			return retrival
			
        def __unicode__(self):
                return unicode(self.__str__())
        

mapService = GoogleMaps() #create GoogleMaps objects

directions = mapService.directions(argv[1], argv[2]) #get directions from google

for step in directions['Directions']['Routes'][0]['Steps']: #print each step in directions to console
	print strip_tags(step['descriptionHtml'])
