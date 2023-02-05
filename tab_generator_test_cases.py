import tab_generator

# intro riff for ぶっ生き返
PROGRESSION =  ["G", "F", "G", "G", "G",
                "G", "F", "G", "G", "G",
                "G", "F", "G", "G", "G",
                "G", "F", "G", "G", "G",
                "G", "F", "G", "G", "G",
                "G", "F", "G", "G", "G",
                "G", "F", "G", "G", "G", "Ab"]

# test for circle of 5ths
# correct output should be 
# [ D, C, D, D, D,
#   D, C, D, D, D,
#   D, C, D, D, D,
#   D, C, D, D, D,
#   D, C, D, D, D, Eb  ]
fifths = []
for note in PROGRESSION:
    fifths.append(tab_generator.get_perfect_fifth(note))
print(f"Fifths: {fifths}")

# test for perfect fourths
# correct output should be
# [ C, Bb, C, C, C,
#   C, Bb, C, C, C,
#   C, Bb, C, C, C,
#   C, Bb, C, C, C,
#   C, Bb, C, C, C, Db ]
fourths = []
for note in PROGRESSION:
    fourths.append(tab_generator.get_perfect_fourth(note))
print(f"Fourths: {fourths}")