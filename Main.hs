module Main where

is_not_hitten :: (Num(a), Ord(a)) => (a, a) -> (a, a) -> Bool
is_not_hitten i x = (fst i /= fst x) && (snd i /= snd x) && (fst i - fst x /= snd i - snd x) && (fst i - fst x /= snd x - snd i)

-- Алгоритмически неоптимизированная функция.
-- "решения" = "решения если ставить ферзя" + "решения если не ставить ферзя". Хвост второй рекурсии растёт экспоненциально, а первой части медленнее
-- prefilter adds 130% (30% .. 180%) performance
find :: (Ord(a), Num(a)) => [(a, a)] -> [(a, a)] -> [[(a, a)]]
find res_start [] = filter (\x -> length x >= count) [res_start]
--find res_start (d:[]) = filter (\x -> length x >= count) [res_start ++ [d]] -- this match adds 15% performance
find res_start (d:deck) = find (res_start ++ [d]) (filter (is_not_hitten d) deck) ++ find res_start deck -- list order adds 50% (-5% .. + 100%) performance

-- Алгоритмически оптимизированная функция: пробуем ставить ферзей на все клетки, на которые имеет смысл (т.е. одной линии).
-- сложность растёт вдвое медленнее чем у предыдущей реализации (хотя тоже экспоненциально)
find1 :: (Ord(a), Num(a)) => [(a, a)] -> [(a, a)] -> [[(a, a)]]
find1 res_start [] = filter (\x -> length x >= count) [res_start]
find1 res_start deck = concat $ map ( \(x, y) -> find1 (res_start ++ [x]) y ) fsubdeck
    where subdeck = zip deck $ deckToSubdecks deck
          fsubdeck = filter (\(x, y) -> fst x == fst (head deck)) subdeck

deckToSubdecks :: (Ord(a), Num(a)) => [(a, a)] -> [[(a, a)]]
deckToSubdecks deck = map (\x -> filter (is_not_hitten x) deck) deck

count = 13
deck = [(x, y) | x <- [1..count], y <- [1..count]]

res = find [] deck

main :: IO ()
main = do
    print(deck)
    print res
    print (length res)