import requests
from bs4 import BeautifulSoup

books = [
    'Kejadian',
    'Keluaran',
    'Imamat',
    'Bilangan',
    'Ulangan',
    'Yosua',
    'Hakim-hakim',
    'Rut',
    '1 Samuel',
    '2 Samuel',
    '1 Raja-raja',
    '2 Raja-raja',
    '1 Tawarikh',
    '2 Tawarikh',
    'Ezra',
    'Nehemia',
    'Ester',
    'Ayub',
    'Mazmur',
    'Amsal',
    'Pengkotbah',
    'Kidung Agung',
    'Yesaya',
    'Yeremia',
    'Ratapan',
    'Yehezkiel',
    'Daniel',
    'Hosea',
    'Yoel',
    'Amos',
    'Obaja',
    'Yunus',
    'Mikha',
    'Nahum',
    'Habakuk',
    'Zefanya',
    'Hagai',
    'Zakharia',
    'Maleakhi',
    'Matius',
    'Markus',
    'Lukas',
    'Yohanes',
    'Kisah Para Rasul',
    'Roma',
    '1 Korintus',
    '2 Korintus',
    'Galatia',
    'Efesus',
    'Filipi',
    'Kolose',
    '1 Tesalonika',
    '2 Tesalonika',
    '1 Timotius',
    '2 Timotius',
    'Titus',
    'Filemon',
    'Ibrani',
    'Yakobus',
    '1 Petrus',
    '2 Petrus',
    '1 Yohanes',
    '2 Yohanes',
    '3 Yohanes',
    'Yudas',
    'Wahyu'
]

def fetch_tb(bookIdx, chapter, has_title_in_beginning):
    tb_book = books[bookIdx]
    base_url = 'https://alkitab.me/in-tb'
    complete_url = f'{base_url}/{tb_book}/{chapter}'

    response = requests.get(complete_url)
    page = BeautifulSoup(response.text, 'html.parser')
    content = page.find(id='the-content')
    verses_html = content.find_all(class_='vw')

    end_result = []
    if has_title_in_beginning:
        end_result.append('')
    for verse_html in verses_html:
        verse_number = verse_html.find('span').string
        verse_texts_html = verse_html.find_all('p')
        verse_texts_list = []
        for verse_text_html in verse_texts_html:
            # if verse_text_html.string == '':
            verse_texts_list.append(verse_text_html.next_element.strip())
        combined_verse_texts = '\n'.join(verse_texts_list)
        end_result.append(f'[{verse_number}] {combined_verse_texts}')

    return end_result