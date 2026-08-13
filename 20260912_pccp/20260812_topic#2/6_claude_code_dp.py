def solution(alp, cop, problems):
    amax_req = cmax_req = 0
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems :
        amax_req = max(amax_req, alp_req)
        cmax_req = max(cmax_req, cop_req)
        
    dp = [[float('inf')] * (cmax_req + 1) for _ in range(amax_req + 1)]
    a_start = min(alp, amax_req)
    c_start = min(cop, cmax_req)
    dp[a_start][c_start] = 0
    for a in range(a_start, amax_req + 1):
        for c in range(c_start, cmax_req + 1):
            if dp[a][c] == float('inf') :
                continue
            # study coding
            if c < cmax_req and dp[a][c] + 1 < dp[a][c + 1]:
                dp[a][c + 1] = dp[a][c] + 1
            # study algorithm
            if a < amax_req and dp[a][c] + 1 < dp[a + 1][c]:
                dp[a + 1][c] = dp[a][c] + 1
            # solve problems
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems :
                if a >= alp_req and c >= cop_req :
                    anew = min(a + alp_rwd, amax_req)
                    cnew = min(c + cop_rwd, cmax_req)
                    if dp[a][c] + cost < dp[anew][cnew]:
                        dp[anew][cnew] = dp[a][c] + cost
            
    return dp[amax_req][cmax_req]