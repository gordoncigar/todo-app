FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

def time(datetime):
    now = datetime.datetime(2025, 3, 7, 10, 30, 0)
    formatted_date = now.strftime("%d %B, %Y")
    return formatted_date


if __name__ =="__main__":
    print("hello")
    print(get_todos())