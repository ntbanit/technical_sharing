N = 3
result = [0] * N

def gen_bin(index):
    if index == N:
        print(result)
        return
    
    for value in range(2):
        result[index] = value
        gen_bin(index + 1)
        result[index] = -1

gen_bin(0)
