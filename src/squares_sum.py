def squares_sum(n):
  result = 0
  for i in range(1, n + 1):
    result = result + i ** 2
  return result
