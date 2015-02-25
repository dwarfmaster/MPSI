
-- Functions to analyze ------------------
pow :: Float -> Int -> Float
pow _ 0 = 1
pow 0 _ = 0
pow x n
     | n > 0 = x * pow x (n-1)
     | n < 0 = pow (1/x) (-n)

f :: Int -> Float -> Float -> Float
f n r x = (pow x n) - r
------------------------------------------

-- Secant method -------------------------
sec :: Float -> Float -> Float -> Float -> Float
sec x1 y1 x2 y2 = -y1 * (1/delta) + x1
    where delta = (y2 - y1)/(x2 - x1)

secant :: (Float -> Float) -> Float -> Float -> Float -> Float
secant f a b e = if abs (f m) < e then m
                 else secant f ma mb e
    where m = sec a (f a) b (f b)
          ma = if f m > 0  then a else m
          mb = if f m <= 0 then b else m
------------------------------------------

-- Dichotomy algorithm -------------------
root :: (Float -> Float) -> Float -> Float -> Float -> Float
root f a b e = if (b-a) < e then sec a (f a) b (f b) else 
                  if (f a)*(f m) <= 0 then root f a m e else root f m b e
    where m = (a+b)/2
------------------------------------------

-- Newton method -------------------------
delta :: (Float -> Float) -> Float -> Float
delta f x = ((f (x+h)) - (f (x-h))) / (2*h)
    where h = 1e-5

newton :: (Float -> Float) -> (Float -> Float) -> Float -> Float -> Float
newton f df xn e = if xn - xn1 < e then xn1 else newton f df xn1 e
    where xn1 = -(f xn)/(df xn) + xn
------------------------------------------

-- Main ----------------------------------
epsilons = map (\x -> pow 10 (-x)) [0..]
prec = 6
p = 2 :: Int
x = 2 :: Float

main = do putStrLn $ (++) "Precision : "   $ show $ epsilons !! prec
          putStrLn $ (++) "With secant : " $ show $ scs !! prec
          putStrLn $ (++) "With dicho : "  $ show $ rts !! prec
          putStrLn $ (++) "With newton : " $ show $ nts !! prec
    where fn = (f p x)
          df = delta fn
          scs = map (secant fn 0  x) epsilons
          rts = map (root   fn 0  x) epsilons
          nts = map (newton fn df x) epsilons
------------------------------------------

