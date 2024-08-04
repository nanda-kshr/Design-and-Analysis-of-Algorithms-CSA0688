def champagne_tower(poured, query_row, query_glass):
    dp = [[0] * k for k in range(1, 102)]
    dp[0][0] = poured
    for r in range(query_row + 1):
        for c in range(r + 1):
            if dp[r][c] > 1:
                dp[r + 1][c] += (dp[r][c] - 1) / 2.0
                dp[r + 1][c + 1] += (dp[r][c] - 1) / 2.0
                dp[r][c] = 1
    return min(1, dp[query_row][query_glass])
print(champagne_tower(1, 1, 1))
print(champagne_tower(2, 1, 1))