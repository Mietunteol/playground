#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import pathlib
import sys


def new_day_new_folder(basepath='./'):
    assert len(basepath) > 0, f'basepath: "{basepath}"'
    path = [basepath]
    for piece in 'y%Y/m%m/d%d'.split('/'):
        utcnow = datetime.datetime.utcnow()
        path.append(datetime.datetime.strftime(utcnow, piece))
        current_folder = pathlib.Path().joinpath(*path)
        current_folder.mkdir(parents=True, exist_ok=True)
        current_filename = current_folder / '__init__.py'
        current_filename.touch()


def main():
    args = ''.join(sys.argv[1:])
    if args and pathlib.Path(args).exists():
        new_day_new_folder(args)
    else:
        new_day_new_folder()


if __name__ == '__main__':
    main()
