
to_search = 'a'

characters_variables = [
    ';',
    ':',
    ',',
    '.',
    '*',
    '(',
    ')',
    '_',
    '!',
    '@',
    '#',
    '$',
    '%',
    '^',
    '&',
    '|',
    '=',
    '-',
    '+',
    '"',
    "'",
]

letters_variables = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'y',
    'x',
    'z',
]

to_search_list = [to_search]

for caracter in characters_variables:
    to_search_list.append(to_search + caracter)

for letter in letters_variables:
    to_search_list.append(to_search + letter)

for letter in letters_variables:
    to_search_list.append(letter + to_search)

to_search_list.append(f' {to_search} ')

words_finded = 0

with open('./to_scrap.txt', 'r') as f:
    lines = f.read()
    lines = lines.split()


    for line in lines:
        for search in to_search_list:
            if search == line:
                words_finded += 1

    f.close()

print(f'Words Founded: {words_finded}')
