class Node:

    def __init__(self) -> None:
        self.ch = ''
        self.is_word = False
        self.children = defaultdict(Node)

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        ptr = self.root
        for c in word:
            ptr = ptr.children[c]
        ptr.is_word = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for i, ch in enumerate(word):
            if not ch in ptr.children:
                return False
            ptr = ptr.children[ch]
        return ptr.is_word

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for ch in prefix:
            if ch not in ptr.children:
                return False
            ptr = ptr.children[ch]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)