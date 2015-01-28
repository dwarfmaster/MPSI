
fact :: Integer -> Integer
fact n = mfact n 1
         where mfact :: Integer -> Integer -> Integer
               mfact 0 a = a
               mfact n a = mfact (n-1) (n*a)

main = print (fact 50000)

