import math
n = int(input()) # biale
m = int(input()) # czarne
k = int(input()) # losowe
ctr1 = 0 #prawdopodobieństwo kul bialych
ctr2 = 0 #prawdopodobieństwo kul czarnych
if n/k >= 1:
    ctr1 = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
if m/k >= 1:
    ctr2 = math.factorial(m) / (math.factorial(k) * math.factorial(m-k))
wynik = (ctr1+ctr2)/(n+m)
print (wynik)


