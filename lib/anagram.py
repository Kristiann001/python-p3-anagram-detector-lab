# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        matches = []
        for anagram in possible_anagrams:
            if self.is_anagram(anagram.lower()):
                matches.append(anagram)
        return matches

    def is_anagram(self, candidate):
        if candidate == self.word:
            return False  # Exclude the word itself
        return sorted(candidate) == sorted(self.word)
