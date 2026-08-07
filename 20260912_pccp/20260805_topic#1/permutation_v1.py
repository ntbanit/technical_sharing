N = 4
result = [0] * N
visited = [False] * N

def gen_pem(index):
    if index == N:
        print(result)
        # check condition, count result 
        return
    
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        result[index] = i + 1

        gen_pem(index + 1)

        visited[i] = False

gen_pem(0)

