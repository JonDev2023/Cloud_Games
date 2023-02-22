import os
import random
from urllib import request
from unidecode import unidecode
import app

SYMBOLS = 'áãâàéêèíîìóõôòúûù'

if input('Change Sprite (Y/N): ') == 'Y':
    app.cmd('mspaint', 'sprite.png')

# Input variables
server = input('Type the server: ')
game_name = input('Type the game Name(maiuscle and minuscle is different): ')
otimizate = input('Otimizate? (Y/N): ')

SYMBOLS_LIST = []

for i in SYMBOLS:
    SYMBOLS_LIST.append(i)

cripto_text1 = random.choice(SYMBOLS_LIST)
cripto_text2 = random.choice(SYMBOLS_LIST)
cripto_text3 = random.choice(SYMBOLS_LIST)

cripto_text = cripto_text1 + cripto_text2 + cripto_text3
print(f'type this without symbols: {cripto_text}')

response1 = input('type the 1: ')
response2 = input('type the 2: ')
response3 = input('type the 3: ')

index = 1
note = 0
max_note = 3
for i in cripto_text:
    if index == 1:
        if response1 == unidecode(cripto_text1):
            note += 1
    if index == 2:
        if response2 == unidecode(cripto_text2):
            note += 1
    if index == 3:
        if response3 == unidecode(cripto_text3):
            note += 1
    index += 1

if note > max_note:
    note = max_note

if note == max_note:
    print('Acess Garanted')
else:
    exit('Acess not Allowed')

# Downloading Main HTML File
file_url = server + '/index.html'
file = 'index.html'
request.urlretrieve(file_url, file)

# Downloading Data JSON File
try:
    file_url = server + '/data_' + game_name + '.json'
    file = 'data_' + game_name + '.json'
    if os.path.exists(file):
        print('Skipped')
    else:
        request.urlretrieve(file_url, file)
except OSError:
    print('Skipped')

# Downloading Game HTML File
try:
    file_url = server + '/game.html'
    file = 'game.html'
    request.urlretrieve(file_url, file)
except OSError:
    print('SKipped')

# Optimize App
if otimizate == 'Y':
    app.optimize()

# Running App
app.node('test')
