import unittest

from hero import Hero
from items import Armor


class HeroTestCase(unittest.TestCase):

    def setUp(self):
        armor_set = [
            Armor('iron helm', 'helm', 25),
            Armor('iron pauldrons', 'shoulder', 25),
            Armor('iron greaves', 'feet', 25)
        ]

        self.hero = Hero('clint', 2, 1500, 0, 'monk', armor_set)

    def tearDown(self):
        pass

    def test_armor_value_total(self):
        self.assertTrue(self.hero.armor_value_total > 0)

    def test_xp(self):
        self.assertTrue(self.hero.xp >= 0)

    def test_level(self):
        self.assertTrue(self.hero.level > 0)
        self.assertTrue(self.hero.level + 1 > self.hero.xp // 1000)


if __name__ == '__main__':
    unittest.main()