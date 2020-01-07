module Main where

test_hitten :: (Num(a), Ord(a)) => (a, a) -> ((a, a) -> Bool)
test_hitten i = \ x -> (fst i /= fst x) && (snd i /= snd x) && (fst i - fst x /= snd i - snd x) && (fst i - fst x /= snd x - snd i)

find1 :: (Ord(a), Num(a)) => [(a, a)] -> [(a, a)] -> [[(a, a)]]
find1 res_start [] = [res_start]
find1 res_start (d:[]) = [res_start ++ [d]]
find1 res_start (d:deck) = find1 res_start deck ++ find1 (res_start ++ [d]) (filter (test_hitten d) deck)

count = 11

main :: IO ()
main = do
    let deck = [(x, y) | x <- [1..count], y <- [1..count]]
    let deck1 = filter (test_hitten (head deck)) deck
    let res = filter (\x -> length x >= count) (find1 [] deck)
    print res
    print (length res)
    
    
