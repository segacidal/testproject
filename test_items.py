import unittest

from items import Weapon, Armor


class WeaponTestCase(unittest.TestCase):

    def setUp(self):
        self.weapon = Weapon('iron blade', 'sword', 35)

    def tearDown(self):
        pass

    def test_damage(self):
        self.assertTrue(self.weapon.damage > 0)


class ArmorTestCase(unittest.TestCase):

    def setUp(self):
        self.armor = Armor('iron helm', 'helm', 50)

    def tearDown(self):
        pass

    def test_damage(self):
        self.assertTrue(self.armor.armor_value > 0)


if __name__ == '__main__':
    unittest.main()
