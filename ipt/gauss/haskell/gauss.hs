-- Types
class (Ord a, Fractional a) => Corps a
instance Corps Float

-- Data
type Line a = [a]
type Matrix a = [Line a]
matrix :: Matrix Float
matrix = [[4, 3, 5], [5, 2, 6]]

-- Utilities
is_zero :: (Corps a) => a -> Bool
is_zero x = if x >= 0 then (x < 1e-10) else is_zero (-x)

first_nonzero :: (Corps a) => Line a -> a
first_nonzero [] = 1
first_nonzero (a:[]) = if not (is_zero a) then a else 1
first_nonzero (a:l)  = if not (is_zero a) then a else first_nonzero l

-- Data to str convention
matrix_show :: (Show a) => Matrix a -> String
matrix_show []     = ""
matrix_show (l:[]) = "| " ++ (array_flat l) ++ " |"
matrix_show (l:a)  = "| " ++ (array_flat l) ++ " |\n" ++ matrix_show a

array_flat :: (Show a) => Line a -> String
array_flat []     = ""
array_flat (a:[]) = (show a)
array_flat (a:l)  = (show a) ++ " " ++ (array_flat l)

matrix_print :: (Show a) => Matrix a -> IO()
matrix_print m = putStrLn (matrix_show m)

-- Operations
matrix_mult :: (Num a) => a -> Line a -> Line a
matrix_mult n l = [n*e | e <- l]

matrix_add :: (Num a) => Line a -> a -> Line a -> Line a
matrix_add _      _ []     = []
matrix_add (l:ls) n (e:es) = [e + n*l] ++ matrix_add ls n es

-- Triangularization
line_normalize :: (Corps a) => Line a -> Line a
line_normalize l = matrix_mult (1/(first_nonzero l)) l

apply :: (Corps a) => Line a -> Line a -> Line a
apply l1 l2 = matrix_add l1 (-1 * first_nonzero l2) l2

trian :: (Corps a) => Matrix a -> Matrix a
trian [] = []
trian (l:ls) = [nl] ++ trian (fmap (apply nl) ls)
    where nl = line_normalize l

-- Main IO
main :: IO()
main = do matrix_print (trian matrix)

