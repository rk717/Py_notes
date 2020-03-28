[4, 1, 2, 3] --> [[1, 3], [2, 4]]

[1, 23, 3, 4, 7] --> [[1, 3]]

[4, 3, 1, 5, 6] --> [[1, 3], [3, 5], [4, 6]]

return all pairs of integers from a given collection of integers that have a difference of 2.

1 solution

numbers = [4,1,2,3]
pairs = []

for i in range(len(numbers)):
  for j in numbers:
    if numbers[i] - j == -2:
      pairs.append([numbers[i], j])
print(paisrs)



   
   


