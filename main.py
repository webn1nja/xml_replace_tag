'''
 На входе - файл xml по ссылке, на выходе такой же xml.
 Скрипт должен заменить тег <count> в ссылке на тег <outlet instock>.
 '''
import vars
import utils as ut


if __name__ == '__main__':
    # скачиваем файл
    xml_file = ut.get_file_xml()

    # заменяем теги
    content = ut.replace_tags(xml_file, vars.warehouse_names)

    # создаем выходной файл
    ut.generate_output_file(content)
