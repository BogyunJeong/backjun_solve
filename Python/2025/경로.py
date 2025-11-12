from collections import defaultdict
import heapq

INF = 30005

def dijkstra(start, graph, N):
    pq = [(-INF,start)]
    distance = [-1] * _N
    distance[start] = INF

    while pq:
        cur_dist,cur_node = heapq.heappop(pq)

        if -cur_dist < distance[cur_node]:
            continue

        for d,n in graph[cur_node]:
            next_d = min(-cur_dist,d)
            if next_d > distance[n]:
                distance[n] = next_d
                heapq.heappush(pq,(-next_d,n))

    return distance



def init(N, K, sCity, eCity, mLimit):
    global graph, _N
    _N = N
    graph = defaultdict(list)
    for i in range(K):
        add(sCity[i], eCity[i], mLimit[i])


def add(sCity, eCity, mLimit):
    graph[sCity].append((mLimit, eCity))
    graph[eCity].append((mLimit, sCity))


def calculate(sCity, eCity, M, mStopover):

    targets = list(mStopover) + [eCity]

    dist = dijkstra(sCity, graph, _N)


    for idx in targets:
        if idx < 0 or idx > _N or dist[idx] == -1:
            return -1

    return min(dist[idx] for idx in targets)
