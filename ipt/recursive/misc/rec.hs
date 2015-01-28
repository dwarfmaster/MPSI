
rec :: Float -> Float
rec 0 = 1
rec n = 1 + 1 / (rec (n-1))

main = print (rec 10000)

