class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        visit = set()
        for edge in prerequisites:
            if edge[1] in adj:
                adj[edge[1]].append(edge[0])
            else:
                adj[edge[1]] = [edge[0]]
            if edge[0] not in adj:
                adj[edge[0]] = []
        
        def dfs(key, smallVis):
            if key in visit:
                return True
            if key in smallVis:
                return False
            res = True
            smallVis.add(key)
            for next in adj[key]:
                res = res and dfs(next, smallVis)
            visit.add(key)
            return res
        
        for key in adj:
            if not dfs(key, set()):
                return False
        return True