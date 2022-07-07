def main():
	with open("input.txt",'r') as f:
		text = f.read().split('\n')

	vacancies_num = int(text[0]) #Количество вакансий в первой строке
	vacancies = {}
	candidates = {}

	#Формируем словарь с вакансиями
	for i in range(0,vacancies_num):
		vacancy = text[i+1]
		vacancy_name, capacity = vacancy.split(',')
		vacancies[vacancy_name] = int(capacity)
		candidates[vacancy_name] = []

	candidates_num = int(text[vacancies_num+1]) #Количество кандидатов
	
	#Формируем словарь с кандидатами по вакансиям
	for j in range(0,candidates_num):
		candidate = text[-2-j] #Берем строки с конца, учитывая пустую строку
		try:
			candidate_name, position, tests, fines = candidate.split(',')
			results = []
			results.append(candidate_name)
			results.append(int(tests))
			results.append(int(fines))
			candidates[position].append(results)
		except: pass

	next_step = []
	output = []

	#Для каждой позиции сортируем кандидатов 
	#и находим нужное количество, требуемое на вакансию 
	for position in vacancies:
		candidates_for_position = candidates[position] #Кандидаты на позицию

		#Сортируем тесты по убыванию, затем штрафы по возрастанию
		s = sorted(candidates_for_position, 
					key=lambda results: (0-results[1], results[2]))

		names = [name[0] for name in s]
		next_step.extend(names)
		next_step = next_step[0:vacancies[position]] #Топ кандидитов
		output.extend(next_step)
		next_step = []

	merged = '\n'.join(sorted(output)) #Сортируем по алфавиту имена кандидатов

	with open('output.txt', 'w') as f:
		f.write(merged)

if __name__ == '__main__':
	main()