# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

### Запуск с параметрами пути к файлу данных по умолчанию (файл `wine_list.xlsx`)

- Скачайте код
- Запустите сайт командой `python3 main.py`
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Запуск с пользовательскими параметрами пути к файлу данных

- Скачайте код
- Запустите сайт командой `python3 main.py путь_к_файлу_данных` (например, `python3 main.py /home/user/Documents/my_shop_wines.xlsx`)
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Образец файла данных

В файле `wine_list.xlsx` содержится образец файла с отформатированной таблицей напитков. Именно такой формат файла необходим программе нашего вебсайта для того чтобы считать список вин и других напитков, с ценами и остальными соответствующими данными. В общем и целом формат таблицы выглядит так:

| Категория      | Название     | Сорт            | Цена | Картинка         | Акция                |
| :------------- | :----------: | :-------------: |:----:| :--------------: | :------------------: |
| Белые вина     | Белая леди   | Дамский пальчик | 399  | belaya_ledi.png  | Выгодное предложение |
| Красные вина   | Черный лекарь| Качич           | 399  | chernyi_lekar.png|                      |

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
