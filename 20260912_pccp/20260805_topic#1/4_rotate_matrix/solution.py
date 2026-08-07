def solution(rows, columns, queries):
    grid = [[0] * columns for _ in range(rows)]
    k = 1
    for i in range(rows):
        for j in range(columns):
            grid[i][j] = k
            k += 1

    def rotate(x0, y0, x1, y1):
        x0 -= 1
        y0 -= 1
        x1 -= 1
        y1 -= 1
        values = []
        positions = []
        for y in range(y0, y1 + 1):
            positions.append((x0, y))
            values.append(grid[x0][y])

        for x in range(x0 + 1, x1 + 1):
            positions.append((x, y1))
            values.append(grid[x][y1])
            
        for y in range(y1 - 1, y0 - 1, -1):
            positions.append((x1, y))
            values.append(grid[x1][y])
        
        for x in range(x1 - 1, x0, -1):
            positions.append((x, y0))
            values.append(grid[x][y0])
        
        index = 1
        N = len(values)
        for i in range(N):
            x, y = positions[index % N]
            grid[x][y] = values[i] 
            index += 1
        
        # print(positions)
        # print(values)
        cur_min = min(values)
        return cur_min
        
    # if rows == columns == 6 :
    #     print(f"rotate={rotate(2, 2, 5, 4)}")
    #     print(grid)
    answer = []
    for x0, y0, x1, y1 in queries :
        answer.append(rotate(x0, y0, x1, y1))
    
    return answer