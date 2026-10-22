class wordNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
"""
Word Dictionary
- implement a trie structure:
    - each node will have a hash map of characters where a character will 
initialize function
- start the creation of a word dictionary
- initialize a word node

add word function:
- takes in a string and appends it to the word dictionary
    - start at a
search function:
- takes in the string and traverses to see if the word is in the dictionary
- dots can be matched with any letter
- there will be at most 2 dots in the word

    psuedo code:
        - start at root
        - traverse word to see if the character is in the dictionary:
            - if c != "." and c not in current trie route:
                return False
            - elif c == "."
            cur = cur.children[c]
        return 

"""
class WordDictionary:

    def __init__(self):
        self.root = wordNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = wordNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord

        return dfs(0, self.root)


