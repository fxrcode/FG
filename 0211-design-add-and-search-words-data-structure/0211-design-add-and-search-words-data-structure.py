class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = 0
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()      

    def addWord(self, word):
        root = self.root
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
        root.end_node = 1
        
    def search(self, word):
        def dfs(node, i):
            if i == len(word): return node.end_node
               
            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i+1): return True
                    
            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)
            
            return False
    
        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)