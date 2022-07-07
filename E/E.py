#!/usr/bin/env pypy
def main():
	#Всего количество открывающих и закрывающих скобок
	num_oppar = 0
	num_clpar = 0

	#Индекс, минимальный индекс открывающей и закрывающей скобок
	idx = 0
	idx_oppar = 0
	idx_clpar = 0

	answer = 0

	with open("input.txt",'r') as f:
		while True:
			#Обрабатываем по одному символу для экономии памяти
			c = f.read(1)

			#В первую очередь обрабатываем ситуацию завершения строки 
			#или подстроки, заканчивающейся знаком равно
			if c=='=' or not c:
				#Если осталось более одной незакрытой скобки - ответ: -1
				if num_oppar+num_clpar>1:
					answer = -1
					break
				elif num_oppar==1:
					#Если потенциальных ответов несколько - ответ: -1
					if answer!=0: 
						answer=-1
						break
					#Если осталась одна открывающая скобка - ответ: ее индекс
					else: answer = idx_oppar
				elif num_clpar==1:
					#Если потенциальных ответов несколько - ответ -1
					if answer!=0: 
						answer=-1
						break
					#Если осталась одна закрывающая скобка - ответ: ее индекс
					else: answer = idx_clpar
				idx_oppar = 0
				idx_clpar = 0
				num_oppar = 0
				num_clpar = 0
				#Если перебрали всю строку и лишней скобки нет - ответ: -1
				if not c: 
					if answer==0: answer=-1
					break

			idx+=1

			#Находим индексы открывающих и закрывающих скобок
			if c == '(':
				num_oppar+=1
				#Если минимальная скобка еще не известна - текущий индекс
				if idx_oppar==0: idx_oppar=idx
			if c == ')':
				num_clpar+=1
				#Если есть открывающие скобки - минусуем количество ("закрываем" скобки)
				if num_oppar!=0:
					num_oppar-=1
					num_clpar-=1
					#Если все открытые скобки закрыты, то меняем минимальный индекс
					if num_oppar==0: idx_oppar=0
				#Если минимальная скобка еще не известна - текущий индекс 
				if idx_clpar==0: idx_clpar=idx

	print(answer)


if __name__ == '__main__':
	main()