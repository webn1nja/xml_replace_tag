'''
Путь к файлу, в котором будет храниться хэш для
проверки файла по ссылке на изменения.
'''

hash_file = 'hash.txt'

# сслыка, содержимое которой обрабатывается
link = 'https://all-cool.ru/bitrix/catalog_export/export_ozon.xml'

'''
Названия складов.
Добавлять можно сколько угодно.
'''
warehouse_names = [
    'realFBS Москва',
    'FBS Москва',
    # добавляем новые по аналогии: в кавычках, через запятую
]
