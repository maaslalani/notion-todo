# System imports
import sys

# Commands imports
from commands import add, list, remove, edit

try:
    command = sys.argv[1]
except IndexError:
    command = 'list'

if command == 'add': add(' '.join(sys.argv[2:]))
if command == 'remove': remove()
if command == 'list': list()
if command == 'edit': edit()
