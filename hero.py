from items import Armor

from read_config import HERO_CLASS_OPTIONS


class Hero:

    def __init__(self, name, level, xp, gender, style, hp, mp=None, armor_set=None):
        self.name = name
        self.level = level
        self.xp = xp
        self.gender = gender
        self.style = style
        self.hp = hp
        self.mp = mp
        self.armor_set = armor_set

        if isinstance(self.armor_set, list):
            armor_types = [i.armor_type for i in armor_set]
            if len(armor_types) > len(set(armor_types)):
                raise ValueError('Can only equip 1 of each armor type!')

        if self.style not in HERO_CLASS_OPTIONS:
            raise ValueError('No such class: {}'.format(self.style))

    def __str__(self):
        return '{}, Lvl: {}, Class: {}'.format(self.name, self.level, self.style)

    @property
    def armor_value_total(self):
        if not self.armor_set:
            return 0
        if isinstance(self.armor_set, list):
            total = 0
            for a in self.armor_set:
                total += a.armor_value

            return total

    def page(self):
        print('*' * 20)
        print('Name:\t{}'.format(self.name))
        print('Class:\t{}'.format(self.style))
        print('Level:\t{}'.format(self.level))
        print('XP:\t{}'.format(self.xp))
        print('Armor:\t{}'.format(self.armor_value_total))
        print('HP:\t{}'.format(self.hp))
        print('MP:\t{}'.format(self.mp))
        print('*' * 20)

    def take_damage(self, damage_amount):
        self.hp -= damage_amount
        if self.hp <= 0:
            self.die()

    def spend_mp(self, mp_cost):
        if self.mp >= mp_cost:
            self.mp -= mp_cost
        else:
            return 'Not enough MP!'

    def gain_xp(self, xp_gained):
        self.xp += xp_gained
        if self.level - 1 < self.xp // 1000:
            self.level_up()

    def level_up(self):
        self.level += 1
        print('You''ve reached level {}!'.format(self.level))

    def die(self):
        raise NotImplementedError


class Party:

    def __init__(self, heroes):
        self.heroes = heroes
        if not isinstance(self.heroes, list):
            self.heroes = [self.heroes]

    def __str__(self):
        return 'Current Party: ' + ', '.join([h.name for h in self.heroes])

    def inventory(self):
        pass


if __name__ == '__main__':
    pass
