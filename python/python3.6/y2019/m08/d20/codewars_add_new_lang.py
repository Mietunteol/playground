#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib


def codewars_add_new_lang(lang_name, basepath='./'):
    assert len(lang_name) > 0, f'lang_name: {lang_name}'
    assert len(basepath) > 0, f'basepath: "{basepath}"'
    basepath = pathlib.Path(basepath).resolve()
    folder = basepath / lang_name
    for kyu in range(1, 8+1):
        current_folder = folder.joinpath(f'kyu_{kyu}')
        current_folder.mkdir(parents=True, exist_ok=True)
        file = current_folder / '.gitkeep'
        file.touch()


def main():
    for lang in ['python', 'php', 'javascript', 'kotlin']:
        codewars_add_new_lang(lang, '../../../../../codewars.com')


if __name__ == '__main__':
    main()
