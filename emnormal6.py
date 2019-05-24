# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _calculate_damage(self, damage, armor):
        return damage - damage * armor

    def attack(self, enemy_health, enemy_armor):
        damage = self._calculate_damage(self.damage, enemy_armor)
        enemy_health = enemy_health - damage
        return enemy_health


class Player(Person):
    pass


class Enemy(Person):
    pass


first_player = Player("Вася", 100, 20, 0.2)
second_player = Enemy("Петя", 100, 25, 0.2)


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def fight(self):
        last_attacker = self.player1
        while self.player1.health > 0 and self.player2.health > 0:
            if last_attacker == self.player1:
                self.player1.health = self.player2.attack(self.player1.health, self.player1.armor)
                last_attacker = self.player2
            else:
                self.player2.health = self.player1.attack(self.player2.health, self.player2.armor)
                last_attacker = self.player1

        if self.player1.health > 0:
            print(f'Игрок {self.player1.name} победил!')
        else:
            print(f'Игрок {self.player2.name} победил!')


game = Game(first_player, second_player)
game.fight()
