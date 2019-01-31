from abc import ABC


class ItemBase(ABC):
    """
    Base class for all Items
    """

    def __init__(self, name, buy_price=None, sell_price=None):
        self.name = name
        self.buy_price = buy_price
        self.sell_price = sell_price

    def __str__(self):
        return self.name


class Weapon(ItemBase):

    def __init__(self, name, weapon_type, damage):
        super(Weapon, self).__init__(name)
        self.weapon_type = weapon_type
        self.damage = damage


class Armor(ItemBase):

    def __init__(self, name, armor_type, armor_value):
        super(Armor, self).__init__(name)
        self.armor_type = armor_type
        self.armor_value = armor_value


class Potion(ItemBase):

    def __init__(self, name, action, value):
        super(Potion, self).__init__(name)
        self.action = action
        self.value = value

    def use(self, hero):
        raise NotImplementedError


class Scroll(ItemBase):

    def __init__(self, name):
        super(Scroll, self).__init__(name)


class Consumable(ItemBase):

    def __init__(self, name):
        super(Consumable, self).__init__(name)


if __name__ == '__main__':
    w = Weapon('iron blade', 'sword', 35)
    a = Armor('iron helm', 'helmet', 50)
    print(w.__dict__)
    print(a.__dict__)