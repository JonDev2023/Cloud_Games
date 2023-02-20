import os
import random
from urllib import request
import app
import smtplib

if input('Change Sprite (S/N): ') == 'S':
    app.cmd('mspaint', 'sprite.png')

# Input variables
server = input('Type the server: ')
game_name = input('Type the game Name(maiuscle and minuscle is different): ')
otimizate = input('Otimizate? (S/N): ')

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
if otimizate == 'S':
    app.optimize()

# Running App
app.node('test')
