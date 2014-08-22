
{-# LANGUAGE BangPatterns #-}

module Main where

  fib :: Integer -> Integer
  fib n = inner n (0,1)
    where
      inner !n (!a, !b)
        | n == 0 = a
        | otherwise = inner (n - 1) (b, a + b)

  evenFibs :: Integer -> [Integer]
  evenFibs n = filter even (takeWhile(<= n) (map fib [1..]))

  main :: IO ()
  main = print $ sum (evenFibs 4000000)
