N = 4
K = 2
result = [0] * K
visited = [False] * (N + 1)

def gen_comb(index):
    if index == K:
        print(result)
        return
    
    for value in range(1, N + 1):
        if visited[value]:
            continue

        visited[value] = True
        result[index] = value
        gen_comb(index + 1)
        visited[value] = False

gen_comb(0)
