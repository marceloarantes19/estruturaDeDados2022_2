def bubble(x):
  n = len(x)
  vezes = 0
  for i in range(0, n-1):
    for j in range(n - 1, i, -1):
      vezes = vezes + 1
      if x[j - 1] > x [j]:
        x[j - 1], x[j] = x[j], x[j - 1]
  return x, vezes

k = [0,1,2,3,4,5,6,7,8,9]
k, vz = bubble(k) 
print(k, "passou", vz)