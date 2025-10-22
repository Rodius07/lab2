import csv
import xml.dom.minidom as minidom
import random


def print_1(books):
    """Подсчитывает количество книг с названием длиннее 30 символов."""
    books.seek(0)
    reader = csv.DictReader(books, delimiter=";")
    count = 0
    for row in reader:
        if len(row['Название']) > 30:
            count += 1
    print(count)


def search(books, author):
    """Ищет и выводит названия книг указанного автора."""
    books.seek(0)
    reader = csv.DictReader(books, delimiter=";")
    for row in reader:
        if row['Автор'] == author:
            print(row['Название'])


def save_to_file(books, filename='name.txt'):
    """Сохраняет 20 случайных книг в файл в указанном формате."""
    books.seek(0)
    reader = csv.DictReader(books, delimiter=";")
    
    # Читаем все строки в список
    all_rows = list(reader)
    
    # Выбираем 20 случайных строк
    num_rows_to_select = 20
    random_rows = random.sample(all_rows, num_rows_to_select)
    
    with open(filename, 'w', encoding='utf-8') as f:
        count = 1
        for row in random_rows:
            date_year = row['Дата поступления'].split()[0][-4:]
            line = f"{count}. {row['Автор']}.{row['Название']} - {date_year}\n"
            f.write(line)
            count += 1


def parse_xml(xml_file):
    """Парсит XML файл и извлекает коды."""
    xml_data = xml_file.read()
    dom = minidom.parseString(xml_data)
    dom.normalize()
    names = ['CharCode','Value']
    # Получаем коды валют
    list_names = []
    for name in names:

        charcodes = dom.getElementsByTagName(name)
        char_code = []
        for charcode in charcodes:
            value = charcode.firstChild.data
            char_code.append(value)
        list_names.append(char_code)
    
    return list_names


if __name__ == "__main__":
    with open('books.csv', encoding='utf-8') as books:
        print_1(books)
        search(books, 'Наталья Жильцова')
        save_to_file(books)
    
    with open('currency.xml', encoding='utf-8') as xml_file:
        char_code, value_code = parse_xml(xml_file)
        print(char_code)
        print(value_code)