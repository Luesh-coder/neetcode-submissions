class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        prereq[i] = [a, b] where course b must be take if one wants to take course a

        numCourses are total number of courses required to take, 0-indexed number. Ex: numCourses = 2 has courses labeled "0, 1"

        must return True if possible to finish all courses, otherwise False

        Each course is a node, then each prereq is a directed edge. You can finish all courses only no cycle is included

        Utilize DFS with cycle detection:
            - while DFS, keep track of courses in current recursion path
            - if visit courese already in current path -> cycle found
            - if course has no prereq left, is safe
        """
          # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the current DFS path
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                # Cycle detected
                return False
            if crs == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True