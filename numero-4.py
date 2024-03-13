def main() -> None:
    with open('a.txt', 'r', encoding='UTF-8') as file_a:
        content = file_a.read().upper()
        with open('b.txt', 'w', encoding='UTF-8') as file_b:
            file_b.write(content)

if __name__ == '__main__':
    main()