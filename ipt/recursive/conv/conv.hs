
horner :: [Int] -> Int -> Int
horner [] _      = 1
horner (a:[]) _  = a
horner (a:b:l) p = horner ((a*p + b) : l) p

join :: [String] -> String
join [] = ""
join (s:ss) = s ++ join ss

topbase :: Int -> Int -> String
topbase p n = join $ map show $ mtopbase p n []
    where mtopbase _ 0 l = l
          mtopbase p n l = mtopbase p q (r:l)
              where (q,r) = divMod n p

t = [1, 0, 1, 0, 0] :: [Int]
main = putStrLn $ show $ horner t 2

