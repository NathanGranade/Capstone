import tab_generator
import os
import platform

def get_terminal_dimensions():
    return os.get_terminal_size()

def get_terminal_columns():
    return os.get_terminal_size().columns

def get_terminal_rows():
    return os.get_terminal_size().lines

ROWS = get_terminal_rows()
COLUMNS = get_terminal_columns()

# PRINT TAB MAP

keys = tab_generator.TAB_MAP.keys()
for key in keys:
    print(key, end = ": ")
    positions = tab_generator.TAB_MAP[key]
    for position in positions:
        print(position, end = " ")
    print()

input("\nTest Complete: print tab map\nPress ENTER to start next test.")
os.system("cls")

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

input("\nTest Complete: get perfect fifths for intro to ぶっ生き返す\nPress ENTER to start next test.")
os.system("cls" if platform.system() == "Windows" else "clear")

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

input("Test Complete: get perfect fourths for intro to ぶっ生き返す\nPress ENTER to start next test.")
os.system("cls")

# test for getting the positions on the fretboard, given the notes to a song
# pig destroyer - naked trees intro
notes = ["E", "F#", "G", "A",
         "E", "F#", "G", "A",
         "E", "F#", "G", "A",
         "E", "F#", "G", "A",
         "E", 
         "E", "E", "E", "E", "E",
         "A#", "A", "A#", "A", "G",
         "E", "E", "E", "E", "E",
         "A#", "A", "A#", "A", "G",
         "E", "E", "E", "E", "E",
         "A#", "A", "A#", "A", "G",
         "E", "E", "E", "E", "E",
         "A#", "A", "A#", "A", "G",
         "E", "E", "E", "E", "E",
         "A#", "A", "A#", "A", "G",
         "E", "E", "E", "E", "E",
         "A#", "A", "A#", "A", "G",
         "E", "F#", "G", "A",
         "E", "F#", "G", "A",
         "E", "F#", "G", "A",
         "E", "F#", "G", "A"
]
positions = []
for note in notes:
    note_instance = tab_generator.Note(note, 0)
    options = tab_generator.TAB_MAP[str(note_instance)]
    easiest = options[0]
    positions.append(easiest)
tablature = {6 : [],
5 : [],
4 : [],
3 : [],
2 : [],
1 : []
}

for position in positions:
    tablature[position.string].append(position.fret)
for key in tablature.keys():
    print(f"{key}|-", end = "")
    for fret in tablature[key]:
        print(f"{fret}", end = "-")
    print()
    
# tests for generating the right powerchord
f_power_chord_tabs = tab_generator.get_power_chord(tab_generator.FretboardPosition(6, 1))
f_tritone_tabs = tab_generator.get_tritone_chord(tab_generator.FretboardPosition(6, 1))
for position in f_power_chord_tabs:
    print(position)
for position in f_tritone_tabs:
    print(position)