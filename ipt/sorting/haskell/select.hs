
select :: [Int] -> [Int]
select []  = []
select [a] = [a]
select (a:l) = [x | x <- sort, x <= a] ++ [a] ++ [x | x <- sort, x > a]
    where sort = select(l)

main = print (select [4, 6, 1, 8, 3, 9, 4, 6, 3, 7])

