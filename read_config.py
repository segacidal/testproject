import configparser

parser = configparser.RawConfigParser()
parser.read('master-config.cfg')

HERO_CLASS_OPTIONS = parser['heroes']['classes'].split(',')
WEAPON_TYPE_OPTIONS = parser['weapons']['weapon_types'].split(',')
ARMOR_TYPE_OPTIONS = parser['armors']['armor_types'].split(',')
