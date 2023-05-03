import logging
import requests
from bs4 import BeautifulSoup

# Настройка логирования
logging.basicConfig(filename='example.log', level=logging.DEBUG)

# Получение содержимого страницы Google
url = 'https://www.google.com'
response = requests.get(url)

# Парсинг HTML-кода страницы
soup = BeautifulSoup(response.content, 'html.parser')

# Поиск всех тегов <a> на странице и вывод их атрибутов href
for link in soup.find_all('a'):
    href = link.get('href')
    if href is not None:
        # Запись найденной ссылки в лог-файл
        print(href)
