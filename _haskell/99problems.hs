
-- Haskell's 99 problems.
-- http://www.haskell.org/haskellwiki/H-99:_Ninety-Nine_Haskell_Problems

module Main where

-- last element in list
myLast :: [a] -> a
myLast [x] = x
myLast (_:xs) = myLast xs
myLast [] = error "\nEmpty list"

-- last but one element in a list
butLast :: [a] -> a
butLast [x] = x
butLast (x:_:[]) = x
butLast (_:xs) = xs !! (length xs -2)
butLast [] = error "\nEmpty list"

-- nth element in list
elementAt :: [a] -> Int -> a
elementAt xs n = xs !! (n - 1)

-- no elements in list
myLength :: [a] -> Int
myLength [] =  0
myLength (_:xs) = 1 + myLength xs

-- reverse list
myRev :: [a] -> [a]
myRev [] = []
myRev (x:xs) = myRev xs ++ [x]

main :: IO ()
main = print $ myRev "123"