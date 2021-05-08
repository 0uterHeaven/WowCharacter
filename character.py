import random


alliance = ['Human', 'Gnome', 'Night Elf', 'Dwarf']
horde = ['Orc', 'Undead', 'Troll', 'Tauren']
    
race = input('Are you Horde or Alliance? ')

if race == 'Horde':
    print(random.choice(horde))
elif race == 'Alliance':
    print(random.choice(alliance))
else:
    print('Please enter Horde or Alliance.')

ACharClass = ['Warrior', 'Mage', 'Rogue', 'Priest', 'Paladin', 'Hunter', 'Warlock', 'Druid', 'Shaman']
#HCharClass = ['Warrior', 'Mage', 'Rogue', 'Priest', 'Shaman', 'Hunter', 'Warlock', 'Druid']

rc = input('What race are you?')

if rc == 'Human'
