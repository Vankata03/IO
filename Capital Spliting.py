def bellman(investment_opportunities, total_capital):
    dp = [[0 for x in range(total_capital + 1)] for y in range(investment_opportunities + 1)]

    # Execute Bellman's algorithm to find the optimal capital allocation
    for j in range(1, investment_opportunities + 1):
        for y in range(total_capital + 1):
            dp[j][y] = dp[j-1][y]
            for c in range(y + 1): 
                dp[j][y] = max(dp[j][y], R(j-1, c) + dp[j-1][y-c])

    # Find the investment opportunities that maximize the total benefit
    result = []
    remaining_capital = total_capital
    for j in range(investment_opportunities, 0, -1):
        if dp[j][remaining_capital] == dp[j-1][remaining_capital]:
            continue
        else:
            invested = None
            for c in range(remaining_capital + 1):
                if dp[j][remaining_capital] == R(j-1, c) + dp[j-1][remaining_capital-c]:
                    invested = c
                    break
            if invested is not None:
                result.append((j-1, invested))
                remaining_capital -= invested

    # Reverse the result to follow the investment chronology
    result.reverse()
    return dp[investment_opportunities][total_capital], result

def R(i, c):
    returns = {
        (1, 0): 0,
        (1, 1): 2,
        (1, 3): 5,
        (2, 0): 0,
        (2, 2): 3,
        (2, 3): 5,
        (2, 4): 6,
        (3, 0): 0,
        (3, 1): 2,
        (3, 2): 4,
        (3, 4): 6,
    }
    while c >= 0:
        if (i, c) in returns:
            return returns[(i, c)]
        c -= 1
    return 0

total_capital = 5
investment_opportunities = 4 

max_profit, investment_plan = bellman(investment_opportunities, total_capital)
print(f"Максималната възвращаемост: {max_profit}")
print(f"План за инвестиция: {investment_plan}")