## A simple Python script that replaces tags in an xml document with Cloudflare's anti-bot page bypass

###### ver. 1.4


 На входе - файл xml по ссылке, на выходе такой же xml.
 Скрипт должен заменить тег <count> в ссылке на тег <outlet> с различными атрибутами.

 Для получения содержимого предложенного url выполняется обход Cloudflare's anti-bot page

***
### Как запускать?

#### Установите виртуальное окружение

-   `python3 -m venv venv` в Linux/macOS;
-   `python -m venv venv` или `py -3 -m venv venv` в Windows;

#### Активируйте виртуальное окружение

Из директории xml_replace_tag выполните команду:
- `source venv/bin/activate` в Linux/macOS;
- ` venv\Scripts\activate.bat` в Windows;

#### Обновите пакетный менеджер
  При создании виртуального окружения будет использоваться та версия менеджера, которая была установлена вместе с Python. И это будет, скорее всего, не самая последняя версия, о чём вам и будет сообщаться каждый раз при обращении к нему.
  Обновить версию можно командой:

-   Windows: `python -m pip install --upgrade pip`;
-   Linux/macOS: `python3 -m pip install --upgrade pip`.


#### Установите зависимости

`pip install -r requirements.txt`

#### Запустите скрипт

-   `python3 -m main.py` в Linux/macOS;
-   `python -m main.py` или `py -3 -m main.py` в Windows