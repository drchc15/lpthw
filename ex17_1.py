# LPTHW ex17.py
# ex 17 super-compact edition
from sys import argv
from os.path import exists
script, from_file, to_file = argv
out_file = open(to_file, 'w').write(open(from_file).read())