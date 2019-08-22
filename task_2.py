import os

def print_directory_contents(path):
    with os.scandir(path) as listOfEntries:
        for entry in listOfEntries:
            if entry.is_dir():
                print_directory_contents(os.path.join(path, entry.name))
            else:
                print(entry.name)


if __name__ == '__main__':
    print_directory_contents("/Users/michaelspasenko/PycharmProjects/exercises")
