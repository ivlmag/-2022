S, Q = open('input.txt').read().splitlines()
S = list(S)
Q = list(Q)

length = len(S)

#Создаем словарь с перечнем букв во входящей строке
S_dict = {char: 0 for char in S}

#Создаем словарь с результатами проверки
check_dict = {}

#Заполнение словарей и проверка совпадающих значений 
for i in range(0, length):
	check_dict[i+1] = 'absent' #Заполняем изначально словарь результатов absent
	S_dict[S[i]]+=1 #Подсчитываем количество букв во входящей строке
	
	if Q[i] == S[i]:
		check_dict[i+1] = 'correct'

		#Замещаем найденные совпадающие позиции, 
		#чтобы они не мешали в следующем цикле проверок,
		#и минусуем количество букв в словаре S_dict
		S_dict[Q[i]]-=1
		S[i] = ''
		Q[i] = ''

#Проверка букв с разными позициями, но в одном слове
for i in range(0, length):
	#Если буква встречалась во входящей строке и ее количество больше 0
	if ((Q[i] in S_dict) and (Q[i]!='') and (S_dict[Q[i]]>0)):
		check_dict[i+1] = 'present'
		S_dict[Q[i]]-=1 #Минусуем количество букв в словаре S_dict

#Преобразуем в нужный формат и сохраняем в файл
check = '\n'.join(list(check_dict.values()))

with open('output.txt', 'w') as f:
    f.write(check)