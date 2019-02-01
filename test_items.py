import unittest

from items import Armor


class ArmorTestCase(unittest.TestCase):

    def setUp(self):
        self.armor = Armor('iron helm', 'Head', 50)

    def tearDown(self):
        pass

    def test_damage(self):
        self.assertTrue(self.armor.armor_value > 0)


if __name__ == '__main__':
    unittest.main()
