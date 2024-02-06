def read_cache(path):
    try:
        with open(path, 'r') as file:
            return not bool(file.read())  # True if file is empty, False otherwise
    except FileNotFoundError:
        with open(path, 'w') as file:
            pass
        return True


def check_executed():
    file_path = 'scripts/.cache'
    is_empty = read_cache(file_path)

    if is_empty:
        with open(file_path, 'w') as file:
            file.write("Executed")
        return False
    else:
        return True
