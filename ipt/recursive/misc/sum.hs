
msum :: Integer -> Integer
msum 0 = 0
msum n = n + (msum (n-1))

main = print (msum 500)

