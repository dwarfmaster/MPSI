
addLst :: [Integer] -> Integer
addLst (x:[]) = x
addLst x      = addLst [ (x !! y) + (x !! (y+1)) | y <- [0..(length x - 2)] ]
main = print (addLst [1..100])

