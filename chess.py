#Задача расстановки 8 ферзей
# для доски из 8 элементов имеет 92 решения
count = 8

#Проверим решение на критерий: ферзей ровно "count" и ферзи не бьют друг-друга
def check_solution(solution):
	is_ok = len(solution) == count;	
	for i in solution:
		s1 = list(filter(lambda x : x[0] != i[0] and x[1] != i[1] and abs(x[0]-i[0]) != abs(x[1]-i[1]), solution))
		is_ok = is_ok and (len(s1) == count -1)		
	return is_ok

# самый обычный рекурсивный поиск: 
def find(deck, curr):
	if len(deck) == 0:
		if len(curr) == count:
			return [curr]
		else:
			return []
	
	res = []
	# Для каждой клетки в "остатке" доски попробуем поставить на неё ферзя, исключить клетки, которые он бьёт и найти решение
	# Потом эти решения объединим
	for i in deck:
		# x[0]>i[0]	# Упорядочиваем ферзей по координате х, чтобы избежать повторов вида: [(0, 0), (1, 7)...] vs [(1, 7), (0, 0)...]
		filtered_deck = list(filter(lambda x : x[0]>i[0] and x[1]!=i[1] and abs(x[0]-i[0])!=abs(x[1]-i[1]), deck))		
		res1 = find(filtered_deck, curr + [i])
		res = res + res1
	return res
	
deck = [(x, y) for x in range(count) for y in range(count)]
res = find(deck, [])
for i in res:
	print(i, " -- ", check_solution(i))
print("Count of results = ", len(res))







	


