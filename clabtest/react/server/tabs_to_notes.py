from sys import argv
from itertools import chain

class Chord:
    def __init__(self, notes = []):
        self.notes = notes
        self.type = "unknown"

    def add_note(self, note: str):
        self.notes.append(note)

    def __str__(self):
        return(str(self.notes))

class FretboardPosition:
    def __init__(self, string: int, fret: int):
        self.string = string
        self.fret = fret
    
    def __str__(self):
        return(f"(String {self.string}, fret {self.fret})")
    
    def __eq__(self, other):
        if other == None:
            return False
        
        if (self.string == other.string) and (self.fret == other.fret):
            return True
        else:
            return False

class Term:
    def __init__(self, sequence_number, chord):
        self.sequence_number = sequence_number
        # chord is an instance of the Chord class
        self.chord = chord

    def __str__(self):
        return(f"{self.sequence_number},{self.string},{self.fret}")
    
    def __eq__(self, other):
        if not type(other) == type(self):
            return False

INVERTED_TAB_MAP = {		
        "(String 7, fret -2)" : "(A, 1)",
		"(String 7, fret -1)" : "(A#, 1)",
		"(String 7, fret 0)" : "(B, 1)",
		"(String 6, fret -4)" : "(C, 2)",
		"(String 7, fret 1)" : "(C, 2)",
		"(String 6, fret -3)" : "(Db, 2)",
		"(String 7, fret 2)" : "(Db, 2)",
		"(String 6, fret -2)" : "(D, 2)",
		"(String 7, fret 3)" : "(D, 2)",
		"(String 6, fret -1)" : "(Eb, 2)",
		"(String 7, fret 4)" : "(Eb, 2)",
		"(String 6, fret 0)" : "(E, 2)",
		"(String 7, fret 5)" : "(E, 2)",
		"(String 6, fret 1)" : "(F, 2)",
		"(String 6, fret 2)" : "(Gb, 2)",
		"(String 6, fret 3)" : "(G, 2)",
		"(String 6, fret 4)" : "(Ab, 2)",
		"(String 6, fret 5)" : "(A, 2)",
		"(String 5, fret 0)" : "(A, 2)",
		"(String 6, fret 6)" : "(Bb, 2)",
		"(String 5, fret 1)" : "(Bb, 2)",
		"(String 6, fret 7)" : "(B, 2)",
		"(String 5, fret 2)" : "(B, 2)",
		"(String 6, fret 8)" : "(C, 3)",
		"(String 5, fret 3)" : "(C, 3)",
		"(String 6, fret 9)" : "(Db, 3)",
		"(String 5, fret 4)" : "(Db, 3)",
		"(String 6, fret 10)" : "(D, 3)",
		"(String 5, fret 5)" : "(D, 3)",
		"(String 4, fret 0)" : "(D, 3)",
		"(String 6, fret 11)" : "(Eb, 3)",
		"(String 5, fret 6)" : "(Eb, 3)",
		"(String 4, fret 1)" : "(Eb, 3)",
		"(String 5, fret 7)" : "(E, 3)",
		"(String 6, fret 12)" : "(E, 3)",
		"(String 4, fret 2)" : "(E, 3)",
		"(String 6, fret 13)" : "(F, 3)",
		"(String 5, fret 8)" : "(F, 3)",
		"(String 4, fret 3)" : "(F, 3)",
		"(String 6, fret 14)" : "(Gb, 3)",
		"(String 5, fret 9)" : "(Gb, 3)",
		"(String 4, fret 4)" : "(Gb, 3)",
		"(String 6, fret 15)" : "(G, 3)",
		"(String 5, fret 10)" : "(G, 3)",
		"(String 4, fret 5)" : "(G, 3)",
		"(String 3, fret 0)" : "(G, 3)",
		"(String 6, fret 16)" : "(Ab, 3)",
		"(String 5, fret 11)" : "(Ab, 3)",
		"(String 4, fret 6)" : "(Ab, 3)",
		"(String 3, fret 1)" : "(Ab, 3)",
		"(String 6, fret 17)" : "(A, 3)",
		"(String 5, fret 12)" : "(A, 3)",
		"(String 4, fret 7)" : "(A, 3)",
		"(String 3, fret 2)" : "(A, 3)",
		"(String 6, fret 18)" : "(Bb, 3)",
		"(String 5, fret 13)" : "(Bb, 3)",
		"(String 4, fret 8)" : "(Bb, 3)",
		"(String 3, fret 3)" : "(Bb, 3)",
		"(String 6, fret 19)" : "(B, 3)",
		"(String 5, fret 14)" : "(B, 3)",
		"(String 4, fret 9)" : "(B, 3)",
		"(String 3, fret 4)" : "(B, 3)",
		"(String 2, fret 0)" : "(B, 3)",
		"(String 6, fret 20)" : "(C, 4)",
		"(String 5, fret 15)" : "(C, 4)",
		"(String 4, fret 10)" : "(C, 4)",
		"(String 3, fret 5)" : "(C, 4)",
		"(String 2, fret 1)" : "(C, 4)",
		"(String 6, fret 21)" : "(Db, 4)",
		"(String 5, fret 16)" : "(Db, 4)",
		"(String 4, fret 11)" : "(Db, 4)",
		"(String 3, fret 6)" : "(Db, 4)",
		"(String 2, fret 2)" : "(Db, 4)",
		"(String 6, fret 22)" : "(D, 4)",
		"(String 5, fret 17)" : "(D, 4)",
		"(String 4, fret 12)" : "(D, 4)",
		"(String 3, fret 7)" : "(D, 4)",
		"(String 2, fret 3)" : "(D, 4)",
		"(String 6, fret 23)" : "(Eb, 4)",
		"(String 5, fret 18)" : "(Eb, 4)",
		"(String 4, fret 13)" : "(Eb, 4)",
		"(String 3, fret 8)" : "(Eb, 4)",
		"(String 2, fret 4)" : "(Eb, 4)",
		"(String 6, fret 24)" : "(E, 4)",
		"(String 5, fret 19)" : "(E, 4)",
		"(String 4, fret 14)" : "(E, 4)",
		"(String 3, fret 9)" : "(E, 4)",
		"(String 2, fret 5)" : "(E, 4)",
		"(String 1, fret 0)" : "(E, 4)",
		"(String 5, fret 20)" : "(F, 4)",
		"(String 4, fret 15)" : "(F, 4)",
		"(String 3, fret 10)" : "(F, 4)",
		"(String 2, fret 6)" : "(F, 4)",
		"(String 1, fret 1)" : "(F, 4)",
		"(String 5, fret 21)" : "(Gb, 4)",
		"(String 4, fret 16)" : "(Gb, 4)",
		"(String 3, fret 11)" : "(Gb, 4)",
		"(String 2, fret 7)" : "(Gb, 4)",
		"(String 1, fret 2)" : "(Gb, 4)",
		"(String 5, fret 22)" : "(G, 4)",
		"(String 4, fret 17)" : "(G, 4)",
		"(String 3, fret 12)" : "(G, 4)",
		"(String 2, fret 8)" : "(G, 4)",
		"(String 1, fret 3)" : "(G, 4)",
		"(String 5, fret 23)" : "(Ab, 4)",
		"(String 4, fret 18)" : "(Ab, 4)",
		"(String 3, fret 13)" : "(Ab, 4)",
		"(String 2, fret 9)" : "(Ab, 4)",
		"(String 1, fret 4)" : "(Ab, 4)",
		"(String 5, fret 24)" : "(A, 4)",
		"(String 4, fret 19)" : "(A, 4)",
		"(String 3, fret 14)" : "(A, 4)",
		"(String 2, fret 10)" : "(A, 4)",
		"(String 1, fret 5)" : "(A, 4)",
		"(String 4, fret 20)" : "(Bb, 4)",
		"(String 3, fret 15)" : "(Bb, 4)",
		"(String 2, fret 11)" : "(Bb, 4)",
		"(String 1, fret 6)" : "(Bb, 4)",
		"(String 4, fret 21)" : "(B, 4)",
		"(String 3, fret 16)" : "(B, 4)",
		"(String 2, fret 12)" : "(B, 4)",
		"(String 1, fret 7)" : "(B, 4)",
		"(String 4, fret 22)" : "(C, 5)",
		"(String 3, fret 17)" : "(C, 5)",
		"(String 2, fret 13)" : "(C, 5)",
		"(String 1, fret 8)" : "(C, 5)",
		"(String 4, fret 23)" : "(Db, 5)",
		"(String 3, fret 18)" : "(Db, 5)",
		"(String 2, fret 14)" : "(Db, 5)",
		"(String 1, fret 9)" : "(Db, 5)",
		"(String 4, fret 24)" : "(D, 5)",
		"(String 3, fret 19)" : "(D, 5)",
		"(String 2, fret 15)" : "(D, 5)",
		"(String 1, fret 10)" : "(D, 5)",
		"(String 3, fret 20)" : "(Eb, 5)",
		"(String 2, fret 16)" : "(Eb, 5)",
		"(String 1, fret 11)" : "(Eb, 5)",
		"(String 3, fret 21)" : "(E, 5)",
		"(String 2, fret 17)" : "(E, 5)",
		"(String 1, fret 12)" : "(E, 5)",
		"(String 3, fret 22)" : "(F, 5)",
		"(String 2, fret 18)" : "(F, 5)",
		"(String 1, fret 13)" : "(F, 5)",
		"(String 3, fret 23)" : "(Gb, 5)",
		"(String 2, fret 19)" : "(Gb, 5)",
		"(String 1, fret 14)" : "(Gb, 5)",
		"(String 3, fret 24)" : "(G, 5)",
		"(String 2, fret 20)" : "(G, 5)",
		"(String 1, fret 15)" : "(G, 5)",
		"(String 2, fret 21)" : "(Ab, 5)",
		"(String 1, fret 16)" : "(Ab, 5)",
		"(String 2, fret 22)" : "(A, 5)",
		"(String 1, fret 17)" : "(A, 5)",
		"(String 2, fret 23)" : "(Bb, 5)",
		"(String 1, fret 18)" : "(Bb, 5)",
		"(String 2, fret 24)" : "(B, 5)",
		"(String 1, fret 19)" : "(B, 5)",
		"(String 1, fret 20)" : "(C, 6)",
		"(String 1, fret 21)" : "(Db, 6)",
		"(String 1, fret 22)" : "(D, 6)",
		"(String 1, fret 23)" : "(Eb, 6)",
		"(String 1, fret 24)" : "(E, 6)"
}

def get_file_contents(file_name):
    """
    opens a file and returns a list of strings where each string
    is a line in the file

    keyword arguments
    -----------------
    file_name -- string corresponding to the file to be read
    """
    file_instance = open(file_name, "r")
    file_contents = file_instance.readlines()
    file_instance.close()
    return(file_contents)

def separate_open_notes_from_fret_positions(file_contents):
    """
    returns a list of lists where each list is the result of splitting
    a string by the | character. For a tab, this means that index 0 is
    the open note corresponding to that string and index 1 is the string
    representation of the frets to be played on that string

    keyword arguments
    -----------------
    file_contents -- a list of strings
    """
    modified_list = []
    
    # adds contents of file_contents to modified_list as lists, 
    # where the 1st element of any given list is always the note
    # an openly-played guitar string corresponds to, and the 2nd element
    # of any list is always the string of frets to be played on that
    # guitar string.
    for x in range(len(file_contents)):
        # ignore completely blank lines
        if file_contents[x] == "\n":
            continue
        
        # tabs always say the note name, then have a | character
        # followed by the frets to be played. 
        # therefore, if you split by the | character, index 0
        # is the note corresponding to that string when played open (no frets)
        # and index 1 is the string representation of the frets to be played
        split_contents = file_contents[x].split("|")
        modified_list.append(split_contents)
    return(modified_list)

def get_unprocessed_tab_dictionary(modified_list):
    """
    returns a dictionary that maps a note (corresponding to the open strings on
    a guitar) to a a string of frets to be played on that string.
    """
    unprocessed_tab_dictionary = dict()

    # 1. get the open-string notes and frets to be played on said string
    # from the modified_list
    # 2. then map them in the dictionary
    string_number = 1
    for x in range(len(modified_list)):
        # index 0 is always the open-string note in modified_list
        # (see separate_open_notes_from_fret_positions() method)
        open_note = modified_list[x][0]
        
        # need to couple the open note with the string number, because it is possible to have a tuning like
        # DADGBE -- in this case, D will be added twice to the keys of the dictionary (no bueno)
        if string_number > 6:                                    # |
            modulus = string_number % 6                          # | this prevents strings from going 0 to 7. Keeps them
            string_number = 6 if modulus == 0 else modulus       # | in range [0, 6]

        open_note = f"{open_note}, {string_number}"
        string_number += 1

        # index 1 is always the string representation of frets to be played
        frets = modified_list[x][1]
        
        # if an open-string note has not yet been mapped the to
        # the dictionary, map it
        if not open_note in unprocessed_tab_dictionary.keys():
            unprocessed_tab_dictionary[open_note] = frets
        # otherwise, add to the frets being tracked by the dictionary
        else: 
            unprocessed_tab_dictionary[open_note] += frets
    return(unprocessed_tab_dictionary)

def get_tuning(tab_dictionary):
    string_open_notes = tab_dictionary.keys()
    tuning = dict()
    for element in string_open_notes:
        # the second [1] is to remove the white space that leads before the
        # number after doing the split (I have no idea why there is a space before the number)
        string_number = int(element.split(",")[1][1])
        string_note = element.split(",")[0]
        tuning[string_number] = string_note
    return(tuning)

def iterate_over_tab_dictionary_vertically(tab_dictionary):
    column = 0
    tuning = get_tuning(tab_dictionary)
    print(tuning)
    example_string = f"{tuning[1]}, 1"
    stopping_point = len(tab_dictionary[example_string])
    print(f"Stopping point is {stopping_point}")
    chords = []
    while column < stopping_point:
        # create a list of notes to put into a chord instance
        # NOTE: you cannot just create a Chord instance and then
        # use the add_note() method, and then append the chord
        # instance to the chords list, because for whatever reason
        # the chord instance will be the same one used previously,
        # resulting in a monstrous chord with 70+ notes somehow
        # being played simultaneously.
        positions = []
        
        # go through every string
        for string in tab_dictionary.keys():
            print(f"string is: {string}")
            value = tab_dictionary[string][column]
            if value in ["p", "/", "h", "-", "\n"]:
                print(f"detected \"{value}\" -- ignoring string {string} for column {column}")
                continue
            string_number = int(string.split(",")[1])
            positions.append(FretboardPosition(string_number, int(value)))
            print(f"Created fretboardPosition {str(FretboardPosition(string_number, int(value)))}")
            print(f"added value {value} to chord {positions}")
        
        if len(positions) > 0:
            notes = [INVERTED_TAB_MAP[str(position)] for position in positions]
            chords.append(Chord(notes))
        
        column += 1
        print(f"column is now {column}")
    return(chords)

if len(argv) < 2:
    exit()

file_contents = get_file_contents(argv[1])

preprocessed_file_contents = separate_open_notes_from_fret_positions(file_contents)

unprocessed_tab_dictionary = get_unprocessed_tab_dictionary(preprocessed_file_contents)

for key in unprocessed_tab_dictionary.keys():
    print(f"{key}: {unprocessed_tab_dictionary[key]}")

chords = iterate_over_tab_dictionary_vertically(unprocessed_tab_dictionary)

for chord in chords:
    print(f"{chord}\n\n")
