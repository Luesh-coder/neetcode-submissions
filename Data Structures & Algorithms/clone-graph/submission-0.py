"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        the graph may contain cycles, thus we can't simply copy nodes recursively without remembering what we've copied.

        To handle, we use a map(old -> new):
            - when we first see a node, we create its copy
            - if we see the same node again, we reuse the already-created copy
            - this avoids infinite loops and ensures each node is cloned exactly once
        
        Depth First Search (DFS) helps us explore and clone all connected nodes
        """

        if not node:
            return None
        
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node) if node else None
            