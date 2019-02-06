# A -> 65
# Z -> 90
class TrieNode:
    def __init__(self, v=None):
        self.children = [None]*26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        it = self.root
        word_length = len(word)

        for level in range(word_length):
            index = ord('A') - ord(word[level].upper())

