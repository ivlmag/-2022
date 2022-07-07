def main():
	import json
	from datetime import datetime

	with open("input.txt",'r') as f:
		text = f.read().split('\n')

	products = json.loads(text[0]) #Загружаем json объект из первой строки

	#Функция для перевода строки в объект datetime
	def _convert_date(date):
		return datetime(*map(int, [date[-4:],date[3:5],date[:2]]))

	#Создаем словарь с фильтрами
	filters = {}
	for i in range(0,5):
		f, v = text[i+1].split(' ')
		if 'DATE' in f:
			v = _convert_date(v)
		filters[f] = v

	#Функция для фильтрации продукта по фильтрам из словаря filters
	def product_filter(product):
		date = _convert_date(product['date'])
		if (
			product['price']>=int(filters['PRICE_GREATER_THAN'])
			and product['price']<=int(filters['PRICE_LESS_THAN'])
			and filters['NAME_CONTAINS'].lower() in product['name'].lower() #регистр
			and date>=filters['DATE_AFTER']
			and date<=filters['DATE_BEFORE']
			):
			return True

	#Фильтрация, списковое включение продуктов, затем - сортировка по id
	prod_filtered = [prod for prod in products if product_filter(prod)]
	prod_filtered.sort(key=lambda prod: prod['id'])
	
	with open('output.txt', 'w') as f:
		f.write(json.dumps(prod_filtered)) #Перевод в json объект

if __name__ == '__main__':
	main()