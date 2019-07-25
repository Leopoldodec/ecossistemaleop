
import tweetstream
import sys
import unidecode

words = ["opera", "firefox", "safari"]
people = [123,124,125]
locations = ["-122.75,36.8", "-121.75,37.8"]
with tweetstream.FilterStream("leopoldo3", "twleopleop1978788888z", track=words,
                           follow=people, locations=locations) as stream:
    for tweet in stream:
        print("A")
