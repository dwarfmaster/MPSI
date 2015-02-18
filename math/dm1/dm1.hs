
combine :: [a] -> (a -> a -> a) -> [a]
combine []      _ = []
combine (e:[])  _ = []
combine (e1:es) f = e1 `f` e2 : combine es f
    where e2 = head es

addLst :: [Integer] -> Integer
addLst (e:[]) = e
addLst  l     = addLst $ combine l (+)

addLst2 :: [Integer] -> Integer
addLst2 (x:[]) = x
addLst2 x      = addLst [x+y | (x,y) <- zip (tail x) (init x)]

main = do putStrLn $ show $ addLst  [1..100]
          putStrLn $ show $ addLst2 [1..100]

