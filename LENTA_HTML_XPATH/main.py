import parse_lenta
import database
import requests


print ("Welcome to news parsing app")

#
 # Импортируем библиотек Requests
 
 
# Основная функция
def main():
    # URL страницы
    url = 'https://lenta.ru//'
    # Получаем страницу
    r = requests.get(url)
    # Открываем файл
    with open('lenta_today.html', 'w', encoding='utf-8') as output_file:
        # Выводим страницу в HTML файл
        output_file.write(r.text)
 
 
# Запуск кода
if __name__ == '__main__':
    main()

    