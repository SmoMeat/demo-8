def somme_fichier(path: str) -> int:
    sum = 0
    with open(path, 'r') as file:
        for line in file.readlines():
            for number in line.split():
                sum += int(number)
    return sum

if __name__ == '__main__':
    print(somme_fichier('numbers.txt'))