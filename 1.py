import heapq

def min_cost(cables):
  
    heapq.heapify(cables)
    
    total_cost = 0

    while len(cables) > 1:
        first  = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second
        total_cost += cost

        heapq.heappush(cables, cost)
    return total_cost

cables = [9, 3, 2, 6, 2, 5]
result = min_cost(cables)
print(f"Мінімальні витрати: {result}")
