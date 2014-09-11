
addLst x = if length x == 1
            then x !! 0
            else addLst [ (x !! y) + (x !! (y+1)) | y <- [0..(length x - 2)] ]
main = print (addLst [1..100])

