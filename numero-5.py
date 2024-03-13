def main() -> None:
    with open('a.txt', 'r', encoding='UTF-8') as file_a:
        content = file_a.read().split("'")
        for i in range(len(content)):
            if i % 2 == 0:
                content[i] = content[i].upper()

        formated_content = "'".join(content)

        with open('b.txt', 'w', encoding='UTF-8') as file_b:
            file_b.write(formated_content)

if __name__ == '__main__':
    main()