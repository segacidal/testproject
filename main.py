from items import Armor, Weapon, Potion
from hero import Hero, Party


def main():
    armor_set = [
        Armor('iron helm', 'helm', 25),
        Armor('iron pauldrons', 'shoulder', 25),
        Armor('iron greaves', 'feet', 25)
    ]

    hero = Hero('Clint', 1, 1000, 0, 'monk', 100, 0, armor_set)

    party = Party(hero)

    hero.page()


if __name__ == '__main__':
    main()
