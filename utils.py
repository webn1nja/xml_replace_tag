import cfscrape
import requests
import vars
from requests.exceptions import HTTPError
from typing import TextIO


fname_index = vars.link.rfind('/')
fname = vars.link[fname_index:]


def get_file_xml() -> str:
    url = vars.link
    USER_AGENT = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, '
                  'like Gecko) Chrome/50.0.2661.102 Safari/537.36')
    HTTP_HEADERS = {'User-Agent': USER_AGENT}
    BASE_URL = 'http://' + url.rsplit('/')[2]
    HTTP_HEADERS['Referer'] = BASE_URL
    HTTP_HEADERS['Content-Type'] = 'text/html; charset=utf-8'
    s = requests.session()
    s.headers = HTTP_HEADERS
    try:
        scraper_one = cfscrape.create_scraper(sess=s)
        r = scraper_one.get(url)

        content = r.text
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print(f'Содержимое ссылки загружено: {url}')

    with open('xml_files' + fname, 'w', encoding="utf-8") as f:
        f.write(content)
    return content


def replace_tags(xml_file: str, warehouse_names: list) -> str:

    str_to_paste = '<outlets>'
    for wh in warehouse_names:
        str_to_paste += f'<outlet instock="10" warehouse_name="{wh}"></outlet>'
    tmp = xml_file.replace('<count>10', str_to_paste)
    rez = tmp.replace('</count>', '</outlets>')
    return rez


def generate_output_file(content: str) -> TextIO:
    with open('result_' + fname[1:], 'w', encoding="utf-8") as f:
        f.write(content)


# def check_counter(number):

#     with open(vars.counter_file, 'r', encoding="utf-8") as f:
#         rez = f.read()

#     if (int(rez) == 0):
#         print('Происходит первый запуск скрипта')
#         return True
#     elif (int(rez) == number):
#         print('Изменений в фиде не обнаружено')
#         return False
#     else:
#         print('Обнаружены изменения в фиде')
#         return True