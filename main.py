from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
import collections

if __name__ == "__main__":
	env = Environment(
	loader=FileSystemLoader('.'),
    	autoescape=select_autoescape(['html', 'xml'])
	)
	template = env.get_template('template.html')
	excel_data_df = pandas.read_excel('wine3.xlsx', sheet_name='Лист1',
									usecols=['Картинка', 'Категория', 'Название',
									'Сорт', 'Цена', 'Акция']).to_dict(orient='records')
	wines = collections.defaultdict(list)

	for drink in excel_data_df:
		wines[drink['Категория']].append(drink)

	wines = collections.OrderedDict(sorted(wines.items(),\
		 							key=lambda t: t[0])) # Отсортировать словарь в алфавитном порядке по ключу 'Категория'
	rendered_page = template.render(wines=wines)

	with open('index.html', 'w', encoding="utf8") as file:
		file.write(rendered_page)

	server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
	server.serve_forever()
