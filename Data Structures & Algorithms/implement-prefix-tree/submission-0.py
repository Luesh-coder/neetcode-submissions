class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    """
    Hash Map version

    Data Strucutre:
        - each node contains:
            children[26]: array of child pointers (one for each letter)
            endOfWord: marks completion of a word
    
    Insert(word):
        - start from root
        - for each character in the word:
            - convert character to index (c - 'a')
            - if the child node doesn't exit, create it
            - move to the child
        - after processing all characters, mark endOfWord = true
    
    Search(word):
        - start from the root
        - For each character:
            - move to the corresponding child
            - if missing, return False
        - After Traversal:
            - Return True only if endOfWord is true
    
    StartsWith(prefix):
        - start from the root
        - Traverse characters of the prefix
        - If all characters exist in sequence, return True
        - No need to check endOfWord
    
    """
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]  = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
    
        