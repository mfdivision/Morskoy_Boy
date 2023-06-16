from colorama import Fore, Back, Style
import random



class Fields:
    computer_field = {'A1': " ", 'A2': " ", 'A3': " ", 'A4': " ", 'A5': " ", 'A6': " ",
                      'B1': " ", 'B2': " ", 'B3': " ", 'B4': " ", 'B5': " ", 'B6': " ",
                      'C1': " ", 'C2': " ", 'C3': " ", 'C4': " ", 'C5': " ", 'C6': " ",
                      'D1': " ", 'D2': " ", 'D3': " ", 'D4': " ", 'D5': " ", 'D6': " ",
                      'E1': " ", 'E2': " ", 'E3': " ", 'E4': " ", 'E5': " ", 'E6': " ",
                      'F1': " ", 'F2': " ", 'F3': " ", 'F4': " ", 'F5': " ", 'F6': " "
                      }
    player_field = {'A1': " ", 'A2': " ", 'A3': " ", 'A4': " ", 'A5': " ", 'A6': " ",
                    'B1': " ", 'B2': " ", 'B3': " ", 'B4': " ", 'B5': " ", 'B6': " ",
                    'C1': " ", 'C2': " ", 'C3': " ", 'C4': " ", 'C5': " ", 'C6': " ",
                    'D1': " ", 'D2': " ", 'D3': " ", 'D4': " ", 'D5': " ", 'D6': " ",
                    'E1': " ", 'E2': " ", 'E3': " ", 'E4': " ", 'E5': " ", 'E6': " ",
                    'F1': " ", 'F2': " ", 'F3': " ", 'F4': " ", 'F5': " ", 'F6': " "
                    }
    computer_field_ships = {'A1': " ", 'A2': " ", 'A3': " ", 'A4': " ", 'A5': " ", 'A6': " ",
                            'B1': " ", 'B2': " ", 'B3': " ", 'B4': " ", 'B5': " ", 'B6': " ",
                            'C1': " ", 'C2': " ", 'C3': " ", 'C4': " ", 'C5': " ", 'C6': " ",
                            'D1': " ", 'D2': " ", 'D3': " ", 'D4': " ", 'D5': " ", 'D6': " ",
                            'E1': " ", 'E2': " ", 'E3': " ", 'E4': " ", 'E5': " ", 'E6': " ",
                            'F1': " ", 'F2': " ", 'F3': " ", 'F4': " ", 'F5': " ", 'F6': " "
                            }

class Computer:
    def comp_shot():
        x = random.choice(['A', 'B', 'C', 'D', 'E', 'F'])
        y = random.choice(['1', '2', '3', '4', '5', '6'])
        v = x + y
        if v in game.player_ships_list:
            print(Fore.BLACK + Back.LIGHTMAGENTA_EX + f'Компьютер попал в {v}')
            game.player_ships_list.remove(v)
            print(f'У нас осталось {len(game.player_ships_list)} хп')
            print(Style.RESET_ALL)
        else:
            print(Fore.BLACK + Back.LIGHTYELLOW_EX + 'Компьютер промахнулся')
            print(v)
            print(Style.RESET_ALL)


    def computer_ships(self):  # расставляем корабли для компьютера
        self.c = ['A', 'B', 'C', 'D', 'E', 'F']
        self.n = ['1', '2', '3', '4', '5', '6']
        self.ship_length = [3, 2, 2, 1, 1, 1]  # задаем количество кораблей и палуб в них

        # проходим циклом по списку кораблей. случайным образом генерируем начальную клетку
        # и расположение корабля - горизонтальное или вертикальное. Вписываем корабль в поле.

        while game.comp_ship_counter <= 6:
            for ii in self.ship_length:
                self.random_dir = random.randint(1, 2)
                self.x = random.choice(self.c)
                self.s = self.c.index(self.x)
                self.z = random.choice(self.n)
                self.q = self.n.index(self.z)

                self.head = self.x + self.z
                # print(f'Head {self.head}, orient {self.random_dir}')

                if self.random_dir == 1:
                    if self.s + ii < 6:
                        self.next_letters = self.c[self.s:self.s + ii]

                        for i in self.next_letters:
                            self.next_cell = i + self.z
                            game.comp_ship_counter += 1
                            game.comp_ships_list.append(self.next_cell)
                            Fields.computer_field_ships[self.next_cell] = '#'

                    else:
                        self.next_letters = self.c[self.s + 1 - ii:self.s + 1]
                        for i in self.next_letters:
                            self.next_cell = i + self.z
                            game.comp_ship_counter += 1
                            game.comp_ships_list.append(self.next_cell)
                            Fields.computer_field_ships[self.next_cell] = '#'

                else:
                    if self.q + ii < 6:
                        self.next_figures = self.n[self.q:self.q + ii]
                        for i in self.next_figures:
                            self.next_cell = self.x + i
                            game.comp_ship_counter += 1
                            game.comp_ships_list.append(self.next_cell)
                            Fields.computer_field_ships[self.next_cell] = '#'

                    else:
                        self.next_figures = self.n[self.q + 1 - ii:self.q + 1]
                        for i in self.next_figures:
                            self.next_cell = self.x + i
                            game.comp_ship_counter += 1
                            game.comp_ships_list.append(self.next_cell)
                            Fields.computer_field_ships[self.next_cell] = '#'

class Player():
    def shot():
        shot = input(Fore.BLACK + Back.LIGHTYELLOW_EX + 'Координаты цели?').upper()
        return shot

    def player_shoot(shot):
        q = Fields()

        if shot in q.computer_field_ships:
            if q.computer_field_ships[shot] == '#':
                q.computer_field[shot] = 'X'
                game.comp_ship_counter -= 1
                print(Fore.BLACK + Back.LIGHTGREEN_EX + 'Есть попадание!')
                print(Style.RESET_ALL)
            else:
                q.computer_field[shot] = 'O'
                print(Fore.BLACK + Back.LIGHTRED_EX + 'Промах')
                print(Style.RESET_ALL)


class Game():
    def __init__(self):
        self.check_win = 'start'
        self.player = Player()
        self.ship_counter = 0
        self.game_checker = 0
        self.comp_ship_counter = 0
        self.comp_ships_list = []
        self.player_ships_list = []
        self.busy_cells = []
        self.active_player = 'player'
        self.passive_player = 'comp'

    def switch_player(self):
        self.active_player, self.passive_player = self.passive_player, self.active_player

    def check_status(self):
        if self.ship_counter == 0:
            game.check_win = 'start'

        elif len(game.comp_ships_list)  == 0 and len(game.player_ships_list) > 0:
            self.check_win = 'finish'

        elif len(game.comp_ships_list) > 0 and len(game.player_ships_list) == 0:
            self.check_win = 'finish'


        elif len(game.comp_ships_list) == 10 and len(game.player_ships_list) == 10:
            self.check_win = 'fight'

    def start(self):
        q = Fields()
        ships = [3, 2, 2, 1, 1, 1]
        # ships = [2, 1]

        for i in range(len(ships)):
            for ii in range(ships[i]):
                print(Fore.LIGHTBLUE_EX + f'Игрок 1, вводим {i + 1}-й корабль,  {ships[i]}-палубник:')
                user_input = input(Fore.LIGHTBLUE_EX + f'Палуба {ii + 1}').upper().replace(" ", "")

                q.player_field[user_input] = '#'
                self.ship_counter += 1
                self.player_ships_list.append(user_input)

            self.print_player_field()

    def print_player_field(self):
        q = Fields()
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        print(Fore.GREEN + 'Игрок 1')
        print(Fore.GREEN + '    1   2   3   4   5   6')

        for ii in range(6):
            print(Fore.GREEN +
                  f'''{letters[ii]} | {q.player_field[letters[ii] + '1']} | {q.player_field[letters[ii] + '2']} | {q.player_field[letters[ii] + '3']} | {q.player_field[letters[ii] + '4']} | {q.player_field[letters[ii] + '5']} | {q.player_field[letters[ii] + '6']} |''')

    def print_comp_field(self):
        q = Fields()
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        print(Fore.RED + 'Компьютер')
        print(Fore.RED + '    1   2   3   4   5   6')
        for ii in range(6):
            print(Fore.RED +
                  f'''{letters[ii]} | {q.computer_field[letters[ii] + '1']} | {q.computer_field[letters[ii] + '2']} | {q.computer_field[letters[ii] + '3']} | {q.computer_field[letters[ii] + '4']} | {q.computer_field[letters[ii] + '5']} | {q.computer_field[letters[ii] + '6']} |''')

    def comp_field(self):
        q = Fields()
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        print(Fore.MAGENTA + 'Компьютер расстановка')
        print(Fore.MAGENTA + '    1   2   3   4   5   6')
        for ii in range(6):
            print(Fore.MAGENTA +
                  f'''{letters[ii]} | {q.computer_field_ships[letters[ii] + '1']} | {q.computer_field_ships[letters[ii] + '2']} | {q.computer_field_ships[letters[ii] + '3']} | {q.computer_field_ships[letters[ii] + '4']} | {q.computer_field_ships[letters[ii] + '5']} | {q.computer_field_ships[letters[ii] + '6']} |''')


def main():
    ship = Computer()

    while True:
        game.check_status()
        print(game.check_win, game.comp_ship_counter, game.game_checker)
        print(game.active_player, game.passive_player)
        if game.check_win == 'start':
            game.start()
            ship.computer_ships()
            # game.comp_field()
            game.print_player_field()
            print(game.comp_ships_list)
            print(game.player_ships_list)


        elif game.check_win == 'fight':
            if game.active_player == 'player':
                q = Player.shot()
                Player.player_shoot(q)
            else:
                print('Ход компа')
                print(Computer.comp_shot())

            print(f' осталось {len(game.player_ships_list)} ')
            game.print_player_field()
            game.print_comp_field()
            game.switch_player()

        elif game.check_win == 'finish':
            if len(game.comp_ships_list) == 0 and len(game.player_ships_list) > 0:
                print('Поздравляем с победой!')

            elif len(game.comp_ships_list) > 0 and len(game.player_ships_list) == 0:
                print("Вы проиграли")
            break


if __name__ == "__main__":
    game = Game()
    main()
