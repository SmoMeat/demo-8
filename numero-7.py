from datetime import datetime

def justify(path):
    with open(path, 'r+', encoding='UTF-8') as file:
        lines = list(
            map(
                lambda line: line.removesuffix('\n'),
                file.readlines()
            )
        )
        txt = ' '.join(lines)
        formated_lines = list(
            map(
                lambda line: line + '. \n' if line[-1] != '.' else line,
                txt.split('. ')
            )
        )

    new_path = f'{path.removesuffix('.txt')}-{int(datetime.timestamp(datetime.now()))}-formatted.txt'
    print(new_path)
    with open(new_path, 'x', encoding='UTF-8') as file:
        file.writelines(formated_lines)

if __name__ == '__main__':
    justify('c.txt')