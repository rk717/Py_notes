def consecutive_ducks(n):
    results = []
    for i in range(1, n):
        the_sum, next_int = i, i + 1
        while (the_sum := the_sum + next_int) <= n:
            if the_sum == n:
                results.append(tuple(range(i, next_int + 1)))
                break
            next_int += 1
    return results

print(consecutive_ducks(69))

#[(9, 10, 11, 12, 13, 14), (22, 23, 24), (34, 35)]
