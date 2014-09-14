
addLst :: [Integer] -> Integer
addLst (x:[]) = x
addLst x      = addLst [x+y | (x,y) <- zip (tail x) (init x)]
main = print (addLst [1..100])

