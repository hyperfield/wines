import pandas as pd
import collections
import pprint

excel_data_df = pd.read_excel('wine2.xlsx', sheet_name='Лист1', usecols=['Картинка', 'Категория', 'Название', 'Сорт', 'Цена'])

excel_data_df = excel_data_df.to_dict(orient='records')

wines = collections.defaultdict(list)

for entry in excel_data_df:
	wines[entry['Категория']].append(entry)

pprint.pprint(wines)
