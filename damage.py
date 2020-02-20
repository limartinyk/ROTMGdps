import math
import matplotlib

# TODO state_builder
#state = {
#    "attack": 75,
#    "dexterity": 50,
#    "damaging": False,
#    "berserk": False,
#    "weak": False,
#    "dazed": False,
#    "shots": 4,
#    "min_shot": 80,
#    "max_shot": 120,
#    "atk_speed_mult": 1,
#    "defense": 20,
#    "cursed": False
#    }

# https://www.realmeye.com/wiki/character-stats

class Damage:
    def __init__(self, state):
        # OUTBOUND (attacking char)
        # stats
        self.attack = state["attack"]
        self.dexterity = state["dexterity"]
        # status TODO
        self.damaging = state["damaging"] # 1.5 damage after attack calculation
        self.berserk = state["berserk"] # 1.5 attack speed after dex calculation
        self.weak = state["weak"] # atk = 0
        self.dazed = state["dazed"] # dex = 0
        # items
        self.shots = state["shots"]
        self.avg_dmg_per_shot = (state["min_shot"] + state["max_shot"] - 1) / 2
        self.atk_speed_mult = state["atk_speed_mult"] # (ass, etherite, etc) TODO

        # INBOUND (defending char)
        # stats
        self.defense = state["defense"]
        # status TODO
        self.cursed = state["cursed"] # 1.2 damage taken after defense calculation

    def calculate_dps(self):
        shot_dmg = self.avg_dmg_per_shot * (0.5 + self.attack / 50)
        shot_dmg_def = max(math.floor(.15 * shot_dmg), shot_dmg - self.defense)

        attacks_per_second = 1.5 + 6.5 * (self.dexterity / 75)

        dps = shot_dmg_def * self.shots * attacks_per_second
        return dps

    def graph_dps(self):
        for defense in range(150):
            self.defense = defense
            self.calculate_dps()

state = { # max_rogue, foul, nothing else
    "attack": 50,
    "dexterity": 75,
    "damaging": False,
    "berserk": False,
    "weak": False,
    "dazed": False,
    "shots": 1,
    "min_shot": 95,
    "max_shot": 175,
    "atk_speed_mult": 1,
    "defense": 10,
    "cursed": False
    }



dmg = Damage(state)
print(dmg.calculate_dps())
