# UnionFind
# find(p) -> group number
# connected(p,q) -> bool is connected
# union(p,q) -> None, add connection p,q

# 1. Quick Find:


class UnionFind1:
    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.length = n
        self.count = n

    def find(self, p):
        return self.id[p]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        if self.connected(p, q):
            return
        pid = self.find(p)
        qid = self.find(q)
        for i in range(self.length):
            if self.id[i] == pid:
                self.id[i] = qid
        self.count -= 1

    def count(self):
        return self.count()


# 2. Quick Union:
# Use tree to organize nodes
class UnionFind2:
    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.length = n
        self.count = n

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        pid = self.find(p)
        qid = self.find(q)
        if pid == qid:
            return
        self.id[pid] = qid
        self.count -= 1

    def count(self):
        return self.count()


# 3. Quick Union + Weighted Average:
# Maintain a size array
class UnionFind3:
    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.length = n
        self.count = n

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        pid = self.find(p)
        qid = self.find(q)
        if pid == qid:
            return
        if self.size[i] <= self.size[j]:
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[i] += self.size[j]
        self.count -= 1

    def count(self):
        return self.count()


# 4. Quick Union + Weighted Average + Update father node:
# modify find
class UnionFind4:
    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.length = n
        self.count = n

    def find(self, p):
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        pid = self.find(p)
        qid = self.find(q)
        if pid == qid:
            return
        if self.size[i] <= self.size[j]:
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[i] += self.size[j]
        self.count -= 1

    def count(self):
        return self.count()

# 5. Quick Union + Weighted Average + Update father node + Weight on Path:
# modify find
class UnionFind5:
    def __init__(self, n,):
        self.id = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.length = n
        self.count = n

    def find(self, p):
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        pid = self.find(p)
        qid = self.find(q)
        if pid == qid:
            return
        if self.size[i] <= self.size[j]:
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[i] += self.size[j]
        self.count -= 1

    def count(self):
        return self.count()


n = int(1e5)
m = int(1e5)
data = [i for i in range(n)]
connections = []
import random
import time
import tqdm

for k in range(m):
    i = random.randint(0, n-1)
    j = random.randint(0, n-1)
    if i != j:
        connections.append((i,j))

print(len(connections))

# union

for obj in [UnionFind4(n)]:
    start = time.time()
    for i, j in tqdm.tqdm(connections):
        obj.union(i, j)
    print('union for ' + str(obj) + 'cost ' + str((time.time() - start) * 1000) + ' ms')
    start = time.time()
    # find
    for i in tqdm.tqdm(range(n)):
        obj.find(i)
    print('find for ' + str(obj) + 'cost ' + str((time.time() - start) * 1000) + ' ms')
    print('=========================================================================')
