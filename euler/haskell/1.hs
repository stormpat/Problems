module Main where

  solver :: Int -> Bool
  solver x = mod x 3 == 0 || mod x 5 == 0

  isValid :: Int
  isValid = sum $ filter solver [1..999]

  main :: IO ()
  main = print isValid
