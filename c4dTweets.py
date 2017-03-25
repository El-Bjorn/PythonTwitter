#!/usr/bin/python

import twitter
import os
import urllib
import string

avatarDir = 'Avatars'
tweetDir = 'Tweets'

def createSubDirs():
	if not os.path.exists(avatarDir):
		os.mkdir(avatarDir,0777)
	if not os.path.exists(tweetDir):
		os.mkdir(tweetDir,0777)
	return

def writeToTweetFile(user,content):
	filename = tweetDir+'/'+user+'.txt'
	print filename
	tweetFile = open(filename,'w')
	tweetFile.write(content.encode('utf8'))
	tweetFile.close
	return

def writeAvatarImg(user,avatURL):
	print "user:"+user
	print "avatURL: "+avatURL
	filext = string.split(avatURL,'.')[-1]
	if filext != "jpg" and filext != "jpeg" and filext != "png":
		return
	print "filext: "+filext
	filename = avatarDir+'/'+user+'.'+filext
	print filename
	if not os.path.exists(filename):
		imgData = urllib.urlopen(avatURL).read()
		avatFile = open(filename,'wb')
		avatFile.write(imgData)
		avatFile.close
	return


def get_tweets(hashtag='#HalfRez'):
	api = twitter.Api("TVbgtvONWqVRnKZkI0HXEg","b07yuSJ8YdEmWrx4WgyC0bKA29yiUmt1CxJOnCmvkA","139188391-C6nykdUScsQZdyvWxDPGk2NMteusbquJUWzXdM8","tXqX0kftsJcEdjoIcd6NfyVRgzssoPj6resm5gtI4")
	statuses = api.GetSearch(hashtag)
	tList = []
	for s in statuses:
		tDict = {'id':s.id,'name':s.user.name}
		tDict['handle'] = string.replace(s.user.screen_name,'/','')
		tDict['imageURL'] = s.user.profile_image_url
		tDict['content'] = s.text
		tList.append(tDict)
		#testing
		print "writing out image"
		writeAvatarImg(tDict['handle'],tDict['imageURL'])
		print "writing tweet"
		writeToTweetFile(tDict['handle'],tDict['content'])
	return tList


def write_tweets(tweetList,filename='tweets.txt'):
	output = open(filename,'w')
	for t in tweetList:
		output.write(t['handle'])
		output.write('	')
		output.write(t['imageURL'])
		output.write('	')
		output.write(t['content'].encode('utf8'))
		#output.write(t['content'])
		output.write('\n------------------------------------\n')
	output.close
	return


def print_tweets(tweetList):
	for t in tweetList:
		print t['name']
		print t['handle']
		print t['imageURL']
		print t['content']
	return


print 'All your tweets are belong to us!' 

# testing
createSubDirs()
#writeAvatarImg("frankie","http://blabla/picOfrank.png")
#writeToTweetFile("benji","boobies!!!!!!!")


tweets = get_tweets('pickles')
write_tweets(tweets)
#print_tweets(tweets)
