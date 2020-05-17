import praw
import string

class words_dict:

    def __init__(self, submission):
        """
        Initializes the ADT

        submission : submission() class from praw
        """
        self.submission = submission

        # Dictionary key: Word
        # Dectionary value: amount of this word in comments
        self.negative = dict()
        self.positive = dict()

        # Two files are required
        with open("negative-words.txt", "r") as f:
            self.negative_words = f.read()
        with open("positive-words.txt", "r") as f:
            self.positive_words = f.read()

    def get(self):
        """
        Returns two dictionaries
        First with Positive words
        Second with Negative words

        return : dict(), dict()
        """
        # Get all words
        words = self._simplify()
        for word in words:
            if self._negative(word):
                if word not in self.negative:
                    self.negative[word] = 1
                else:
                    self.negative[word] += 1

            elif self._positive(word):
                if word not in self.positive:
                    self.positive[word] = 1
                else:
                    self.positive[word] += 1

        return self.positive, self.negative

    def _simplify(self):
        """
        Reads all comments from a submission
        Returns a list with all words

        return : list()
        """
        submissionList = []
        temp = self.submission
        temp.comments.replace_more(limit=None)
        for comment in temp.comments.list():
            submissionList.append(comment.body)
        words_list = []
        for comment in submissionList:
            replacement = string.punctuation.replace("-", "")
            comment = comment.translate(str.maketrans('', '', replacement))
            res = comment.split()
            for i in res:
                words_list.append(i.lower())
        return words_list

    def _negative(self, word):
        """
        Determines if word is negative

        word : str()
        return : bool()
        """
        if self.search("negative-words.txt", word):
            return True
        return False

    def _positive(self, word):
        """
        Determines if word is positive

        word : str()
        return : bool()
        """
        if self.search("positive-words.txt", word):
            return True
        return False

    def search(self, file, word):
        with open(file, "r") as f:
            for line in f:
                if line[:-1] == word:
                    return True
            return False
