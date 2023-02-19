import os

def cmd(command, tag1: str = None, tag2: str = None):
    allow_multi_tags = True
    only_command = False
    if tag2 == None and allow_multi_tags:
        allow_multi_tags = False
    if tag1 == None and not only_command:
        only_command = True
    if allow_multi_tags and not only_command:
        os.system(f'{command} {tag1} {tag2}')
    if not allow_multi_tags and not only_command:
        os.system(f'{command} {tag1}')
    if not allow_multi_tags and only_command:
        os.system(f'{command}')


def node(command):
    print('Opening task manager...')
    try:
        cmd('taskmgr')
    except OSError:
        print('Sorry, error when opening taskmgr')
    print('Opening Application...')
    try:
        cmd('node', command)
    except OSError:
        exit('Sorry, error when executing game')

def optimize():
    try:
        cmd('start', 'otimizator.vbe')
    except OSError:
        print('Cannot Optimize your game')
