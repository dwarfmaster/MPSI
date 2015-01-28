
mpow :: Int -> Float -> Float
mpow 0 _ = 1
mpow n f = f * (mpow (n-1) f)

main = print (mpow 50 0.5)

