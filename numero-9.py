import re

class Bottin:
    def __init__(self):
        self.path = 'bottin.csv'
        self.bottin = self.parse_bottin()
    
    def __del__(self):
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.writelines(map(
                lambda person: f'{person['name']},{person['phone_number']}\n',
                self.bottin
            ))

    def search_by_phone(self, phone_number: str) -> list:
        to_return = []
        for person in self.bottin:
            if person['phone_number'] == phone_number:
                to_return.append(person)
        return to_return
    
    def search_by_name(self, name: str) -> list:
        to_return = []
        for person in self.bottin:
            if person['name'] == name:
                to_return.append(person)
        return to_return
    
    def append(self, name: str, phone_number: str) -> None:
        self.bottin.append({
            'name': name,
            'phone_number': phone_number
        })

    def parse_bottin(self) -> list[dict]:
        with open(self.path, 'r+', encoding='UTF-8') as file:
            bottin = map(
                lambda person: {
                    'name': person.split(',')[0],
                    'phone_number':  person.split(',')[1].removesuffix('\n')
                },
                file.readlines()
            )
        
        return list(bottin)
    
def terminal() -> None:
    bottin = Bottin()

    print('Bienvenue dans le bottin téléphonique !')
    print('Pour trouver une personne ')
    while (user_input := input('Voulez-vous ajouter (a) ou trouver une personne (s) ou quitter (q) : ')) not in ('q', ''):
        if user_input == 'a':
            name = input('Quelle est le nom de la personne à ajouter ? ')
            phone_number = input('Quelle est son numéro de téléphone ? ')
            bottin.append(name, phone_number)
        elif user_input == 's':
            info = input('Quelle est le nom ou le numéro de la personne ? ')
            
            if re.match('[0-9]+ [0-9]+-[0-9]+', info):
                search = bottin.search_by_phone(info)[0]
                print(f'{search['name']}, {search['phone_number']}')
            else:
                search = bottin.search_by_name(info)[0]
                print(f'{search['name']}, {search['phone_number']}')
    del bottin


if __name__ == '__main__':
    terminal()
    # bottin = Bottin()
    # bottin.append('mathieu', '438 501-3188')
    # print(bottin.search_by_phone('450 831-5133'))
    # print(bottin.search_by_name('jean'))
    # print(bottin.search_by_name('mathieu'))
    # del bottin