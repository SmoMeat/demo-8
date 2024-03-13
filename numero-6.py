def main() -> None:
    with open('a.txt', 'r', encoding='UTF-8') as file_a:
        lines = file_a.readlines()
        formated_lines = list(
            map(
                lambda line: ' ' * (79 - len(line)) + line,
                lines
            )
        )

        with open('b.txt', 'w', encoding='UTF-8') as file_b:
            file_b.writelines(formated_lines)


if __name__ == '__main__':
    main()