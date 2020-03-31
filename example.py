import praw
# !WARNING!
# This code is not meant to work without inputting parameters
# I`m not putting them in because they hold confidential info (username, password, client id and secret)
def bot_login():
	print "Logging in..."
	username = "RedditUsername"
	password = "password"
	client_id = "idGoesHere"
	client_secret = "secretGoesHere"
	my_info = praw.Reddit(username = username,
				password = password,
				client_id = client_id,
				client_secret = client_secret,
				user_agent = "Some item v1.0")
	print "Logged in!"
	return my_info

if __name__ == "__main__":
	bot_login()
