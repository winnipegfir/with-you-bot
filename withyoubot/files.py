def change_file(file, change):
    with open('./' + file + '.txt', 'r') as f:
        counter = f.read()
    with open('./' + file + '.txt', 'w') as f:
        number = eval(counter + change + '1')
        f.write(str(number))


def read_file(file):
    with open('./' + file + '.txt', 'r') as f:
        number = f.read()

    return number


def commands_file():
    with open('./commands.json', 'r') as f:
        json = f.read()

    return json