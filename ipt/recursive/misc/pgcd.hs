
mpgcd :: Int -> Int -> Int
mpgcd a 0 = abs a
mpgcd 0 b = abs b
mpgcd a b = let r = (rem a b) in mpgcd b r

main = print (mpgcd 275 11)
