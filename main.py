import os


def red(string: str):
    return f'\033[91m{string}\033[0m'


def green(string: str):
    return f'\033[92m{string}\033[0m'


def download(game_path: str, link: str, file: str):
    file_path = f'{game_path}\\{file}'
    return_code = os.system(f'curl -o "{file_path}" "{link}?id=1IGENwFzLm8bBEboISadYSNEdxbnjz1fH&export=download&authuser=0&confirm=t" --no-progress-meter')
    if return_code:
        print(red('ERROR: Something went wrong while downloading the file.'))
        exit(return_code)


def edit_settings(file_path: str):
    return_code = os.system(f'REG IMPORT "{file_path}"')
    if return_code:
        print(red('ERROR: Something went wrong while editing the settings.'))
        exit(return_code)


def start_game(game_path: str):
    return_code = os.system(f'"{game_path}\\GGDLauncher.exe"')
    if return_code:
        print(red('ERROR: Something went wrong while starting the game.'))
        exit(return_code)


link = 'https://drive.usercontent.google.com/download?id=1IGENwFzLm8bBEboISadYSNEdxbnjz1fH&export=download&authuser=0'
file = 'settings.reg'
game_path = 'D:\\SteamLibrary\\steamapps\\common\\Goose Goose Duck'

input_game_path = input(f'Type path to game directory (if path is "{game_path}" just press enter): ')
if input_game_path:
    game_path = input_game_path

print('Downloading file...')
download(game_path, link, file)
print(green('File downloaded'))

print('Editing settings...')
edit_settings(f'{game_path}\\{file}')
print(green('Settings edited'))

print('Playing game...')
start_game(game_path)
print(green('Quit'))
