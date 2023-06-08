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


class Computer(Fields):
    pass


class Ship():
    def __init__(self):
        self.next_cell = 0

    def search_free_cells(self):
        if Fields.computer_field_ships[self.next_cell] == '#' :
            pass
            # print(f'{self.next_cell} занята')
            # game.comp_ship_counter -= 1


        else:
            game.comp_ship_counter += 1
            Fields.computer_field_ships[self.next_cell] = '#'





    def computer_ships(self):   # расставляем корабли для компьютера
        self.ii=None
        self.c = ['A', 'B', 'C', 'D', 'E', 'F']
        self.n = ['1', '2', '3', '4', '5', '6']
        self.ship_length = [3, 2, 2, 1, 1, 1, 1]  # задаем количество кораблей и палуб в них

        # проходим циклом по списку кораблей. случайным образом генерируем начальную клетку
        # и раположение - горизонтальное или вертикальное.
        # проверяем


        while game.comp_ship_counter <= 3:
            for ii in self.ship_length:
                self.random_dir = random.randint(1, 2)
                self.x = random.choice(self.c)
                self.s = self.c.index(self.x)
                self.z = random.choice(self.n)
                self.q=self.n.index(self.z)

                self.head = self.x + self.z

                if self.random_dir==1:
                    if self.s + ii < 6:
                        self.next_letters = self.c[self.s:self.s + ii]
                        self.search_free_cells()

                    else:
                        self.next_letters = self.c[self.s - ii:self.s]
                        for i in self.next_letters:
                            self.next_cell = i + self.z
                            print(self.next_cell)
                            self.search_free_cells()
                else:
                    if self.q + ii < 6:
                        self.next_figures = self.n[self.q:self.q + ii]
                        for i in self.next_figures:
                            self.next_cell = self.x + i
                            print(self.next_cell)
                            self.search_free_cells()
                    else:
                        self.next_figures = self.n[self.q - ii:self.q]
                        for i in self.next_figures:
                            self.next_cell = self.x + i
                            print(self.next_cell)
                            self.search_free_cells()


class Player():
    def __init__(self):
        pass

    def player_shoot(self):
        q = Fields()
        shot = input(Fore.YELLOW + 'Координаты цели?').upper()
        if shot in q.computer_field_ships:
            if q.computer_field_ships[shot] == '#':
                q.computer_field[shot] = 'X'
                game.comp_ship_counter -= 1
                print(Fore.RED + 'попадание')
                print(Style.RESET_ALL)
            else:
                q.computer_field[shot] = 'O'
                print(Fore.BLACK + Back.RED + 'промах')
                print(Style.RESET_ALL)


class Game():
    def __init__(self):
        self.check_win = 'start'
        self.player = Player()
        self.ship_counter = 0
        self.game_checker = 0
        self.comp_ship_counter = 0

    def check_status(self):
        if self.ship_counter == 0:
            game.check_win = 'start'

        elif self.comp_ship_counter == 0 and self.ship_counter == 2:
            self.check_win = 'finish'

        elif self.ship_counter == 2 and self.comp_ship_counter >= 1:
            self.check_win = 'fight'

    def start(self):

        # ships = [3, 2, 2, 1, 1, 1, 1]
        ships = [1, 1]

        for i in range(1):
            for ii in range(ships[i - 1]):
                print(Fore.LIGHTBLUE_EX + f'Игрок 1, вводим {i + 1}-й корабль,  {ships[i - 1]}-палубник:')
                user_input = input(Fore.LIGHTBLUE_EX + f'Палуба {ii + 1}').upper().replace(" ", "")
                q = Fields()
                q.player_field[user_input] = '#'
                self.ship_counter += 1

    def printField(self):
        q = Fields()
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        print(Fore.GREEN + 'Игрок 1')
        print(Fore.GREEN + '    1   2   3   4   5   6')

        for ii in range(6):
            print(Fore.GREEN +
                  f'''{letters[ii]} | {q.player_field[letters[ii] + '1']} | {q.player_field[letters[ii] + '2']} | {q.player_field[letters[ii] + '3']} | {q.player_field[letters[ii] + '4']} | {q.player_field[letters[ii] + '5']} | {q.player_field[letters[ii] + '6']} |''')

        print(Fore.RED + 'Компьютер')
        print(Fore.RED + '    1   2   3   4   5   6')
        for ii in range(6):
            print(Fore.RED +
                  f'''{letters[ii]} | {q.computer_field[letters[ii] + '1']} | {q.computer_field[letters[ii] + '2']} | {q.computer_field[letters[ii] + '3']} | {q.computer_field[letters[ii] + '4']} | {q.computer_field[letters[ii] + '5']} | {q.computer_field[letters[ii] + '6']} |''')

        print(Fore.MAGENTA + 'Компьютер расстановка')
        print(Fore.MAGENTA + '    1   2   3   4   5   6')
        for ii in range(6):
            print(Fore.MAGENTA +
                  f'''{letters[ii]} | {q.computer_field_ships[letters[ii] + '1']} | {q.computer_field_ships[letters[ii] + '2']} | {q.computer_field_ships[letters[ii] + '3']} | {q.computer_field_ships[letters[ii] + '4']} | {q.computer_field_ships[letters[ii] + '5']} | {q.computer_field_ships[letters[ii] + '6']} |''')


def main():
    ship=Ship()
    ship.computer_ships()

    while True:
        game.check_status()
        # print(game.check_win, game.comp_ship_counter, game.game_checker)
        if game.check_win == 'start':
            game.start()
            game.printField()

        elif game.check_win == 'fight':
            game.player.player_shoot()
            game.printField()

        elif game.check_win == 'finish':
            print('победа')
            break


if __name__ == "__main__":
    game = Game()
    main()
