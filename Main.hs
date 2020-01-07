module Main where

test_hitten :: (Num(a), Ord(a)) => (a, a) -> (a, a) -> Bool
test_hitten i x = (fst i /= fst x) && (snd i /= snd x) && (fst i - fst x /= snd i - snd x) && (fst i - fst x /= snd x - snd i)

find1 :: (Ord(a), Num(a)) => [(a, a)] -> [(a, a)] -> [[(a, a)]]
find1 res_start [] = [res_start]
find1 res_start (d:[]) = [res_start ++ [d]]
find1 res_start (d:deck) = find1 (res_start ++ [d]) (filter (test_hitten d) deck) ++ find1 res_start deck

count = 11
deck = [(x, y) | x <- [1..count], y <- [1..count]]
res = filter (\x -> length x >= count) (find1 [] deck)

main :: IO ()
main = do
    print res
    print (length res)