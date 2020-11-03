import pandas

excel_data_df = pandas.read_excel('wine.xlsx', sheet_name='Лист1', usecols=['Название', 'Сорт', 'Цена', 'Картинка'])

print(excel_data_df.to_dict(orient='record'))
