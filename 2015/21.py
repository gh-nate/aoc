# Copyright (c) 2022 gh-nate
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from dataclasses import dataclass

import itertools
import sys


def prompt(message):
    return int(input(message).rstrip())


boss_hit = prompt('Please enter the hit points for the boss: ')
boss_damage = prompt('Please enter the damage score for the boss: ')
boss_armor = prompt('Please enter the armor score for the boss: ')


@dataclass
class Character:
    hit: int
    damage: int
    armor: int

    def attacked_by(self, attacker):
        damage_dealt = attacker.damage - self.armor
        self.hit -= damage_dealt if damage_dealt > 1 else 1


@dataclass(frozen=True)
class Item:
    name: str
    cost: int
    damage: int
    armor: int


class Weapon(Item):
    pass


class Armor(Item):
    pass


class Ring(Item):
    def __add__(self, other):
        return Ring(
            f'{self.name} + {other.name}',
            self.cost + other.cost,
            self.damage + other.damage,
            self.armor + other.armor,
        )


weapons = [
    Weapon('Dagger', 8, 4, 0),
    Weapon('Shortsword', 10, 5, 0),
    Weapon('Warhammer', 25, 6, 0),
    Weapon('Longsword', 40, 7, 0),
    Weapon('Greataxe', 74, 8, 0),
]
armors = [
    Armor('Leather', 13, 0, 1),
    Armor('Chainmail', 31, 0, 2),
    Armor('Splintmail', 53, 0, 3),
    Armor('Bandedmail', 75, 0, 4),
    Armor('Platemail', 102, 0, 5),
]
rings = [
    Ring('Damage +1', 25, 1, 0),
    Ring('Damage +2', 50, 2, 0),
    Ring('Damage +3', 100, 3, 0),
    Ring('Defense +1', 20, 0, 1),
    Ring('Defense +2', 40, 0, 2),
    Ring('Defense +3', 80, 0, 3),
]


def is_player_winner(player, opponent):
    while True:
        opponent.attacked_by(player)
        if opponent.hit <= 0:
            return True
        player.attacked_by(opponent)
        if player.hit <= 0:
            return False


def get_rings():
    yield Ring('', 0, 0, 0)
    for ring in rings:
        yield ring
    for ring_1, ring_2 in itertools.combinations(rings, 2):
        yield ring_1 + ring_2


def get_armors():
    yield Armor('', 0, 0, 0)
    for armor in armors:
        yield armor


def get_items():
    for weapon in weapons:
        for armor in get_armors():
            for ring in get_rings():
                yield weapon, armor, ring


least_amount_of_gold = sys.maxsize
most_amount_of_gold = 0
for w, a, r in get_items():
    cost = w.cost + a.cost + r.cost
    if is_player_winner(
        Character(100, w.damage + r.damage, a.armor + r.armor),
        Character(boss_hit, boss_damage, boss_armor),
    ):
        if cost < least_amount_of_gold:
            least_amount_of_gold = cost
    else:
        if cost > most_amount_of_gold:
            most_amount_of_gold = cost

print(f'Part 1: {least_amount_of_gold}')
print(f'Part 2: {most_amount_of_gold}')
