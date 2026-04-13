
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return

        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        elif self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1

    def groups(self):
        result = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in result:
                result[root] = []
            result[root].append(i)
        return result



uf = UnionFind(10)
print("Initial groups: ", uf.groups())
# {0: [0], 1: [1], 2: [2], 3: [3], 4: [4], 5: [5], 6: [6], 7: [7], 8: [8], 9: [9]}

uf.union(0, 1)
uf.union(1, 2)
print("New groups: ", uf.groups())
# {0: [0, 1, 2],   3: [3], 4: [4],   5: [5],   6: [6],   7: [7],   8: [8],   9: [9]}

uf.union(3, 4)
uf.union(4, 5)
uf.union(6, 7)
print("New groups: ", uf.groups())
# {0: [0, 1, 2],   3: [3, 4, 5],   6: [6, 7],   8: [8],   9: [9]}

uf.union(2, 5)
print("New groups: ", uf.groups())
# {0: [0, 1, 2, 3, 4, 5],   6: [6, 7],   8: [8],   9: [9]}

print("find(0):", uf.find(0))   # 0
print("find(4):", uf.find(4))   # 0
print("find(7):", uf.find(7))   # 6