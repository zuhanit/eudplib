from typing import Literal, TypeAlias

DefUpgradeDict: dict[str, int] = {
    "Terran Infantry Armor": 0,
    "Terran Vehicle Plating": 1,
    "Terran Ship Plating": 2,
    "Zerg Carapace": 3,
    "Zerg Flyer Carapace": 4,
    "Protoss Armor": 5,
    "Protoss Plating": 6,
    "Terran Infantry Weapons": 7,
    "Terran Vehicle Weapons": 8,
    "Terran Ship Weapons": 9,
    "Zerg Melee Attacks": 10,
    "Zerg Missile Attacks": 11,
    "Zerg Flyer Attacks": 12,
    "Protoss Ground Weapons": 13,
    "Protoss Air Weapons": 14,
    "Protoss Plasma Shields": 15,
    "U-238 Shells": 16,
    "Ion Thrusters": 17,
    "Burst Lasers (Unused)": 18,
    "Titan Reactor (SV +50)": 19,
    "Ocular Implants": 20,
    "Moebius Reactor (Ghost +50)": 21,
    "Apollo Reactor (Wraith +50)": 22,
    "Colossus Reactor (BC +50)": 23,
    "Ventral Sacs": 24,
    "Antennae": 25,
    "Pneumatized Carapace": 26,
    "Metabolic Boost": 27,
    "Adrenal Glands": 28,
    "Muscular Augments": 29,
    "Grooved Spines": 30,
    "Gamete Meiosis (Queen +50)": 31,
    "Metasynaptic Node (Defiler +50)": 32,
    "Singularity Charge": 33,
    "Leg Enhancements": 34,
    "Scarab Damage": 35,
    "Reaver Capacity": 36,
    "Gravitic Drive": 37,
    "Sensor Array": 38,
    "Gravitic Boosters": 39,
    "Khaydarin Amulet (HT +50)": 40,
    "Apial Sensors": 41,
    "Gravitic Thrusters": 42,
    "Carrier Capacity": 43,
    "Khaydarin Core (Arbiter +50)": 44,
    "Unused45": 45,
    "Unused46": 46,
    "Argus Jewel (Corsair +50)": 47,
    "Unused48": 48,
    "Argus Talisman (DA +50)": 49,
    "Unused50": 50,
    "Caduceus Reactor (Medic +50)": 51,
    "Chitinous Plating": 52,
    "Anabolic Synthesis": 53,
    "Charon Booster": 54,
    "Unused55": 55,
    "Unused56": 56,
    "Unused57": 57,
    "Unused58": 58,
    "Unused59": 59,
    "Unused60": 60,
}

DefaultUpgrade: TypeAlias = Literal[
    "Terran Infantry Armor",
    "Terran Vehicle Plating",
    "Terran Ship Plating",
    "Zerg Carapace",
    "Zerg Flyer Carapace",
    "Protoss Armor",
    "Protoss Plating",
    "Terran Infantry Weapons",
    "Terran Vehicle Weapons",
    "Terran Ship Weapons",
    "Zerg Melee Attacks",
    "Zerg Missile Attacks",
    "Zerg Flyer Attacks",
    "Protoss Ground Weapons",
    "Protoss Air Weapons",
    "Protoss Plasma Shields",
    "U-238 Shells",
    "Ion Thrusters",
    "Burst Lasers (Unused)",
    "Titan Reactor (SV +50)",
    "Ocular Implants",
    "Moebius Reactor (Ghost +50)",
    "Apollo Reactor (Wraith +50)",
    "Colossus Reactor (BC +50)",
    "Ventral Sacs",
    "Antennae",
    "Pneumatized Carapace",
    "Metabolic Boost",
    "Adrenal Glands",
    "Muscular Augments",
    "Grooved Spines",
    "Gamete Meiosis (Queen +50)",
    "Metasynaptic Node (Defiler +50)",
    "Singularity Charge",
    "Leg Enhancements",
    "Scarab Damage",
    "Reaver Capacity",
    "Gravitic Drive",
    "Sensor Array",
    "Gravitic Boosters",
    "Khaydarin Amulet (HT +50)",
    "Apial Sensors",
    "Gravitic Thrusters",
    "Carrier Capacity",
    "Khaydarin Core (Arbiter +50)",
    "Unused45",
    "Unused46",
    "Argus Jewel (Corsair +50)",
    "Unused48",
    "Argus Talisman (DA +50)",
    "Unused50",
    "Caduceus Reactor (Medic +50)",
    "Chitinous Plating",
    "Anabolic Synthesis",
    "Charon Booster",
    "Unused55",
    "Unused56",
    "Unused57",
    "Unused58",
    "Unused59",
    "Unused60",
]
