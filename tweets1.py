#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "3094831522-tgA7HOeFZdKgMdmsjvgah7dg8nYBBZG4Tslw4nE"
access_token_secret = "r7yQGb3zHjJzTsZBk5Jd6gHYMkwlLpQO7VMpjQCz8MR3c" 
consumer_key = "JuIsPj0mn0ytDLjwgDC98uxja"
consumer_secret = "K5t8KSLptWc3XRpTyP3Xn969uI4Ndfq1I3qtaclMesrtiOwp9q"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    
    print 5

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['shared economy'])