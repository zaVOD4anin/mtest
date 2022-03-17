def input_files():
    files = []
    for i in range(int(input('enter num files: '))):
        files.append(input(f'Enter name file{i + 1}: '))
        if not files[i].endswith('.txt'):
            files[i] += '.txt'
    return files


def create_file():
    files = input_files()
    try:
        with open('union.txt', 'a') as un_file:
            for file in files:
                with open(file) as k:
                    un_file.write(f'{k.read()}')
    except:
        print('Fail open')
    else:
        print('Union file created')


if __name__ == '__main__':
    create_file()
