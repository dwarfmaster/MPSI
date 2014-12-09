-- Data
matrix :: [[Float]]
matrix = [[4, 3, 5], [5, 2, 6]]

-- Utilities
is_zero :: Float -> Bool
is_zero x = if x > 0 then (x < 1e-10) else is_zero (-x)

first_nonzero :: [Float] -> Int
first_nonzero [] = 0
first_nonzero (a:[]) = if (is_zero a) then 0 else 1
first_nonzero (a:l)  = if (is_zero a) then 0 else ((first_nonzero l) + 1)

-- Data to str convention
matrix_show :: [[Float]] -> String
matrix_show []     = ""
matrix_show (l:[]) = "| " ++ (array_flat l) ++ " |"
matrix_show (l:a)  = "| " ++ (array_flat l) ++ " |\n" ++ matrix_show a

array_flat :: [Float] -> String
array_flat []     = ""
array_flat (a:[]) = (show a)
array_flat (a:l)  = (show a) ++ " " ++ (array_flat l)

-- Main IO
main :: IO()
main = putStrLn $ (matrix_show matrix) ++ (show (first_nonzero [0, 0, 3, 4, 0]))

