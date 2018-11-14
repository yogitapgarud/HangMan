import random

class HangmanLexicon:

    def getWordCount(self):
        return 10

    def getWord(self,index):

        words = ["BUOY", "COMPUTER", "CONNOISSEUR", "DEHYDRATE", "FUZZY", "HUBBUB", "KEYHOLE", "QUAGMIRE", "SLITHER", "ZIRCON"]

        n = len(words)

        assert index < n and index >= 0

        return words[index]

print("Welcome to Hangman!")

hangman = HangmanLexicon()

w = hangman.getWord(random.randint(0,hangman.getWordCount()))
s = ['-'] * len(w)

print "The word now looks like this: " + ''.join(s)
print("You have 8 guesses left.")

x = raw_input("Make a guess.")
print("Your guess: ", x.upper())
