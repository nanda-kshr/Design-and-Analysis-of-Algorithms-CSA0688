def climb_stairs(n):
    if n <= 1: return 1
    prev, curr = 1, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
print(climb_stairs(4))
print(climb_stairs(3))