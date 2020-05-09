import praw

class words_dict:

    def __init__(self, submission):
        self.submission = submission
        self.negative = dict()
        self.positive = dict()
        self.negative_words = open("negative-words.txt", "r").read()
        self.positive_words = open("positive-words.txt", "r").read()

    def get(self):
        words = self._simplify()
        for word in words:
            if self._negative(word):
                if not word in self.negative:
                    self.negative[word] = 1
                else:
                    self.negative[word] += 1
            elif self._positive(word):
                if not word in self.positive:
                    self.positive[word] = 1
                else:
                    self.positive[word] += 1
        return self.positive, self.negative

    def _simplify(self):
        self.submission.comments.replace_more(limit=None)
        words = []
        for word in self.submission.comments.list():
            words.append(word)
        return words

    def _negative(self, word):
        if word in self.negative_words:
            return True
        return False

    def _positive(self, word):
        if word in self.positive_words:
            return True
        return False