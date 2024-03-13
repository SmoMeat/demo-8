def en_commun(first_text: str, second_text: str) -> bool:
    for char in map(lambda x: x, first_text):
        if char in map(lambda x: x, second_text):
            return True
    return False

def test_en_commun() -> None:
    assert en_commun('Allo', 'Bonjour')
    assert en_commun('batiment', 'texte')
    assert not en_commun('Allo', '学中文')
    assert not en_commun('ÉCOLE', 'six cent quatre (604)')

if __name__ == '__main__':
    test_en_commun()
    print(en_commun('allo bbb', 'l'))