
horner :: [Int] -> Int -> Int
horner [] _      = 1
horner (a:[]) _  = a
horner (a:b:l) p = horner ((a*p + b) : l) p

vals = ['0'..'9'] ++ ['a'..'z'] ++ ['A'..'Z']

topbase :: Int -> Int -> String
topbase p n = map (vals!!) $ mtopbase p n []
    where mtopbase _ 0 l = l
          mtopbase p n l = mtopbase p q (r:l)
              where (q,r) = divMod n p

approxp :: Int -> Double -> Double -> String
approxp p x e
 | x < 0     = '-' : approxp p (-1 * x) e
 | x >= 1    = let (n,d) = properFraction x in topbase p n ++ approxp p d e
 | otherwise = '.':mapproxp p x n []
    where n = abs $ ceiling $ logBase (fromIntegral p) e
          mapproxp :: Int -> Double -> Int -> String -> String
          mapproxp _ _ 0 l = l
          mapproxp p x n l = mapproxp p d (n - 1) (l ++ [vals !! i])
              where nx = x * fromIntegral p
                    (i,d) = properFraction nx

