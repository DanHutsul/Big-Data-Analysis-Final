from words_dict import words_dict
import praw
from mega import Mega


def main():
    # Log in
    print('Authenticating...\n')
    reddit = praw.Reddit('bot', user_agent='positive_counter_bot')
    print(f'Authenticated as {reddit.user.me()}\n')

    # Confines the search to one subreddit
    # This is a test subreddit used to test bots
    # This is done to ease the demonstration and testing
    # This line will be changed in the future
    subreddit = reddit.subreddit("testingground4bots")

    for comment in subreddit.stream.comments():
        process_submission(comment)


def process_submission(comment):
    # Check for code phrase
    if "Positive_Counter_Bot" in comment.body:

        # Check if comment was already processed
        with open("processed_threads.txt", "r") as p:
            if str(comment.id) in p.read():
                print("Comment already processed, skipping")
                return 0
        print("Processing comment")
        # Add comment id to database
        with open("processed_threads.txt", "a") as p:
            p.write(str(comment.id) + "\n")

        # ADT use
        new_submission = words_dict(comment.submission)
        positive_words, negative_words = new_submission.get()

        # Counts amount of different words
        positive_points = 0
        for value in positive_words.values():
            positive_points += value
        negative_points = 0
        for value in negative_words.values():
            negative_points += value

        # Message construction
        message = ""
        if negative_points == 0:
            message += "This thread is so pure! I'm impressed guys. "
        elif positive_points >= negative_points:
            message += "This thread is quite positive. Good job guys! "
        else:
            message += "This thread is quite negative. This makes me sad. "
        message += "I've counted " + str(positive_points) \
            + " positive words and " + str(negative_points) + \
            " negative words in this post's comment thread"

        # Creating a file to save words to
        # Delete the old file
        with open('words.txt', 'w+') as f:
            f.write("")
        # Add words
        with open('words.txt', 'a') as f:
            f.write("Positive Words: ")
            for w, num in positive_words.items():
                f.write(w + " " + str(num) + "\n")
            f.write("Negative Words: ")
            for w, num in negative_words.items():
                f.write(w + " " + str(num) + "\n")

        # Uploading the file to Cloud
        mega = Mega()
        m = mega.login("positivitybot27@gmail.com", "thelegend27")
        words_file = m.upload("words.txt")
        url = m.get_upload_link(words_file)
        message += "\n\n[Link to all words file](" + url + ")"

        # This is a line for testing
        # Commented line is the final one
        print(message)
        comment.reply(message)

main()
