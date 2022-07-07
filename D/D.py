def main():

	with open("input.txt",'r') as f:
		labirinth = f.read().split('\n')

	N, M = labirinth.pop(0).split(' ')

	#Переводим в тип данных "список", чтобы было доступно изменение символов
	for i in range(0, int(N)):
		labirinth[i] = list(labirinth[i])

		#Ищем индекс стартовой позиции
		for j in range(0, int(M)):
			if 'S' == labirinth[i][j]:
				S_index = [i, j]

	#Создаем список индексов для проверки в цикле, 
	#вначале вносим только индекс стартовой точки
	index_list = []
	index_list.append(S_index)

	#Если на позиции символ '.' - заменяем на соответствующую букву направления
	#и добавляем этот индекс в список для дальнейшей проверки
	def _check_point(index, direction):
		if labirinth[index[0]][index[1]] == '.':
			labirinth[index[0]][index[1]] = direction
			index_list.append(index)

	#Цикл работает, пока список с индексами не пустой.
	#Новые индексы добавляются в функции check_point 
	while index_list:
		length = len(index_list)
		for _ in range(0,length):
			ind = index_list.pop(0)

			#Запускаем проверку для всех направлений
			_check_point([ind[0]-1,ind[1]],'U')
			_check_point([ind[0]+1,ind[1]],'D')
			_check_point([ind[0],ind[1]-1],'L')
			_check_point([ind[0],ind[1]+1],'R')

	#Склеиваем лабиринт обратно, переводя списки в строки 
	#и разделяя строки переносами
	labirinth = [''.join(labirinth[k]) for k in range(0, int(N))]
	with open('output.txt', 'w') as f:
		f.write('\n'.join(labirinth))


if __name__ == '__main__':
	main()