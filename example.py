import praw
import config
import time
import os

def bot_login():
	print "Logging in..."
	r = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "The Reddit Commenter v1.0")
	print "Logged in!"

	return r
