import Control.Monad (guard)
import Data.List (tails)

parse :: String -> IO [Int]
parse fn = map read . lines <$> readFile fn

partOne :: [Int] -> Int
partOne xs = head [a * b | a:as <- tails xs, b <- as, a + b == 2020]

partTwo :: [Int] -> Int
partTwo xs = head $ do
    a:as <- tails xs
    b:bs <- tails as
    guard (a + b < 2020)
    c <- bs
    guard (a + b + c == 2020)
    return (a * b * c)

main :: IO ()
main = do
    expenses <- parse "day1.input"
    print (partOne expenses)
    print (partTwo expenses)
