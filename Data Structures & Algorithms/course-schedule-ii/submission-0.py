class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visit = set()
        ans = []
        completed = set()

        def dfs(crs):
            if crs in visit:
                return False
            
            if crs in completed:
                return True
            
            if preMap[crs] == [] and crs not in completed:
                ans.append(crs)
                completed.add(crs)
                return True

            visit.add(crs)
            for pre in preMap[crs]:
               if not dfs(pre): return False
            
            visit.remove(crs)
            preMap[crs] = []
            ans.append(crs)
            completed.add(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
            
        
        return ans
