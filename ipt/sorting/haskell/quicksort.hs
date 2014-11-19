
quicksort :: [Int] -> [Int]
quicksort []    = []
quicksort [a]   = [a]
quicksort (a:l) = quicksort([x | x <- l, x <= a]) ++ [a] ++ quicksort([x | x <- l, x > a])

main = print (quicksort([4, 6, 1, 8, 3, 9, 4, 6, 3, 7]))

