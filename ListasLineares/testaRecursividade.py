def teste(n):
  if n > 0:
    #print("linha 2 - valor", n)
    teste(n-1)
    print("linha 4 - valor", n)

teste(4)
