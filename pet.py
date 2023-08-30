class Pet:
    def __init__(self, strength=0, agility=0, intellect=0, will=0, power=0):
        self.strength = strength
        self.agility = agility
        self.intellect = intellect
        self.will = will
        self.power = power

        self.stats = {
            "strength": self.strength,
            "agility": self.agility,
            "will": self.will,
            "power": self.power,
            "intellect": self.intellect,
        }

        self.selfish_talents = {
            # ULTRA RARE
            "Mighty": {"strength": 65},
            "Brilliant": {"intellect": 65},
            "Relentless": {"agility": 65},
            "Thinkin' Cap": {"will": 65},
            "Powerful": {"power": 65},
            "Best of Shows": {"strength": 40, "intellect": 25},
            "Unshakeable": {"strength": 40, "agility": 25},
            "Cautious": {"strength": 40, "will": 40},
            "Vigorous": {"strength": 40, "power": 40},
            "Cunning": {"intellect": 25, "agility": 40},
            "Perceptive": {"intellect": 40, "will": 25},
            "Resourceful": {"intellect": 40, "power": 25},
            "Early Bird": {"agility": 40, "will": 25},
            "Refreshed": {"agility": 25, "power": 40},
            "Capable": {"will": 40, "power": 25},
            # RARE
            "Tenacious": {"strength": 50},
            "Astute": {"intellect": 50},
            "Durable": {"agility": 50},
            "Crafty": {"will": 50},
            "Spirited": {"power": 50},
            "Stalwart": {"strength": 25, "intellect": 25},
            "Tireless": {"strength": 25, "agility": 25},
            "Vigilant": {"strength": 25, "will": 25},
            "Dashing": {"strength": 25, "power": 25},
            "Efficient": {"intellect": 25, "agility": 25},
            "Intuitive": {"intellect": 25, "will": 25},
            "Gifted": {"intellect": 25, "power": 25},
            "Well Trained": {"agility": 25, "will": 25},
            "Courageous": {"agility": 25, "power": 25},
            "Careful": {"will": 25, "power": 25},
            # UNCOMMON
            "Rugged": {"strength": 40},
            "Sharp": {"intellect": 40},
            "Steadfast": {"agility": 40},
            "Canny": {"will": 40},
            "Eager": {"power": 40},
            "Adroit": {"strength": 15, "intellect": 25},
            "Determined": {"strength": 15, "agility": 25},
            "Dependable": {"strength": 25, "will": 15},
            "Effervescent": {"strength": 25, "power": 15},
            "Effective": {"intellect": 25, "agility": 15},
            "Attentive": {"intellect": 15, "will": 25},
            "Quick-Witted": {"intellect": 15, "power": 25},
            "Sturdy": {"agility": 15, "will": 25},
            "Interpid": {"agility": 25, "power": 15},
            "Forceful": {"will": 15, "power": 25},
            # COMMON
            "Hearty": {"strength": 25},
            "Calculating": {"intellect": 25},
            "Dogged": {"agility": 25},
            "Wise": {"will": 25},
            "Cheeky": {"power": 25},
        }

        self.talents = {
            "Damage": {
                "Boon": 0,
                "Giver": 0,
                "Dealer": 0,
            },
            "Resist": {
                "Defy": 0,
                "Proof": 0,
                "Ward": 0,
            },
            "Critical": {
                "Critical Hitter": 0,
                "Critical Striker": 0,
                "Striker": 0,
                "Assailant": 0,
            },
            "Critical Block": {
                "Blocker": 0,
                "Defender": 0,
            },
            "Armor Piercing": {
                "Piercer": 0,
                "Breaker": 0,
            },
            "Out. Healing": {
                "Healer": 0,
                "Medic": 0,
            },
            "Accuracy": {
                "Eye": 0,
                "Shot": 0,
                "Sniper": 0,
            },
        }

        self.load_talents()

    def load_talents(self):
        Agility = self.agility
        Will = self.will
        Power = self.power
        Strength = self.strength
        Intellect = self.intellect

        self.talents["Damage"]["Boon"] = int(
            (1 / 400) * (2 * Strength + 2 * Will + Power)
        )
        self.talents["Damage"]["Giver"] = int(
            (2 / 400) * (2 * Strength + 2 * Will + Power)
        )
        self.talents["Damage"]["Dealer"] = int(
            (3 / 400) * (2 * Strength + 2 * Will + Power)
        )

        self.talents["Resist"]["Defy"] = int(
            (1 / 250) * (2 * Strength + 2 * Agility + Power)
        )
        self.talents["Resist"]["Proof"] = int(
            (2 / 250) * (2 * Strength + 2 * Agility + Power)
        )
        self.talents["Resist"]["Ward"] = int(
            (3 / 250) * (2 * Strength + 2 * Agility + Power)
        )

        self.talents["Accuracy"]["Eye"] = int(
            (1 / 400) * (2 * Intellect + 2 * Agility + Power)
        )
        self.talents["Accuracy"]["Shot"] = int(
            (2 / 400) * (2 * Intellect + 2 * Agility + Power)
        )
        self.talents["Accuracy"]["Sniper"] = int(
            (3 / 400) * (2 * Intellect + 2 * Agility + Power)
        )

        self.talents["Critical"]["Critical Hitter"] = int(
            (18 / 1000) * (2 * Agility + 2 * Will + Power)
        )
        self.talents["Critical"]["Critical Striker"] = int(
            (24 / 1000) * (2 * Agility + 2 * Will + Power)
        )
        self.talents["Critical"]["Striker"] = int(
            (20 / 1000) * (2 * Agility + 2 * Will + Power)
        )
        self.talents["Critical"]["Assailant"] = int(
            (25 / 1000) * (2 * Agility + 2 * Will + Power)
        )

        self.talents["Critical Block"]["Blocker"] = int(
            (18 / 1000) * (2 * Intellect + 2 * Will + Power)
        )
        self.talents["Critical Block"]["Defender"] = int(
            (24 / 1000) * (2 * Intellect + 2 * Will + Power)
        )

        self.talents["Armor Piercing"]["Piercer"] = int(
            (3 / 2000) * (2 * Strength + 2 * Agility + Power)
        )
        self.talents["Armor Piercing"]["Breaker"] = int(
            (5 / 2000) * (2 * Strength + 2 * Agility + Power)
        )

        self.talents["Out. Healing"]["Healer"] = int(
            (6 / 2000) * (2 * Strength + 2 * Will + Power)
        )
        self.talents["Out. Healing"]["Medic"] = int(
            (13 / 2000) * (2 * Strength + 2 * Will + Power)
        )
