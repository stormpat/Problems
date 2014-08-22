-- Learning Haskell

module Main where

  import Data.Char

  sanitize :: String -> String
  sanitize str =
      let a = [toUpper (head str)]
          b = tail str
      in a ++ b

  main :: IO ()
  main = print $ sanitize "please UpCaSe the first LettER, and fIX The LEET StRinG"
