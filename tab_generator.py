WHOLE_STEPS = ["A", "B", "C", "D", "E", "F", "G"]

TUNINGS = {
        # NOTE: 7 and 8 string guitar tunings can be created by simply appending extended range to existing 6 string tuning; for example, B standard (7 string) = ["B"] + TUNINGS["E standard"] 

        # 6 String standard tunings
        "E standard": ["E", "A", "D", "G", "B", "E"],
        # Eb standard is the same as D# standard
        "Eb standard" : ["Eb", "Ab", "Db", "Gb", "Bb", "Eb"], 
        "D standard" : ["D", "G", "C", "F", "A", "D"],
        # C# standard is the same as Db standard
        "C# standard": ["C#", "F#", "B", "E", "G#", "C#"],
        "C standard" : ["C", "F", "A#", "D#", "G", "C"],
        "B standard" : ["B", "E", "A", "D", "G", "B"],
        "A standard" : ["A", "D", "G", "C", "E", "A"],
        
        # 6 string drop tunings
        "Drop D": ["D", "A", "D", "G", "B", "E"],
        "Drop C#": ["C#", "G#", "C#", "F#", "A#", "D#"],
        "Drop C": ["C", "G", "C", "F", "A", "D"],
        "Drop B": ["B", "F#", "B", "E", "G#", "C#"],
        "Drop A": ["A", "E", "A", "D", "G", "B"]
        }

class Note:
    def __init__(self, note: str, octave: int):
        self.note = note
        # E standard tuning is used as reference for octave = 0; therefore:
        # E, 0 -> open E (6th string)
        #   E, -1 open E on 8th string
        # A, 0 -> open A, or 5th fret of E
        # D, 0 -> open D (4th string)
        # G, 0 -> open G (3rd string)
        # B, 0 -> open B (2nd string)
        # E, 1 -> open E (1st string)
        self.octave = octave

    def one_step_down(self):
        if self.note in WHOLE_STEPS:
            index = WHOLE_STEPS.index(self.note)
            if index != 0:
                one_step_down_note = WHOLE_STEPS[index-1]
            else:
                one_step_down_note = WHOLE_STEPS[len(WHOLE_STEPS)-1]
            new_note = Note(one_step_down_note, self.octave)

class Chord:
    def __init__(self, notes: list):
        self.notes = notes


class PowerChord(Chord):
    def __init__(self, root):
        self.notes = [root]


class FretboardPosition:
    def __init__(self, string: int, fret: int):
        self.string = string
        self.fret = fret

# This is all the ways you can play any given note on a guitar's fretboard, under the presumption that you have a 6 string guitar with 24 frets.
# To handle other tunings, just transpose (see transpose function) from Standard E tuning.
# For example, D Standard is 1 whole step lower than E standard, so to transpose E → D, move DOWN each fretboard position by 2, except for where the fret is 0.
#                                                                   to transpose D → E, moe UP each fretboard position by 2, except for where the fret is 24.
TAB_MAP = {
        Note("E", 0) :  [FretboardPosition(6, 0)], 
        Note("F", 0) :  [FretboardPosition(6, 1)],
        Note("F#", 0) : [FretboardPosition(6, 2)],
        Note("Gb", 0) : [FretboardPosition(6, 2)],
        Note("G", 0) :  [FretboardPosition(6, 3)],
        Note("G#", 0) : [FretboardPosition(6, 4)],
        Note("Ab", 0) : [FretboardPosition(6, 4)],
        Note("A", 0) :  [FretboardPosition(6, 5), FretboardPosition(5, 0)],
        Note("A#", 0) : [FretboardPosition(6, 6), FretboardPosition(5, 1)],
        Note("Bb", 0) : [FretboardPosition(6, 6), FretboardPosition(5, 1)],
        Note("B", 0) :  [FretboardPosition(6, 7), FretboardPosition(5, 2)],
        Note("C", 0) :  [FretboardPosition(6, 8), FretboardPosition(5, 3)],
        Note("C#", 0) : [FretboardPosition(6, 9), FretboardPosition(5, 4)],
        Note("Db", 0) : [FretboardPosition(6, 9), FretboardPosition(5, 4)],
        Note("D", 0) :  [FretboardPosition(6, 10), FretboardPosition(5, 5), FretboardPosition(4, 0)],
        Note("D#", 0) : [FretboardPosition(6, 11), FretboardPosition(5, 6), FretboardPosition(4, 1)],
        Note("Eb", 0) : [FretboardPosition(6, 11), FretboardPosition(5, 6), FretboardPosition(4, 1)],
        
        
        # One octave up Low E String                A String                  D String                  G String                  B String                 High E String
        Note("E", 1) :  [FretboardPosition(6, 12), FretboardPosition(5, 7),  FretboardPosition(4, 2)],
        Note("F", 1) :  [FretboardPosition(6, 13), FretboardPosition(5, 8),  FretboardPosition(4, 3)],
        Note("F#", 1) : [FretboardPosition(6, 14), FretboardPosition(5, 9),  FretboardPosition(4, 4)],
        Note("Gb", 1) : [FretboardPosition(6, 14), FretboardPosition(5, 9),  FretboardPosition(4, 4)],
        Note("G", 1) :  [FretboardPosition(6, 15), FretboardPosition(5, 10), FretboardPosition(4, 5),  FretboardPosition(3, 0)], 
        Note("G#", 1) : [FretboardPosition(6, 16), FretboardPosition(5, 11), FretboardPosition(4, 6),  FretboardPosition(3, 1)],
        Note("Ab", 1) : [FretboardPosition(6, 16), FretboardPosition(5, 11), FretboardPosition(4, 6),  FretboardPosition(3, 1)],
        Note("A", 1) :  [FretboardPosition(6, 17), FretboardPosition(5, 12), FretboardPosition(4, 7),  FretboardPosition(3, 2)],
        Note("A#", 1):  [FretboardPosition(6, 18), FretboardPosition(5, 13), FretboardPosition(4, 8),  FretboardPosition(3, 3)],
        Note("Bb", 1):  [FretboardPosition(6, 18), FretboardPosition(5, 13), FretboardPosition(4, 8),  FretboardPosition(3, 3)],
        Note("B", 1) :  [FretboardPosition(6, 19), FretboardPosition(5, 14), FretboardPosition(4, 9),  FretboardPosition(3, 4), FretboardPosition(2, 0)],
        Note("C", 1) :  [FretboardPosition(6, 20), FretboardPosition(5, 15), FretboardPosition(4, 10), FretboardPosition(3, 5), FretboardPosition(2, 1)],
        Note("C#", 1) : [FretboardPosition(6, 21), FretboardPosition(5, 16), FretboardPosition(4, 11), FretboardPosition(3, 6), FretboardPosition(2, 2)],
        Note("Db", 1) : [FretboardPosition(6, 21), FretboardPosition(5, 16), FretboardPosition(4, 11), FretboardPosition(3, 6), FretboardPosition(2, 2)],
        Note("D", 1) :  [FretboardPosition(6, 22), FretboardPosition(5, 17), FretboardPosition(4, 12), FretboardPosition(3, 7), FretboardPosition(2, 3)],
        Note("D#", 1) : [FretboardPosition(6, 23), FretboardPosition(5, 18), FretboardPosition(4, 13), FretboardPosition(3, 8), FretboardPosition(2, 4)],
        Note("Eb", 1) : [FretboardPosition(6, 23), FretboardPosition(5, 18), FretboardPosition(4, 13), FretboardPosition(3, 8), FretboardPosition(2, 4)],
        
        # Two octaves up
        Note("E", 2) :  [FretboardPosition(6, 24), FretboardPosition(5, 19), FretboardPosition(4, 14), FretboardPosition(3, 9), FretboardPosition(2, 5), FretboardPosition(1, 0)],
        Note("F", 2) :  [                          FretboardPosition(5, 20), FretboardPosition(4, 15), FretboardPosition(3, 10), FretboardPosition(2, 6), FretboardPosition(1, 1)],
        Note("F#", 2) : [                          FretboardPosition(5, 21), FretboardPosition(4, 16), FretboardPosition(3, 11), FretboardPosition(2, 7), FretboardPosition(1, 2)],
        Note("Gb", 2) : [                          FretboardPosition(5, 21), FretboardPosition(4, 16), FretboardPosition(3, 11), FretboardPosition(2, 7), FretboardPosition(1, 2)],
        Note("G", 2) :  [                          FretboardPosition(5, 22), FretboardPosition(4, 17), FretboardPosition(3, 12), FretboardPosition(2, 8), FretboardPosition(1, 3)],
        Note("G#", 2) : [                          FretboardPosition(5, 23), FretboardPosition(4, 18), FretboardPosition(3, 13), FretboardPosition(2, 9), FretboardPosition(1, 4)],
        Note("Ab", 2) : [                          FretboardPosition(5, 23), FretboardPosition(4, 18), FretboardPosition(3, 13), FretboardPosition(2, 9), FretboardPosition(1, 4)],
        Note("A", 2) :  [                          FretboardPosition(5, 24), FretboardPosition(4, 19), FretboardPosition(3, 14), FretboardPosition(2, 10), FretboardPosition(1, 5)],
        Note("A#", 2) : [                                                    FretboardPosition(4, 20), FretboardPosition(3, 15), FretboardPosition(2, 11), FretboardPosition(1, 6)],
        Note("Bb", 2) : [                                                    FretboardPosition(4, 20), FretboardPosition(3, 15), FretboardPosition(2, 11), FretboardPosition(1, 6)],
        Note("B", 2) :  [                                                    FretboardPosition(4, 21), FretboardPosition(3, 16), FretboardPosition(2, 12), FretboardPosition(1, 7)],
        Note("C", 2) :  [                                                    FretboardPosition(4, 22), FretboardPosition(3, 17), FretboardPosition(2, 13), FretboardPosition(1, 8)],
        Note("C#", 2) : [                                                    FretboardPosition(4, 23), FretboardPosition(3, 18), FretboardPosition(2, 14), FretboardPosition(1, 9)],
        Note("Db", 2) : [                                                    FretboardPosition(4, 23), FretboardPosition(3, 18), FretboardPosition(2, 14), FretboardPosition(1, 9)],
        Note("D", 2) :  [                                                    FretboardPosition(4, 24), FretboardPosition(3, 19), FretboardPosition(2, 15), FretboardPosition(1, 10)],
        Note("D#", 2) : [                                                                              FretboardPosition(3, 20), FretboardPosition(2, 16), FretboardPosition(1, 11)],
        Note("Eb", 2) : [                                                                              FretboardPosition(3, 20), FretboardPosition(2, 16), FretboardPosition(1, 11)],
        
        # Three octaves up
        Note("E", 3) :  [                                                                              FretboardPosition(3, 21), FretboardPosition(2, 17), FretboardPosition(1, 12)],
        Note("F", 3) :  [                                                                              FretboardPosition(3, 22), FretboardPosition(2, 18), FretboardPosition(1, 13)],
        Note("F#", 3) : [                                                                              FretboardPosition(3, 23), FretboardPosition(2, 19), FretboardPosition(1, 14)],
        Note("Gb", 3) : [                                                                              FretboardPosition(3, 23), FretboardPosition(2, 19), FretboardPosition(1, 14)],
        Note("G", 3) :  [                                                                              FretboardPosition(3, 24), FretboardPosition(2, 20), FretboardPosition(1, 15)],
        Note("G#", 3) : [                                                                                                        FretboardPosition(2, 21), FretboardPosition(1, 16)],
        Note("Ab", 3) : [                                                                                                        FretboardPosition(2, 21), FretboardPosition(1, 16)],
        Note("A", 3) :  [                                                                                                        FretboardPosition(2, 22), FretboardPosition(1, 17)],
        Note("A#", 3) : [                                                                                                        FretboardPosition(2, 23), FretboardPosition(1, 18)],
        Note("Bb", 3) : [                                                                                                        FretboardPosition(2, 23), FretboardPosition(1, 18)],
        Note("B", 3) :  [                                                                                                        FretboardPosition(2, 24), FretboardPosition(1, 19)],
        Note("C", 3) :  [                                                                                                                                  FretboardPosition(1, 20)],
        Note("C#", 3) : [                                                                                                                                  FretboardPosition(1, 21)],
        Note("Db", 3) : [                                                                                                                                  FretboardPosition(1, 21)],
        Note("D", 3) :  [                                                                                                                                  FretboardPosition(1, 22)],
        Note("D#", 3) : [                                                                                                                                  FretboardPosition(1, 23)],
        Note("Eb", 3) : [                                                                                                                                  FretboardPosition(1, 23)],
        
        # Four Octaves up
        Note("E", 4) :  [                                                                                                                                  FretboardPosition(1, 24)]
        
        }

CIRCLE_OF_FIFTHS = [
                   "C", 
                   "G", 
                   "D", 
                   "A", 
                   "E", 
                   "B", 
                   "Gb", 
                   "Db", 
                   "Ab", 
                   "Eb", 
                   "Bb", 
                   "F"]

def lateral_fretboard_distance(note1, note2):
    """returns the lateral distance (how many frets away) this note is from another note on the fretboard. Used to determine whether or not the note should be on the same string, or a different string. E.g. it is extremely difficult to go from the 3rd fret to the 9th fret on the E string, so it would be better to play the 3rd fret on the E string, then the 4th fret on the A string."""
    if TAB_MAP[note1].string == TAB_MAP[note2].string:
        highest_fret = max(TAB_MAP[note1].fret, TAB_MAP[note2].fret)
        lowest_fret = min(TAB_MAP[note1].fret, TAB_MAP[note2].fret)
        return highest_fret - lowest_fret

"""
def note_to_fret(note, previous = None):
    # previous argument is if you want the placement of the note to be contextual. For example, if the previous note is the 3rd fret on the E string, then the next note should not be the 11th fret on the E string, as this will be hard to reach. It should instead then be the 6th fret on the A string
    if previous == None:
        if note in TAB_MAP:
            return TAB_MAP[note]
        else:
            print("Error: note is not in tablature map (you need to update it)")
    else:
        if note in TAB_MAP and previous in TAB_MAP:
           # later add code to ensure that the  
           
        else:
            print("Erorr: the note is not in the tablature map (you need to update it)")
"""

def determine_tuning(notes: list):
    """
    Determines the tuning the guitar should be in, based on the lowest played note.
    """
    decision = None
    lowest_octave = 0
    for note in notes:
        if note.octave < lowest_octave:
            lowest_octave = note.octave

    candidates = []
    for note in notes:
        if note.octave == lowest_octave:
            candidates.append(note)
    
    # still working this out
    # started this method really quick while i had some time before going to the gym 
    for tuning in TUNINGS:
        if tuning[0] in candidates:
            decision = tuning
    return tuning

def transpose_fretboard_position(note, level: int):
    """
    Given a note, return the position on the fretboard on which it is played for a guitar that is tuned <level> HALF STEPS lower or higher.
    
    Keyword arguments:
    note -- an instance of the Note class
    level -- the amount of half steps to transpose up or down
    """
    positions = TAB_MAP[note]
    transposed_positions = []
    for position in positions:
        # transpose the note up/down
        transposed_note = position.fret + level
    
        # check for validity on guitar with 24 frets
        if transposed_note in range(0, 25):
            transposed_positions.append(FretboardPosition(position.string, transposed_note))
    
    return(transposed_positions)

def get_perfect_fifth(note: str):
    """
    Returns the perfect 5th of a given note. Useful for procedurally generating the list of notes to play for various chords.
    
    keyword arguments:
    note -- string representation of a note. Octave doesn't matter here, so an instance of the Note class is not necessary.
    """
    # index of the note in the 
    index = CIRCLE_OF_FIFTHS.index(note)
    if index < len(CIRCLE_OF_FIFTHS) - 1:
        perfect_fifth = CIRCLE_OF_FIFTHS[index + 1]
    else:
        perfect_fifth = CIRCLE_OF_FIFTHS[0]
    return(perfect_fifth)
 
def get_perfect_fourth(note: str):
    """
    Returns the perfect 4th of a given note. Useful for procedurally generating the list of notes to play for various chords. Same as the get_perfect_fifth method, but it goes backwards.
    
    keyword arguments:
    note -- string representation of a note. Octave doesn't matter here, so an instance of the Note class is not necessary.
    """
    # index of the note in the 
    index = CIRCLE_OF_FIFTHS.index(note)
    if index > 0:
        perfect_fourth = CIRCLE_OF_FIFTHS[index - 1]
    else:
        perfect_fourth = CIRCLE_OF_FIFTHS[len(CIRCLE_OF_FIFTHS)-1]
    return(perfect_fourth)
        
        
            
