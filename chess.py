#Задача расстановки 8 ферзей
# для доски из 8 элементов имеет 92 решения
count = 8

#Проверим решение на критерий: ферзей ровно "count" и ферзи не бьют друг-друга
def check_solution(solution):
	is_ok = len(solution) == count;	for i in solution:
		s1 = list(filter(lambda x : x[0] != i[0] and x[1] != i[1] and abs(x[0]-i[0]) != abs(x[1]-i[1]), solution))
		is_ok = is_ok and (len(s1) == count -1)
	return is_ok

# самый обычный рекурсивный поиск:
# передаём "остаток доски" -- свободные и не бьющиеся клетки и "начало решения" -- клетки куда уже поставили ферзей.
#
# Пробуем найти все решения для данной позиции (т.е. решения, если ставить ферзя в клетку-0, клетку-1, клетку-2..., и естественно фильтровать клеки что он бьёт)
# Нам нужен немного грязный хак: если мы ставим ферзя на клетку-K, то нам надо выкинуть не только те клетки, которые он бьёт, но и все клетки,
# которые "меньше" текущей, чтобы избежать повторений вида: [(0, 0), (1, 7)...] vs [(1, 7), (0, 0)...]
def find(deck, curr):
	counts[len(curr)] = counts[len(curr)] + 1

	if len(deck) == 0:
		if len(curr) == count:
			return [curr]
		else:
			return []

	res = []
	for i in deck:
		filtered_deck = filter(lambda x : (x[0] > i[0]) and (x[0]!=i[0] and x[1]!=i[1] and abs(x[0]-i[0])!=abs(x[1]-i[1])), deck)
		res1 = find(list(filtered_deck), curr + [i])
		res = res + res1
	return res

def gen_test(i):
	return lambda x : (x[0] != i[0] and x[1] != i[1] and abs(x[0]-i[0]) != abs(x[1]-i[1]))

# Улучшенная версия программы.# Ишем все решения вида: "все решения, если на первую клетку ставить ферзя" + "все решения, если на 1ю клетку не ставить ферзя"
def find1(deck, curr):
	counts[len(curr)] = counts[len(curr)] + 1

	if len(deck) == 0:
		c = filter(lambda x : len(x) == count, [curr])
		return list(c)
	else:
		filtered_deck = filter(gen_test(deck[0]), deck)
		res1 = find1(list(filtered_deck), curr + [deck[0]])
		res2 = find1(deck[1:], curr)
		return res1 + res2

def find2(deck, curr):
	counts[len(curr)] = counts[len(curr)] + 1

	if len(deck) == 0:
		return list(filter(lambda x : len(x) >= count, [curr]))
	else:
		filtered_deck = list(filter(gen_test(deck[0]), deck))
		return find2(filtered_deck, curr + [deck[0]]) + find2(deck[1:], curr);


# Подготовка
deck = [(x, y) for x in range(count) for y in range(count)]
counts = [0 for i in range(count + 1)]
res = find2(deck, [])

# Проверка (ну так на всякий случай) корректности решений
for i in res:
	print(i, " -- ", check_solution(i))
print("Count of solutions = ", len(res))
print("%d calls, calls details: " % sum(counts), counts)
print()

# А теперь для всех функций
for f in [find, find1, find2]:
	counts = [0 for i in range(count + 1)]
	res0 = f(deck, [])	

	is_ok = (len(res) == len(res0))
	for i in res0:
		is_ok = is_ok and check_solution(i)
	print("%s = %r: %d solutions, %d calls, call details: " % (f.__name__, is_ok, len(res0), sum(counts)), counts)
