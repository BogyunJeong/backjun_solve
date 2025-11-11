from collections import defaultdict
import heapq

def dijkstra(graph,start,mStopover):
	pq = [(-30005,start)]
	v = len(graph)
	distance = [-1] * v

	while(pq):
		cur_cost,cur_node = heapq.heappop(pq)

		if distance[cur_node] != -1:
			return
		distance[cur_node] = -cur_cost

		for v,n in graph[cur_node]:
			dist = min(-v,cur_cost)
			heapq.heappush(pq,(-dist,n))


def init(N, K, sCity, eCity, mLimit):
	global graph,_N
	_N = N
	graph = defaultdict(list)
	for i in range(K):
		add(sCity[i],eCity[i],mLimit[i])


def add(sCity, eCity, mLimit):
	graph[sCity].append((mLimit,eCity))
	graph[eCity].append((mLimit,sCity))


def calculate(sCity, eCity, M, mStopover):
	mStopover.append(eCity)

	dist = dijkstra(graph,sCity,mStopover)

	if max([dist[idx] for idx in mStopover]) == 30005:
		return -1
	return