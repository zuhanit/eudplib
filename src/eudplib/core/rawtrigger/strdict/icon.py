from typing import Literal, TypeAlias

DefIconDict: dict[str, int] = {
    "Marine": 0,
    "Ghost": 1,
    "Vulture": 2,
    "Goliath": 3,
    "Blank (Goliath Turret)": 4,
    "Siege Tank (Tank Mode)": 5,
    "Blank (Tank Turret)": 6,
    "SCV": 7,
    "Wraith": 8,
    "Science Vessel": 9,
    "Gui Montag": 10,
    "Gui Montag (Firebat)": 10,
    "Dropship": 11,
    "Battlecruiser": 12,
    "Vulture Spider Mine": 13,
    "Nuclear Missile": 14,
    "Civilian": 15,
    "Sarah Kerrigan": 16,
    "Sarah Kerrigan (Ghost)": 16,
    "Alan Schezar": 17,
    "Alan Schezar (Goliath)": 17,
    "Blank (Alan Turret)": 18,
    "Jim Raynor (Vulture)": 19,
    "Jim Raynor (Marine)": 20,
    "Tom Kazansky": 21,
    "Tom Kazansky (Wraith)": 21,
    "Magellan": 22,
    "Magellan (Science Vessel)": 22,
    "Edmund Duke (Siege Tank)": 23,
    "Blank (Duke Turret)": 24,
    "Edmund Duke (Siege Mode)": 25,
    "Blank (Siege Duke Turret)": 26,
    "Blank (Arcturus Mengsk)": 27,
    "Hyperion": 28,
    "Hyperion (Battlecruiser)": 28,
    "Norad II (Battlecruiser)": 29,
    "Terran Siege Tank (Siege Mode)": 30,
    "Blank (Siege Tank Turret)": 31,
    "Firebat": 32,
    "Marine (Scanner Sweep)": 33,
    "Medic": 34,
    "Larva": 35,
    "Radioactive (Zerg Egg)": 36,
    "Zergling": 37,
    "Hydralisk": 38,
    "Ultralisk": 39,
    "Broodling": 40,
    "Drone": 41,
    "Overlord": 42,
    "Mutalisk": 43,
    "Guardian": 44,
    "Queen": 45,
    "Defiler": 46,
    "Scourge": 47,
    "Torrarsque": 48,
    "Torrarsque (Ultralisk)": 48,
    "Matriarch": 49,
    "Matriarch (Queen)": 49,
    "Infested Terran": 50,
    "Infested Kerrigan": 51,
    "Infested Kerrigan (Infested Terran)": 51,
    "Unclean One": 52,
    "Unclean One (Defiler)": 52,
    "Hunter Killer": 53,
    "Hunter Killer (Hydralisk)": 53,
    "Devouring One": 54,
    "Devouring One (Zergling)": 54,
    "Kukulza (Mutalisk)": 55,
    "Kukulza (Guardian)": 56,
    "Yggdrasill": 57,
    "Yggdrasill (Overlord)": 57,
    "Valkyrie": 58,
    "Mutalisk/Guardian Cocoon": 59,
    "Corsair": 60,
    "Dark Templar (Unit)": 61,
    "Devourer": 62,
    "Dark Archon": 63,
    "Probe": 64,
    "Zealot": 65,
    "Dragoon": 66,
    "High Templar": 67,
    "Archon": 68,
    "Shuttle": 69,
    "Scout": 70,
    "Arbiter": 71,
    "Carrier": 72,
    "Interceptor": 73,
    "Dark Templar (Hero)": 74,
    "Zeratul": 75,
    "Zeratul (Dark Templar)": 75,
    "Tassadar/Zeratul": 76,
    "Tassadar/Zeratul (Archon)": 76,
    "Fenix (Zealot)": 77,
    "Fenix (Dragoon)": 78,
    "Tassadar": 79,
    "Tassadar (Templar)": 79,
    "Mojo": 80,
    "Mojo (Scout)": 80,
    "Warbringer": 81,
    "Warbringer (Reaver)": 81,
    "Gantrithor": 82,
    "Gantrithor (Carrier)": 82,
    "Reaver": 83,
    "Observer": 84,
    "Scarab": 85,
    "Danimoth": 86,
    "Danimoth (Arbiter)": 86,
    "Blank (Aldaris)": 87,
    "Artanis": 88,
    "Artanis (Scout)": 88,
    "Rhynadon": 89,
    "Rhynadon (Badlands Critter)": 89,
    "Bengalaas": 90,
    "Bengalaas (Jungle Critter)": 90,
    "Lurker (Cargo Ship - Unused)": 91,
    "Mercenary Gunship (Unused)": 92,
    "Scantid": 93,
    "Scantid (Desert Critter)": 93,
    "Kakaru": 94,
    "Kakaru (Twilight Critter)": 94,
    "Ragnasaur": 95,
    "Ragnasaur (Ashworld Critter)": 95,
    "Ursadon": 96,
    "Ursadon (Ice Critter)": 96,
    "Blank (Zerg Lurker Egg)": 97,
    "Blank (Raszagal)": 98,
    "Samir Duran": 99,
    "Samir Duran (Ghost)": 99,
    "Alexei Stukov": 100,
    "Alexei Stukov (Ghost)": 100,
    "Map Revealer": 101,
    "Blank (Gerard DuGalle)": 102,
    "Lurker": 103,
    "Infested Duran": 104,
    "Infested Duran (Infested Terran)": 104,
    "Blank (Disruption Field)": 105,
    "Command Center": 106,
    "Comsat Station": 107,
    "Nuclear Silo": 108,
    "Supply Depot": 109,
    "Refinery": 110,
    "Barracks": 111,
    "Academy": 112,
    "Factory": 113,
    "Starport": 114,
    "Control Tower": 115,
    "Science Facility": 116,
    "Covert Ops": 117,
    "Physics Lab": 118,
    "Blank (Starbase - Unused)": 119,
    "Machine Shop": 120,
    "Repair Bay (Unused)": 121,
    "Engineering Bay": 122,
    "Armory": 123,
    "Missile Tower": 124,
    "Bunker": 125,
    "Crashed Norad II": 126,
    "Ion Cannon": 127,
    "Uraj": 128,
    "Khalis": 129,
    "Infested Command Center": 130,
    "Hatchery": 131,
    "Lair": 132,
    "Hive": 133,
    "Nydus Canal": 134,
    "Hydralisk Den": 135,
    "Defiler Mound": 136,
    "Greater Spire": 137,
    "Queen's Nest": 138,
    "Evolution Chamber": 139,
    "Ultralisk Cavern": 140,
    "Spire": 141,
    "Spawning Pool": 142,
    "Creep Colony": 143,
    "Spore Colony": 144,
    "Radioactive (Zerg Bldg1 - Unused)": 145,
    "Sunken Colony": 146,
    "Overmind (Without Shell)": 147,
    "Overmind (With Shell)": 148,
    "Extractor": 149,
    "Mature Chrysalis": 150,
    "Cerebrate": 151,
    "Cerebrate Daggoth": 152,
    "Blank (Zerg Bldg2 - Unused)": 153,
    "Nexus": 154,
    "Robotics Facility": 155,
    "Pylon": 156,
    "Assimilator": 157,
    "Blank (Protoss Bldg1 - Unused)": 158,
    "Observatory": 159,
    "Gateway": 160,
    "Blank (Protoss Bldg2 - Unused)": 161,
    "Photon Cannon": 162,
    "Citadel of Adun": 163,
    "Cybernetics Core": 164,
    "Templar Archives": 165,
    "Forge": 166,
    "Stargate": 167,
    "Stasis Cell/Prison": 168,
    "Fleet Beacon": 169,
    "Arbiter Tribunal": 170,
    "Robotics Support Bay": 171,
    "Shield Battery": 172,
    "Khaydarin Crystal Formation": 173,
    "Protoss Temple": 174,
    "Xel'Naga Temple": 175,
    "Mineral Cluster (Type 1)": 176,
    "Mineral Cluster (Type 2)": 177,
    "Mineral Cluster (Type 3)": 178,
    "Blank (Cave - Unused)": 179,
    "Blank (Cave-in - Unused)": 180,
    "Blank (Cantina - Unused)": 181,
    "Blank (Mining Platform - Unused)": 182,
    "Blank (Independent CC - Unused)": 183,
    "Blank (Independent Starport - Unused)": 184,
    "Blank (Jump Gate - Unused)": 185,
    "Blank (Ruins - Unused)": 186,
    "Blank (Khayd. Crystal Form. - Unused)": 187,
    "Vespene Geyser": 188,
    "Warp Gate": 189,
    "Psi Disrupter": 190,
    "Blank (Zerg Marker)": 191,
    "Blank (Terran Marker)": 192,
    "Blank (Protoss Marker)": 193,
    "Zerg Beacon": 194,
    "Terran Beacon": 195,
    "Protoss Beacon": 196,
    "Zerg Flag Beacon": 197,
    "Terran Flag Beacon": 198,
    "Protoss Flag Beacon": 199,
    "Power Generator": 200,
    "Overmind Cocoon": 201,
    "Blank (Dark Swarm)": 202,
    "Blank (Floor Missile Trap)": 203,
    "Blank (Floor Hatch - Unused)": 204,
    "Blank (Left Upper Level Door)": 205,
    "Blank (Right Upper Level Door)": 206,
    "Blank (Left Pit Door)": 207,
    "Blank (Right Pit Door)": 208,
    "Blank (Floor Gun Trap)": 209,
    "Blank (Left Wall Missile Trap)": 210,
    "Blank (Left Wall Flame Trap)": 211,
    "Infested Mine (Unused)": 212,
    "Blank (Right Wall Flame Trap)": 213,
    "Start Location": 214,
    "Flag": 215,
    "Young Chrysalis": 216,
    "Psi Emitter": 217,
    "Data Disc": 218,
    "Khaydarin Crystal": 219,
    "Blank (Mineral Chunk Type 1)": 220,
    "Blank (Mineral Chunk Type 2)": 221,
    "Blank (Protoss Vespene Orb Type 1)": 222,
    "Blank (Protoss Vespene Orb Type 2)": 223,
    "Blank (Zerg Vespene Sac Type 1)": 224,
    "Blank (Zerg Vespene Sac Type 2)": 225,
    "Blank (Terran Vespene Tank Type 1)": 226,
    "Blank (Terran Vespene Tank Type 2)": 227,
    "Move": 228,
    "Stop": 229,
    "Attack": 230,
    "Gather": 231,
    "Repair": 232,
    "Return Resources": 233,
    "Terran Basic Buildings": 234,
    "Terran Advanced Buildings": 235,
    "Cancel": 236,
    "Use Stimpack": 237,
    "U-238 Shells": 238,
    "Burst Lasers (Unused)": 239,
    "Lockdown": 240,
    "EMP Shockwave": 241,
    "Irradiate": 242,
    "Use Spider Mines": 243,
    "Afterburners (Unused Terran Upgrade)": 244,
    "Siege Mode": 245,
    "Tank Mode": 246,
    "Defensive Matrix": 247,
    "Titan Reactor": 248,
    "Ocular Implants": 249,
    "Scanner Sweep": 250,
    "Yamato Gun": 251,
    "Cloak": 252,
    "Decloak": 253,
    "Patrol": 254,
    "Hold Position": 255,
    "Moebius Reactor": 256,
    "Zerg Basic Buildings": 257,
    "Zerg Advanced Buildings": 258,
    "Burrow": 259,
    "Unburrow": 260,
    "Ventral Sacs": 261,
    "Antennae": 262,
    "Metabolic Boost": 263,
    "Adrenal Glands": 264,
    "Plague": 265,
    "Muscular Augments": 266,
    "Ensnare": 267,
    "Grooved Spines": 268,
    "Roar (Unused Zerg Upgrade)": 269,
    "Dark Swarm": 270,
    "Parasite": 271,
    "Protoss Basic Buildings": 272,
    "Protoss Advanced Buildings": 273,
    "Mind Control (SC Beta - Unused)": 274,
    "Psionic Storm": 275,
    "Gravitic Boosters": 276,
    "Hallucination": 277,
    "Stasis Field": 278,
    "Blank": 279,
    "Recall": 280,
    "Singularity Charge": 281,
    "Lift off": 282,
    "Land": 283,
    "Apollo Reactor": 284,
    "Colossus Reactor": 285,
    "Set Rally Point": 286,
    "Ion Thrusters": 287,
    "Infantry Weapons": 288,
    "Vehicle Weapons": 289,
    "Ship Weapons": 290,
    "Ship Plating": 291,
    "Infantry Armor": 292,
    "Vehicle Armor": 293,
    "Gamete Meiosis": 294,
    "Metasynaptic Node": 295,
    "Pneumatized Caparace": 296,
    "Zerg Caparace": 297,
    "Flyer Caparace": 298,
    "Melee Attacks": 299,
    "Missile Attacks": 300,
    "Flyer Attacks": 301,
    "Consume": 302,
    "Ground Armor": 303,
    "Air Plating": 304,
    "Ground Weapons": 305,
    "Air Weapons": 306,
    "Leg Enhancements": 307,
    "Recharge Shields": 308,
    "Load (into Transport)": 309,
    "Plasma Shields": 310,
    "Nuclear Strike": 311,
    "Unload All (from Transport/Bunker)": 312,
    "Infest Command Center": 313,
    "Scarab Damage": 314,
    "Reaver Capacity": 315,
    "Gravitic Drive": 316,
    "Sensor Array": 317,
    "Khaydarin Amulet": 318,
    "Apial Sensors": 319,
    "Gravitic Thrusters": 320,
    "Carrier Capacity": 321,
    "Khaydarin Core": 322,
    "Gauss Rifle": 323,
    "C-10 Canister Rifle": 324,
    "Fragmentation Grenade": 325,
    "Twin Autocannons": 326,
    "Hellfire Missile Pack": 327,
    "Arclite Cannon": 328,
    "Fusion Cutter": 329,
    "Fusion Cutter (Harvest)": 330,
    "Gemini Missiles": 331,
    "Burst Lasers": 332,
    "ATS Laser Battery": 333,
    "ATA Laser Battery": 334,
    "Flame Thrower": 335,
    "Arclite Shock Cannon": 336,
    "Longbolt Missile": 337,
    "Claws": 338,
    "Needle Spines": 339,
    "Kaiser Blades": 340,
    "Toxic Spores": 341,
    "Spines": 342,
    "Flyer Attack": 343,
    "Acid Spore": 344,
    "Glave Wurm": 345,
    "Venom (Unused Zerg Weapon)": 346,
    "Seeker Spores": 347,
    "Subterranean Tentacle": 348,
    "Suicide (Infested Terran)": 349,
    "Suicide (Scourge)": 350,
    "Particle Beam": 351,
    "Particle Beam (Harvest)": 352,
    "Psi/Warp Blades": 353,
    "Phase Disruptor": 354,
    "Psi Assault": 355,
    "Psionic Shockwave": 356,
    "Radioactive (Unused)": 357,
    "Dual Photon Blasters": 358,
    "Anti-matter Missiles": 359,
    "Phase Disruptor Cannon": 360,
    "Pulse Cannon": 361,
    "STS/STA Photon Cannon": 362,
    "Radioactive (Unused2)": 363,
    "Spider Mine": 364,
    "Heal": 365,
    "Restoration": 366,
    "Restoration2": 367,
    "Disruption Web": 368,
    "Disruption Web2": 369,
    "Unknown371": 370,
    "Mind Control": 371,
    "Feedback": 372,
    "Optical Flare": 373,
    "Afterburners ON (Unused)": 374,
    "Afterburners OFF (Unused)": 375,
    "Lurker Aspect": 376,
    "Unknown378": 377,
    "Anabolic Synthesis": 378,
    "Chitinous Plating": 379,
    "Charon Boosters": 380,
    "Maelstrom": 381,
    "Subterranean Spines": 382,
    "Argus Jewel": 383,
    "Caduceus Reactor": 384,
    "Argus Talisman": 385,
    "Play (Replay)": 386,
    "Pause (Replay)": 387,
    "Speed Up (Replay)": 388,
    "Slow Down (Replay)": 389,
}

DefaultIcon: TypeAlias = Literal[
    "Marine",
    "Ghost",
    "Vulture",
    "Goliath",
    "Blank (Goliath Turret)",
    "Siege Tank (Tank Mode)",
    "Blank (Tank Turret)",
    "SCV",
    "Wraith",
    "Science Vessel",
    "Gui Montag",
    "Dropship",
    "Battlecruiser",
    "Vulture Spider Mine",
    "Nuclear Missile",
    "Civilian",
    "Sarah Kerrigan",
    "Alan Schezar",
    "Blank (Alan Turret)",
    "Jim Raynor (Vulture)",
    "Jim Raynor (Marine)",
    "Tom Kazansky",
    "Magellan",
    "Edmund Duke (Siege Tank)",
    "Blank (Duke Turret)",
    "Edmund Duke (Siege Mode)",
    "Blank (Siege Duke Turret)",
    "Blank (Arcturus Mengsk)",
    "Hyperion",
    "Norad II (Battlecruiser)",
    "Terran Siege Tank (Siege Mode)",
    "Blank (Siege Tank Turret)",
    "Firebat",
    "Marine (Scanner Sweep)",
    "Medic",
    "Larva",
    "Radioactive (Zerg Egg)",
    "Zergling",
    "Hydralisk",
    "Ultralisk",
    "Broodling",
    "Drone",
    "Overlord",
    "Mutalisk",
    "Guardian",
    "Queen",
    "Defiler",
    "Scourge",
    "Torrarsque",
    "Matriarch",
    "Infested Terran",
    "Infested Kerrigan",
    "Unclean One",
    "Hunter Killer",
    "Devouring One",
    "Kukulza (Mutalisk)",
    "Kukulza (Guardian)",
    "Yggdrasill",
    "Valkyrie",
    "Mutalisk/Guardian Cocoon",
    "Corsair",
    "Dark Templar (Unit)",
    "Devourer",
    "Dark Archon",
    "Probe",
    "Zealot",
    "Dragoon",
    "High Templar",
    "Archon",
    "Shuttle",
    "Scout",
    "Arbiter",
    "Carrier",
    "Interceptor",
    "Dark Templar (Hero)",
    "Zeratul",
    "Tassadar/Zeratul",
    "Fenix (Zealot)",
    "Fenix (Dragoon)",
    "Tassadar",
    "Mojo",
    "Warbringer",
    "Gantrithor",
    "Reaver",
    "Observer",
    "Scarab",
    "Danimoth",
    "Blank (Aldaris)",
    "Artanis",
    "Rhynadon",
    "Bengalaas",
    "Lurker (Cargo Ship - Unused)",
    "Mercenary Gunship (Unused)",
    "Scantid",
    "Kakaru",
    "Ragnasaur",
    "Ursadon",
    "Blank (Zerg Lurker Egg)",
    "Blank (Raszagal)",
    "Samir Duran",
    "Alexei Stukov",
    "Map Revealer",
    "Blank (Gerard DuGalle)",
    "Lurker",
    "Infested Duran",
    "Blank (Disruption Field)",
    "Command Center",
    "Comsat Station",
    "Nuclear Silo",
    "Supply Depot",
    "Refinery",
    "Barracks",
    "Academy",
    "Factory",
    "Starport",
    "Control Tower",
    "Science Facility",
    "Covert Ops",
    "Physics Lab",
    "Blank (Starbase - Unused)",
    "Machine Shop",
    "Repair Bay (Unused)",
    "Engineering Bay",
    "Armory",
    "Missile Tower",
    "Bunker",
    "Crashed Norad II",
    "Ion Cannon",
    "Uraj",
    "Khalis",
    "Infested Command Center",
    "Hatchery",
    "Lair",
    "Hive",
    "Nydus Canal",
    "Hydralisk Den",
    "Defiler Mound",
    "Greater Spire",
    "Queen's Nest",
    "Evolution Chamber",
    "Ultralisk Cavern",
    "Spire",
    "Spawning Pool",
    "Creep Colony",
    "Spore Colony",
    "Radioactive (Zerg Bldg1 - Unused)",
    "Sunken Colony",
    "Overmind (Without Shell)",
    "Overmind (With Shell)",
    "Extractor",
    "Mature Chrysalis",
    "Cerebrate",
    "Cerebrate Daggoth",
    "Blank (Zerg Bldg2 - Unused)",
    "Nexus",
    "Robotics Facility",
    "Pylon",
    "Assimilator",
    "Blank (Protoss Bldg1 - Unused)",
    "Observatory",
    "Gateway",
    "Blank (Protoss Bldg2 - Unused)",
    "Photon Cannon",
    "Citadel of Adun",
    "Cybernetics Core",
    "Templar Archives",
    "Forge",
    "Stargate",
    "Stasis Cell/Prison",
    "Fleet Beacon",
    "Arbiter Tribunal",
    "Robotics Support Bay",
    "Shield Battery",
    "Khaydarin Crystal Formation",
    "Protoss Temple",
    "Xel'Naga Temple",
    "Mineral Cluster (Type 1)",
    "Mineral Cluster (Type 2)",
    "Mineral Cluster (Type 3)",
    "Blank (Cave - Unused)",
    "Blank (Cave-in - Unused)",
    "Blank (Cantina - Unused)",
    "Blank (Mining Platform - Unused)",
    "Blank (Independent CC - Unused)",
    "Blank (Independent Starport - Unused)",
    "Blank (Jump Gate - Unused)",
    "Blank (Ruins - Unused)",
    "Blank (Khayd. Crystal Form. - Unused)",
    "Vespene Geyser",
    "Warp Gate",
    "Psi Disrupter",
    "Blank (Zerg Marker)",
    "Blank (Terran Marker)",
    "Blank (Protoss Marker)",
    "Zerg Beacon",
    "Terran Beacon",
    "Protoss Beacon",
    "Zerg Flag Beacon",
    "Terran Flag Beacon",
    "Protoss Flag Beacon",
    "Power Generator",
    "Overmind Cocoon",
    "Blank (Dark Swarm)",
    "Blank (Floor Missile Trap)",
    "Blank (Floor Hatch - Unused)",
    "Blank (Left Upper Level Door)",
    "Blank (Right Upper Level Door)",
    "Blank (Left Pit Door)",
    "Blank (Right Pit Door)",
    "Blank (Floor Gun Trap)",
    "Blank (Left Wall Missile Trap)",
    "Blank (Left Wall Flame Trap)",
    "Infested Mine (Unused)",
    "Blank (Right Wall Flame Trap)",
    "Start Location",
    "Flag",
    "Young Chrysalis",
    "Psi Emitter",
    "Data Disc",
    "Khaydarin Crystal",
    "Blank (Mineral Chunk Type 1)",
    "Blank (Mineral Chunk Type 2)",
    "Blank (Protoss Vespene Orb Type 1)",
    "Blank (Protoss Vespene Orb Type 2)",
    "Blank (Zerg Vespene Sac Type 1)",
    "Blank (Zerg Vespene Sac Type 2)",
    "Blank (Terran Vespene Tank Type 1)",
    "Blank (Terran Vespene Tank Type 2)",
    "Move",
    "Stop",
    "Attack",
    "Gather",
    "Repair",
    "Return Resources",
    "Terran Basic Buildings",
    "Terran Advanced Buildings",
    "Cancel",
    "Use Stimpack",
    "U-238 Shells",
    "Burst Lasers (Unused)",
    "Lockdown",
    "EMP Shockwave",
    "Irradiate",
    "Use Spider Mines",
    "Afterburners (Unused Terran Upgrade)",
    "Siege Mode",
    "Tank Mode",
    "Defensive Matrix",
    "Titan Reactor",
    "Ocular Implants",
    "Scanner Sweep",
    "Yamato Gun",
    "Cloak",
    "Decloak",
    "Patrol",
    "Hold Position",
    "Moebius Reactor",
    "Zerg Basic Buildings",
    "Zerg Advanced Buildings",
    "Burrow",
    "Unburrow",
    "Ventral Sacs",
    "Antennae",
    "Metabolic Boost",
    "Adrenal Glands",
    "Plague",
    "Muscular Augments",
    "Ensnare",
    "Grooved Spines",
    "Roar (Unused Zerg Upgrade)",
    "Dark Swarm",
    "Parasite",
    "Protoss Basic Buildings",
    "Protoss Advanced Buildings",
    "Mind Control (SC Beta - Unused)",
    "Psionic Storm",
    "Gravitic Boosters",
    "Hallucination",
    "Stasis Field",
    "Blank",
    "Recall",
    "Singularity Charge",
    "Lift off",
    "Land",
    "Apollo Reactor",
    "Colossus Reactor",
    "Set Rally Point",
    "Ion Thrusters",
    "Infantry Weapons",
    "Vehicle Weapons",
    "Ship Weapons",
    "Ship Plating",
    "Infantry Armor",
    "Vehicle Armor",
    "Gamete Meiosis",
    "Metasynaptic Node",
    "Pneumatized Caparace",
    "Zerg Caparace",
    "Flyer Caparace",
    "Melee Attacks",
    "Missile Attacks",
    "Flyer Attacks",
    "Consume",
    "Ground Armor",
    "Air Plating",
    "Ground Weapons",
    "Air Weapons",
    "Leg Enhancements",
    "Recharge Shields",
    "Load (into Transport)",
    "Plasma Shields",
    "Nuclear Strike",
    "Unload All (from Transport/Bunker)",
    "Infest Command Center",
    "Scarab Damage",
    "Reaver Capacity",
    "Gravitic Drive",
    "Sensor Array",
    "Khaydarin Amulet",
    "Apial Sensors",
    "Gravitic Thrusters",
    "Carrier Capacity",
    "Khaydarin Core",
    "Gauss Rifle",
    "C-10 Canister Rifle",
    "Fragmentation Grenade",
    "Twin Autocannons",
    "Hellfire Missile Pack",
    "Arclite Cannon",
    "Fusion Cutter",
    "Fusion Cutter (Harvest)",
    "Gemini Missiles",
    "Burst Lasers",
    "ATS Laser Battery",
    "ATA Laser Battery",
    "Flame Thrower",
    "Arclite Shock Cannon",
    "Longbolt Missile",
    "Claws",
    "Needle Spines",
    "Kaiser Blades",
    "Toxic Spores",
    "Spines",
    "Flyer Attack",
    "Acid Spore",
    "Glave Wurm",
    "Venom (Unused Zerg Weapon)",
    "Seeker Spores",
    "Subterranean Tentacle",
    "Suicide (Infested Terran)",
    "Suicide (Scourge)",
    "Particle Beam",
    "Particle Beam (Harvest)",
    "Psi/Warp Blades",
    "Phase Disruptor",
    "Psi Assault",
    "Psionic Shockwave",
    "Radioactive (Unused)",
    "Dual Photon Blasters",
    "Anti-matter Missiles",
    "Phase Disruptor Cannon",
    "Pulse Cannon",
    "STS/STA Photon Cannon",
    "Radioactive (Unused2)",
    "Spider Mine",
    "Heal",
    "Restoration",
    "Restoration2",
    "Disruption Web",
    "Disruption Web2",
    "Unknown371",
    "Mind Control",
    "Feedback",
    "Optical Flare",
    "Afterburners ON (Unused)",
    "Afterburners OFF (Unused)",
    "Lurker Aspect",
    "Unknown378",
    "Anabolic Synthesis",
    "Chitinous Plating",
    "Charon Boosters",
    "Maelstrom",
    "Subterranean Spines",
    "Argus Jewel",
    "Caduceus Reactor",
    "Argus Talisman",
    "Play (Replay)",
    "Pause (Replay)",
    "Speed Up (Replay)",
    "Slow Down (Replay)",
]
