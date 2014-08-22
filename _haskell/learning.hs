module Main where
  -- Learning Haskell. Random functions (using recursion).
  -- n to power of x with if/else
  pow :: Integer -> Integer -> Integer
  pow n x =
    if n == 0 || x == 0
    then 1
    else x * pow (n-1) x

  -- n to power of x with guards
  pow' :: Integer -> Integer -> Integer
  pow' n x
    | n == 0 = 1
    | x == 0 = 0
    | otherwise = x * pow' (n-1) x

  -- repeat string
  repStr :: String -> Integer -> String
  repStr str n =
    if n == 0
    then "" -- or []
    else str ++ repStr str (n-1)

  -- repeat with guards
  repStr' :: String -> Integer -> String
  repStr' str n
    | n == 0 = [] -- or ""
    | otherwise = str ++ repStr' str (n-1)








  main :: IO ()
  main = print (repStr' "moi" 2)