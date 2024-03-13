def compter(first_text: str, second_text: str) -> int:
    return first_text.count(second_text)

def test_compter() -> None:
    assert compter('Salut, bonjour, allo, bonjour', 'bonjour') == 2
    assert compter('Salut, bonjour, allo', 'bonjour') == 1
    assert compter('Salut, bonjour, allo, bonjr', 'bonjour') == 1
    assert compter('a, a, a, a, b, c, d, d', 'a') == 4



if __name__ == '__main__':
    test_compter()
    print(compter('Salut, bonjour, allo, bonjour', 'bonjour'))