#!/usr/bin/env python3

'''
Viết 1 một trò chơi đánh đối kháng giữa 2 nhân vật. Mỗi nhân vật có tên (str),
máu (int), vũ khí.
Vũ khí chọn random khi tạo nhân vật, có damage (int) bằng lượng máu trừ đi
khi đánh trúng.

Cho 2 nhân vật lần lượt đánh nhau, print kết quả mỗi lượt đánh, print người
thắng.

'''
import random


class Fighter():
    def __init__(self, name, HP):
        self.name = name
        self.hp = HP
        self.weapon_dmg = (Weapon(random.randrange(int(self.hp / 10))).damage)

    def __str__(self):
        return (self.name, self.hp)


class Weapon():
    def __init__(self, damage):
        self.damage = damage


def solve(player1, player2):
    '''Trả về tuple tên người thắng cuộc và lượng máu còn lại (int)'''
    result = ('', 0)

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    no_turn = 0
    print('Player1: {0} vs Player 2: {1}'.format(player1.name, player2.name))
    print('*' * 12 + '=' * 10 + '*' * 12)
    while player1.hp > 0 and player2.hp > 0:
        no_turn += 1
        print('Turn : {}'.format(no_turn))
        print('Player 1 attack, damage = {}'.format(player1.weapon_dmg))
        player2.hp -= player1.weapon_dmg
        print('Player 2 hp left: {}'.format(player2.hp))
        if player2.hp <= 0:
            print('*' * 20)
            print('Player 2: {} lose'.format(player2.name))
            print('Player 1: {} win'.format(player1.name))
            result = (player1.name, player1.hp)
            break
        print('Player 2 attack: damage = {}'.format(player2.weapon_dmg))
        player1.hp -= player2.weapon_dmg
        print('Player 1 hp left: {}'.format(player1.hp))
        if player1.hp <= 0:
            print('*' * 20)
            print('Player 1: {} lose'.format(player1.name))
            print('Player 2: {} win'.format(player2.name))
            result = (player2.name, player2.hp)
            break
        print('*' * 20)
    return result


def main():
    # Thay đổi các dòng sau cho phù hợp
    player1 = Fighter('LiuKang', 1000)
    player2 = Fighter('KungLao', 1000)
    print(solve(player1, player2))


if __name__ == "__main__":
    main()
