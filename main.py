import heapq


def cable_connection_costs(cables):
    heapq.heapify(cables)

    costs = list()

    while len(cables) > 1:
        shortest1 = heapq.heappop(cables)
        shortest2 = heapq.heappop(cables)
        cost = shortest1 + shortest2
        costs.append(cost)

        heapq.heappush(cables, cost)

    return costs

cables = [1, 3, 5, 7, 1]
result = cable_connection_costs(cables)

print(f"Порядок з'єднання:\n", "->".join([str(order) for order in result]))
print(f"Мінімальні загальні витрати з'єднання всіх кабелів: {sum(result)}")
