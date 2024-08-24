N, Q = map(int, input().split())
layers = []
requests = []
for i in range(N):
    layers.append([*map(int, input().split())])
for i in range(Q):
    R, V = map(int, input().split())
    requests.append([R - 1, V])

solution = dict()
for i in range(len(layers)):
    i_d, i_c = layers[i]
    if i not in solution:
        solution[i] = [[i, i_c]]
        max_d = i_d
        for j in range(i + 1, len(layers)):
            j_d, j_c = layers[j]
            if j_d > max_d:
                max_d = j_d
                solution[i].append([j, j_c])
        for j, v in enumerate(solution[i][1:]):
            solution[v[0]] = solution[i][j+1:]

for i, v in requests:
    total = 0
    for j, c in solution[i]:
        total += c
        if total >= v:
            print(j + 1)
            break
    if total < v:
        print(0)