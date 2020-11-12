#!/usr/bin/python
# -*- coding: UTF-8 -*-

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
import collections
import sys
import argparse

BEGIN_YEAR = 1920


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs='?', default='wine_list.xlsx')

    return parser


if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    env = Environment(loader=FileSystemLoader('.'), autoescape=select_autoescape(['html', 'xml']))
    template = env.get_template('template.html')
    excel_dataframe = pandas.read_excel(namespace.path, sheet_name='Лист1',
                                        usecols=['Картинка', 'Категория',
                                                 'Название', 'Сорт', 'Цена',
                                                 'Акция'],
                                        keep_default_na=False)\
                            .to_dict(orient='records')
    wines = collections.defaultdict(list)

    for drink in excel_dataframe:
        wines[drink['Категория']].append(drink)

    # Отсортировать словарь в алфавитном порядке по ключу 'Категория'
    wines = collections.OrderedDict(sorted(wines.items(),
                                           key=lambda t: t[0]))
    rendered_page = template.render(wines=wines, age=datetime.datetime.now()
                                                             .year-BEGIN_YEAR)

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
