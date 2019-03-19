import os
import platform
import subprocess

import cat_service


def main():
    print_header()
    folder = get_or_create_output_folder()
    print(f'Found or created folder: {folder}')
    download_cats(folder)
    display_cats(folder)


def print_header():
    print('---------------------')
    print('   Cat Factory App')
    print('---------------------')


def get_or_create_output_folder():
    folder = 'cat_pictures'
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, folder)
    print(full_path)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print(f'Creating new directory at {full_path}...')
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    cat_count = 1
    print(f'Downloading {cat_count} cats into {folder}...')
    for i in range(1, cat_count + 1):
        name = f'lolcat_{i}'
        print(f'Download cat {name}...')
        cat_service.get_cat(folder, name)


def display_cats(folder):
    plat = platform.system()
    print(f'platform = {plat}')
    print(f'folder = {folder}')
    if plat == 'Linux':
        subprocess.call(['xdg-open', folder])
    elif plat == 'Darwin':
        subprocess.call(['open', folder])
    elif plat == 'Windows':
        subprocess.call(['start', folder], shell=True)
    else:
        print(f'Your platform ({plat}) is not supported.')


if __name__ == '__main__':
    main()
