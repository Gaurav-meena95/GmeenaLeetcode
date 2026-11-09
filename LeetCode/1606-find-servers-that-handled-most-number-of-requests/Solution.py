from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free_server = SortedList(range(k))
        busy_server = []
        count = [0] * k
        n = len(arrival)
        for i in range(n):
            t = arrival[i]
            while busy_server and busy_server[0][0] <= t:
                free_server.add(heapq.heappop(busy_server)[1])
            if not free_server:
                continue
            pref = i % k
            idx = free_server.bisect_left(pref)
            if idx == len(free_server):
                idx = 0
            s = free_server[idx]
            free_server.pop(idx)
            count[s] += 1
            heapq.heappush(busy_server, (t + load[i], s))
        mx = max(count)
        return [i for i in range(k) if count[i] == mx]