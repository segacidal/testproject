import unittest

from items import Weapon


class WeaponTestCase(unittest.TestCase):

    def setUp(self):
        self.weapon = Weapon('iron blade', 'Sword', 35)

    def tearDown(self):
        pass

    def test_damage(self):
        self.assertTrue(self.weapon.damage > 0)


if __name__ == '__main__':
    unittest.main()
