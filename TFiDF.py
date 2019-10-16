import math
documents = [
    'The car is driven on the road.',
    'The truck is driven on the highway.'
]


total_dict = {}
for i in range(len(documents)):
    total_dict[i] = {}
    for word in documents[i].strip().split(' '):
        w = word.replace('.','').lower()
        total_dict[i][w] = total_dict[i].get(w,0) + 1
print(total_dict)
res_dict = {}

keys = set()
for i in range(len(documents)):
    keys = keys.union(total_dict[i].keys())
keys = list(keys)
tf = [[0] * len(documents) for _ in range(len(keys))]
df = [0] * len(keys)
length = [len(d.strip().split(' ')) for d in documents]
for i,k in enumerate(keys):
    count = 0
    for j,d in enumerate(documents):
        tf[i][j] += total_dict[j].get(k,0)*1.0/length[j]
        count += int(total_dict[j].get(k,0) > 0)
    df[i] = len(documents) * 1.0 / count


for i in range(len(keys)):
    for j in range(len(documents)):
        tf[i][j] *= math.log(df[i],10)

for i,k in enumerate(keys):
    print(k,tf[i])








