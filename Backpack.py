def knapsack(W, weights, values, n, multiple_items_allowed):
    dp = [[0 for w in range(W + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                if multiple_items_allowed:
                    dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i][w - weights[i - 1]])
                else:
                    dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    res = dp[n][W]
    w = W
    items_selected = []
    i = n

    while i > 0 and res > 0:
        if multiple_items_allowed:
            while i > 0 and dp[i][w] == dp[i][w - weights[i - 1]] + values[i - 1]:
                items_selected.append(i)
                w -= weights[i - 1]
                res -= values[i - 1]
        else:
            if dp[i][w] != dp[i - 1][w]:
                items_selected.append(i)
                res -= values[i - 1]
                w -= weights[i - 1]
        i -= 1

    items_count = {}
    for item in items_selected:
        if item in items_count:
            items_count[item] += 1
        else:
            items_count[item] = 1

    return dp[n][W], items_count


W = 600
weights = [150, 160, 220, 120, 80]
values = [45, 50, 70, 40, 30]
n = 5
multiple_items_allowed = True

max_costs, items_in_knapsack = knapsack(W, weights, values, n, multiple_items_allowed)
print("Максималната цена на раницата е: ", max_costs)
print("Продуктите и техният брой, които се включват в раницата са: ", items_in_knapsack)
