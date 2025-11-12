import heapq

INF = 21e9


def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    for a,b,c in paths:
        graph[a].append((c,b)) # 가중치, 노드 순으로 힙에 삽입
        graph[b].append((c,a))

    gate_set = set(gates)
    summit_set = set(summits)


    hq = []
    intensity = [INF] * (n+1)

    for gate in gates:
        heapq.heappush(hq,(0,gate))
        intensity[gate] = 0

    while hq:
        cur_intensity,node = heapq.heappop(hq)

        if cur_intensity > intensity[node]:
            continue
        
        if node in summit_set:
            continue

        for weight, next_node in graph[node]:
            if next_node in gate_set:
                continue

            new_intensity = max(cur_intensity,weight)

            if new_intensity < intensity[next_node]:
                intensity[next_node] = new_intensity
                heapq.heappush(hq,(new_intensity,next_node))
    result_summit = -1
    result_intensity = INF

    for summit in sorted(summits):
        if intensity[summit] < result_intensity:
            result_intensity = intensity[summit]
            result_summit = summit
    
    return [result_summit, int(result_intensity)]