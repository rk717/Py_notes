results = ['1', '2', '3']

results = map(int, results)

>>>results = list(map(int, results))


>>> results = ["1", "2", "3"]
>>> results = [int(i) for i in results]
>>> results
[1, 2, 3]
results = [int(i) for i in results]
