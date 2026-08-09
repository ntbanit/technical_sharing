def solution(alp, cop, problems):
    max_alp_req = 0
    max_cop_req = 0
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems :
        max_alp_req = max(max_alp_req, alp_req)
        max_cop_req = max(max_cop_req, cop_req)
    
    output = float('inf')
    dp = [[float('inf')] * (max_cop_req + 1) for _ in range(max_alp_req + 1)]
    def dfs(a, c, time) :
        nonlocal output
        if time >= output :
            return
        if time >= dp[a][c] : # already reached this state, cheaper or equal
            return 
        
        dp[a][c] = time
        if a >= max_alp_req and c >= max_cop_req :
            output = min(output, time)
            return
        if a < max_alp_req :
            dfs(a + 1, c, time + 1)
        if c < max_cop_req :
            dfs(a, c + 1, time + 1)
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems :
            if a >= alp_req and c >= cop_req :
                na = min(max_alp_req, a + alp_rwd)
                nc = min(max_cop_req, c + cop_rwd)
                dfs(na, nc, time + cost)
    
    alp = min(alp, max_alp_req)
    cop = min(cop, max_cop_req)
    dfs(alp, cop, 0)
    return output

# testcase 1
print(solution(
      10
    , 10
    , [
        [10, 15, 2, 1, 2]
      , [20, 20, 3, 3, 4]
      ]
    )
) # return 15

# testcase 2
print(solution(
      10
    , 10
    , [
        [0,0,2,1,2]
      , [4,5,3,1,2]
      , [4,11,4,0,2]
      , [10,4,0,4,2]
      ]
    )
) # return 13
