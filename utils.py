import cfscrape
import requests
from requests.exceptions import HTTPError
from typing import TextIO


link = 'https://all-cool.ru/bitrix/catalog_export/export_ozon.xml'

fname_index = link.rfind('/')
fname = link[fname_index:]


def get_file_xml() -> str:
    url = link
    USER_AGENT = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, '
                  'like Gecko) Chrome/50.0.2661.102 Safari/537.36')
    HTTP_HEADERS = {'User-Agent': USER_AGENT}
    BASE_URL = 'http://' + url.rsplit('/')[2]
    HTTP_HEADERS['Referer'] = BASE_URL
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


def replace_tags(xml_file: str) -> str:

    tmp = xml_file.replace('<count>', '<outlet instock>')
    rez = tmp.replace('</count>', '</outlet instock>')
    return rez


def generate_output_file(content: str) -> TextIO:
    with open('result_' + fname[1:], 'w', encoding="utf-8") as f:
        f.write(content)
