from typing import List, Dict
import re
import pathlib

def input_filename(day: int, use_example: bool = False):
    input_dir = pathlib.Path('.').parent / 'inputs'
    file_suffix = '_example' if use_example else ''
    input_file = input_dir / f'day{day:02}{file_suffix}.txt'
    return input_file

def get_text(filename: str) -> str:
    f = open(filename,'r')
    text = f.read()
    f.close()
    return text

def get_int_list(filename: str) -> List[int]:
    f = open(filename,'r')
    f_lines = f.readlines()
    f.close()
    return [int(n) for n in f_lines]

def get_dict_iter(filename: str, pattern: str) -> List[Dict[str, str]]:
    text = get_text(filename)
    return (m.groupdict() for m in re.finditer(pattern, text))