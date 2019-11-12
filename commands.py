# System imports
import sys, tempfile, os
from subprocess import call

# CLI imports
from termcolor import cprint
import inquirer as prompt

# Notion imports
from notion.client import NotionClient
from notion.block import TodoBlock

EDITOR = os.environ.get('EDITOR', 'vim')
CLIENT = NotionClient(token_v2=os.environ.get('NOTION_TOKEN'))
page = CLIENT.get_block(os.environ.get('NOTION_PAGE'))

def list():
    todos = [(todo.title, index) for index, todo in enumerate(page.children)]
    default = [index for index, todo in enumerate(page.children) if todo.checked]
    checked = prompt.checkbox(page.title, choices=todos, default=default)
    changed = set(checked).symmetric_difference(set(default))

    for index in changed:
        page.children[index].checked = index in checked

def add(todo):
    if todo == '':
        todo = prompt.editor('Write todo')
        print(todo)
    page.children.add_new(TodoBlock, title=todo)

def remove():
    index, todo = select_todo()
    if prompt.confirm('Are you sure?'):
        page.children[index].remove()

def edit():
    index, todo_to_edit = select_todo()
    edited_todo = prompt.editor(
        'Editing ' + todo_to_edit,
        default=todo_to_edit
    )
    page.children[index].title = edited_todo

def select_todo():
    todos = [todo.title for todo in page.children]

    todo = prompt.list_input(
        'Select Todo',
        choices=todos,
    )

    index = todos.index(todo)

    return index, todo
