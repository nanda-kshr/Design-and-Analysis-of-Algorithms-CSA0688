def find_ways_to_move_out(m, n, N, i, j):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    dp = [[[0] * (N + 1) for _ in range(n)] for _ in range(m)]
    dp[i][j][0] = 1
    result = 0
    for step in range(1, N + 1):
        for x in range(m):
            for y in range(n):
                for d in directions:
                    nx, ny = x + d[0], y + d[1]
                    if 0 <= nx < m and 0 <= ny < n:
                        dp[nx][ny][step] += dp[x][y][step - 1]
                    else:
                        result += dp[x][y][step - 1]
    return result

print(find_ways_to_move_out(2, 2, 2, 0, 0))
print(find_ways_to_move_out(1, 3, 3, 0, 1))