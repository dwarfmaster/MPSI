
fibo :: Int -> Integer
fibo n = mfibo n 1 1
         where mfibo 0 a _ = a
               mfibo n a b = mfibo (n-1) b (a+b)

main = print (fibo 35)

