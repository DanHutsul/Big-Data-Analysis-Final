# Import the praw library
import praw

def main():
    # We create a new instance of Reddit
    reddit = praw.Reddit(
        # The 3 variables needed to log in
        # The program does not work in this state
        # as the values are dummies
        # You need to replace them with real ones to work
        user_agent="SOMEBOT (by /u/USERNAME)",
        client_id="CLIENT_ID",
        client_secret="CLIENT_SECRET",
        # The username and password make it possible
        # to use user features, like commenting
        username="USERNAME",
        password="PASSWORD"
    )
    # We get an instance of r/redditddev subreddit
    subreddit = reddit.subreddit("redditdev")
    # We then use this instance to access the comments on r/redditdev
    for comment in subreddit.stream.comments():
        reply_to_comment(comment)

def reply_to_comment(comment):
    normalized_title = comment.title.lower()
    # The if statement checks if the comment contains
    # the phrase
    # Most bots use their names as this minimises the chance
    # of a false call
    if "Hello World" in normalized_title:
        # .reply() makes a reply from the bot 
        comment.reply("Hello to you too!")

if __name__ == "__main__":
    main()