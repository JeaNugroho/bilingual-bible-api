import requests
import re

books = [
    'Genesis',
    'Exodus',
    'Leviticus',
    'Numbers',
    'Deuteronomy',
    'Joshua',
    'Judges',
    'Ruth',
    '1 Samuel',
    '2 Samuel',
    '1 Kings',
    '2 Kings',
    '1 Chronicles',
    '2 Chronicles',
    'Ezra',
    'Nehemiah',
    'Esther',
    'Job',
    'Psalms',
    'Proverbs',
    'Ecclesiastes',
    'Song of Solomon',
    'Isaiah',
    'Jeremiah',
    'Lamentations',
    'Ezekiel',
    'Daniel',
    'Hosea',
    'Joel',
    'Amos',
    'Obadiah',
    'Jonah',
    'Micah',
    'Nahum',
    'Habakkuk',
    'Zephaniah',
    'Haggai',
    'Zechariah',
    'Malachi',
    'Matthew',
    'Mark',
    'Luke',
    'John',
    'Acts',
    'Romans',
    '1 Corinthians',
    '2 Corinthians',
    'Galatians',
    'Ephesians',
    'Philippians',
    'Colossians',
    '1 Thessalonians',
    '2 Thessalonians',
    '1 Timothy',
    '2 Timothy',
    'Titus',
    'Philemon',
    'Hebrews',
    'James',
    '1 Peter',
    '2 Peter',
    '1 John',
    '2 John',
    '3 John',
    'Jude',
    'Revelation'
]

maxChapters = [
    50,
    40,
    27,
    36,
    34,
    24,
    21,
    4,
    31,
    24,
    22,
    25,
    29,
    36,
    10,
    13,
    10,
    42,
    150,
    31,
    12,
    8,
    66,
    52,
    5,
    48,
    12,
    14,
    3,
    9,
    1,
    4,
    7,
    3,
    3,
    3,
    2,
    14,
    4,
    28,
    16,
    24,
    21,
    28,
    16,
    16,
    13,
    6,
    6,
    4,
    4,
    5,
    3,
    6,
    4,
    3,
    1,
    13,
    5,
    5,
    3,
    5,
    1,
    1,
    1,
    22
]

def get_esv_books():
    return books

def get_max_chapters():
    return maxChapters

def fetch_esv(param, token):
    base_url = 'https://api.esv.org/v3/passage/text/'

    headers = {
        'Authorization': f'Token {token}'
    }

    params = {
        'q': param
    }

    try:
        response = requests.get(base_url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(response)
    
    except requests.exceptions.RequestException as e:
        print(e.response)

def chop_string(input_string, params):
    input_string = input_string[len(params):]
    input_string = input_string.split('Footnotes')[0]

    # Use regex to find all occurrences of '[<a_number>]'
    pattern = r'\[\d+\]'
    split_positions = [match.start() for match in re.finditer(pattern, input_string)]

    # Add the start and end positions of the string to the split positions
    split_positions = [0] + split_positions + [len(input_string)]

    # Chop the string into pieces
    chopped_strings = [input_string[start:end] for start, end in zip(split_positions, split_positions[1:])]

    return chopped_strings