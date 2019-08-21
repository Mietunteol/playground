# https://www.codewars.com/kata/baby-shark-lyrics-generator
import base64
import zlib


def baby_shark_lyrics():
    # EASY
    return zlib.decompress(base64.b64decode(
        'eJxzSkyqVCjOSCzK1lFIyc/HhrmcqK5Gkcs3PzeXoAaaKFLk'
        'cklMSSGogyaKFLncixLzUnITCemhoTKoGwqI00UbZYpcPqkl6'
        'sUK6fkKGaV5Jbh10VCZIldQaZ5CYnlipc6jhmUADlwJ3Q==')).decode()
