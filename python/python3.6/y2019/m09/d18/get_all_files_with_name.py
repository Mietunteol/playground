#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pathlib
import sys


# noinspection PyShadowingNames
def get_all_files(folder):
    assert pathlib.Path(folder).resolve().exists(), folder
    for item in pathlib.Path(folder).resolve().glob('**/*'):
        try:
            if item.is_file():
                yield item
        except (PermissionError,):
            pass


# noinspection PyShadowingNames
def get_all_files_with_name(folder, name):
    for item in get_all_files(folder):
        if item.name == name:
            yield item


if __name__ == '__main__':
    """
    sudo python3 y2019/m09/d18/get_all_files_with_name.py "/" "foo.bar"
    """
    out_folder = pathlib.Path(sys.argv[1:][0]).resolve()
    out_folder.mkdir(parents=True, exist_ok=True)
    name = sys.argv[1:][1]
    out_file = out_folder / 'result.txt'
    out_file.touch()
    with open(out_file, 'wb') as f_out:
        f_out.truncate()
    os.chmod(f'{out_file}', 0o777)
    for file in get_all_files_with_name('/', name):
        with open(out_file, 'a', encoding='utf-8') as f_out:
            f_out.write(f'{file}\n')
