FILEPATH="todos.txt"


def get_todos(filepath=FILEPATH):
    """REad a text file 'todos.txt' as file_local and return the contents
    to a list named todos_local by using readlines method with file context"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the contents of the list todos to the file named 'todos.txt'
    by using writlines method with file context"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)
