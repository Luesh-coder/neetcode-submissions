class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Depth First Search

        when we visit and cell that hasn't been visited, start a DFS to sink the entire island

        psuedo:
        Iterate through every cell
        when a cell with value '1' is found:
            - increment the island count
            - run DFS from that cell
        
        in DFS:
            - if the cell is out of bounds or is '0', return
            - mark the current cell as '0' (visited)
            - recursively explore every direction

        continue until all cells are processed
        return total island count  
        """

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0"):
                return
            
            grid[r][c] = "0"

            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        
        return islands
