from typing import List, Dict
import re

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