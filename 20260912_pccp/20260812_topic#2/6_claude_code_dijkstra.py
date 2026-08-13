import heapq

def solution(alp, cop, problems):
    max_alp_req = 0
    max_cop_req = 0
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp_req = max(max_alp_req, alp_req)
        max_cop_req = max(max_cop_req, cop_req)
    
    start_a = min(alp, max_alp_req)
    start_c = min(cop, max_cop_req)
    
    dist = [[float('inf')] * (max_cop_req + 1) for _ in range(max_alp_req + 1)]
    dist[start_a][start_c] = 0
    pq = [(0, start_a, start_c)]
    
    while pq:
        time, a, c = heapq.heappop(pq)
        if time > dist[a][c]:
            continue  # stale entry, skip
        if a >= max_alp_req and c >= max_cop_req:
            return time
        
        # study alp
        if a < max_alp_req:
            na, nc, nt = a + 1, c, time + 1
            if nt < dist[na][nc]:
                dist[na][nc] = nt
                heapq.heappush(pq, (nt, na, nc))
        # study cop
        if c < max_cop_req:
            na, nc, nt = a, c + 1, time + 1
            if nt < dist[na][nc]:
                dist[na][nc] = nt
                heapq.heappush(pq, (nt, na, nc))
        # solve a problem
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if a >= alp_req and c >= cop_req:
                na = min(max_alp_req, a + alp_rwd)
                nc = min(max_cop_req, c + cop_rwd)
                nt = time + cost
                if nt < dist[na][nc]:
                    dist[na][nc] = nt
                    heapq.heappush(pq, (nt, na, nc))
    
    return dist[max_alp_req][max_cop_req]