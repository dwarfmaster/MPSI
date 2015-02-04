
-- Functions to analyze ------------------
f1 :: Float -> Float
f1 x = -2*(x - 1.5)

f2 :: Float -> Float
f2 x = (exp (-x)) - 0.5

f3 :: Float -> Float
f3 x = x*x - 2
------------------------------------------

-- Dichotomy algorithm -------------------
sec :: Float -> Float -> Float -> Float -> Float
sec x1 y1 x2 y2 = -y1 * (1/delta) + x1
                  where delta = (y2 - y1)/(x2 - x1)

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
epsilon1 = 0.0001
epsilon2 = 0.000001
funcs = [f1, f2, f3]

main = print ((show (fmap mroot funcs)) ++ " " ++ (show (mnewton f3)))
       where rootf a b e f = root f a b e
             mroot = (rootf 0 4 epsilon1)
             newtonf xn e f = newton f (delta f) xn e
             mnewton = (newtonf 4 epsilon2)
------------------------------------------

