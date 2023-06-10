from colorama import Fore, Back, Style
import random


class Player:
    def __init__(self):

        self.player_input = None
        self.player_ships = 3
        self.player_field = []

    def switch_player(self):
        self.active_player, self.passive_player = self.passive_player, self.active_player

    def get_input(self):
        if self.active_player == 'player':
            self.player_input = input(Fore.YELLOW + 'Координаты цели?').upper()
            self.player_field.append(self.player_input)
        else:
            print('qewr')

        print(self.player_field)


class Game:
    def __init__(self):
        self.game_status = None
        self.player_ship_counter = 0
        self.active_player = 'player'
        self.passive_player = 'comp'

    def check_status(self):
        if self.player_ship_counter == 0:
            self.game_status = 'start'
            print('22')
        return self.game_status

    def ships_setting(self):
        player = Player()
        player.get_input()


def main():
    #   запуск цикла
    # 1. проверяем статус игры - старт, бой, финиш
    # 2. старт - расстановка кораблей
    # 3. бой - активный игрок вводит координаты клетки
    #   проверка клетки с полем пасссивного игрока
    #   вывод результата, запись изменений в полях
    #   определение статуса игры - бой или финиш.
    #   если бой - смена активного и пассивного игроков
    # 4. финиш - вывод информации о победителе.
    #   остановка цикла

    game = Game()
    player=Player()

    while True:
        game.check_status()
        print(game.game_status)
        print(player.active_player)
        if game.game_status == 'start':
            game.ships_setting()
        else:
            print('33')
        player.switch_player()




main()
