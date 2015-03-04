
horner :: [Int] -> Int -> Int
horner [] _      = 1
horner (a:[]) _  = a
horner (a:b:l) p = horner ((a*p + b) : l) p

t = [1, 0, 1, 0, 0] :: [Int]
main = putStrLn $ show $ horner t 2

