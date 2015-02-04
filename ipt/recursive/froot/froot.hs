
f1 :: Float -> Float
f1 x = -2*(x - 1.5)

f2 :: Float -> Float
f2 x = (exp (-x)) - 0.5

f3 :: Float -> Float
f3 x = (1 - (exp (-x))) - 0.1

root :: (Float -> Float) -> Float -> Float -> Float -> Float
root f a b e = if (b-a) < e then m else if (f a)*(f m) <= 0 then root f a m e else root f m b e
               where m = (a+b)/2

epsilon = 0.0001
funcs = [f1, f2, f3]

main = let mroot = (rootf 0 4 epsilon) in print (fmap mroot funcs)
       where rootf a b e f = root f a b e

