class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(n):
            res = n

            while res!=par[res]:
                par[res] = par[par[res]]
                res = par[res]
            # print()
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # print(n1, n2, p1, p2)

            if p1==p2:
                return 1
            else:
                if rank[p1] > rank[p2]:
                    par[p2] = p1
                    rank[p1]+=rank[p2]

                else:
                    par[p1] = p2
                    rank[p2] +=rank[p1]

                return 0

        for n1, n2 in edges:
            if union(n1,n2):
                return [n1,n2]        