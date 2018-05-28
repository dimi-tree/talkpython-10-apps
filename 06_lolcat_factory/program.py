import os
import platform
import subprocess

import cat_service


def print_the_header():
    app_header = 'CAT FACTORY APP'
    print('-' * (20 + len(app_header)))
    print(' ' * 10 + app_header)
    print('-' * (20 + len(app_header)))
    print()


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)

    if not (os.path.exists(full_path) or os.path.isdir(full_path)):
        print(f'Creating new directory at {full_path}')
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print('Contacting server to download cats...')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = f'lolcat_{i}'
        print(f'Downloading cat {name}')
        cat_service.get_cat(folder, name)

    print('Done.')


def display_cats(folder):
    # Open folder

    if platform.system() == 'Darwin':  # Mac OS X
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print(f"We don't support your os: {platform.system()}")


def main():
    print_the_header()
    folder = get_or_create_output_folder()
    # download_cats(folder)
    display_cats(folder)



if __name__ == '__main__':
    main()
