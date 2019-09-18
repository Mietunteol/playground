import os
import pathlib


def directory_size(directory):
    # noinspection PyTypeChecker
    return sum(os.path.getsize(item.resolve()) if item.is_file() else 0
               for item in pathlib.Path(directory).resolve().glob('**/*'))


if __name__ == '__main__':
    print(directory_size(pathlib.Path().home()))
