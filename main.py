from items import Armor, Weapon, Potion
from hero import Hero, Party


def main():
    armor_set = [
        Armor('iron helm', 'Head', 25),
        Armor('iron pauldrons', 'Shoulders', 25),
        Armor('iron greaves', 'Feet', 25)
    ]

    hero = Hero('Clint', 1, 1000, 0, 'Paladin', 100, 100, armor_set)

    party = Party(hero)

    hero.page()
    print(party)


if __name__ == '__main__':
    main()
