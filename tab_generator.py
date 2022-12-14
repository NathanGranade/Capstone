WHOLE_STEPS = ["A", "B", "C", "D", "E", "F", "G"]

TUNINGS = {
        # NOTE: 7 and 8 string guitar tunings can be created by simply appending extended range to existing 6 string tuning; for example, B standard (7 string) = ["B"] + TUNINGS["E standard"] 

        # 6 String standard tunings
        "E standard": ["E", "A", "D", "G", "B", "E"],
        # Eb standard is the same as D# standard
        "Eb standard" : ["Eb", "Ab", "Db", "Gb", "Bb", "Eb"], 
        "D standard" : ["D", "G", "C", "F", "A", "D"],
        # C# standard is the same as Db standard
        "C# standard": ["C#", "F#", "B", "E", "G#", "C#"] 
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
TAB_MAP = {
        Note("E", 0) : [FretboardPosition(6, 0)], 
        Note("F", 0) : [FretboardPosition(6, 1)],
        Note("F#", 0) : [FretboardPosition(6, 2)],
        Note("G", 0) : [FretboardPosition(6, 3)],
        Note("Ab", 0) : [FretboardPosition(6, 4)],
        Note("A", 0) : [FretboardPosition(6, 5), FretboardPosition(5, 0)],
        Note("A#", 0) : [FretboardPosition(6, 6), FretboardPosition(5, 1)],
        Note("B", 0) : [FretboardPosition(6, 7), FretboardPosition(5, 2)],
        Note("C", 0) : [FretboardPosition(6, 8)], FretboardPosition(5, 3)],
        Note("C#", 0) : [FretboardPosition(6, 9), FretboardPosition(5, 4)],
        Note("D", 0) : [FretboardPosition(6, 10), FretboardPosition(5, 5), FretboardPosition(4, 0)],
        Note("Eb", 0) : [FretboardPosition(6, 11), FretboardPosition(5, 6), FretboardPosition(4, 1)],
        
        # One octave up
        Note("E", 1) : [FretboardPosition(6, 12), FretboardPosition(5, 7), FretboardPosition(4, 2)],
        Note("F#", 1) : [FretboardPosition(6, 13), FretboardPosition(5, 8), FretboardPosition(4, 3)],
        Note("F", 1) : [FretboardPosition(6, 14), FretboardPosition(5, 9), FretboardPosition(4, 4)],
        Note("G", 1) : [FretboardPosition(6, 15), FretboardPosition(5, 10), FretboardPosition(4, 5), FretboardPosition(5, 0)],
        Note("Ab", 1) : [],
        Note("A", 1) : [],
        Note("A#", 1): [],
        Note("B", 1) : [],
        Note("C", 1) : [],
        Note("C#", 1) : [],
        Note("D", 1) : [],
        Note("Eb", 1) : [],
        Note("E", 2) : [],
        }

 def lateral_fretboard_distance(note1, note2):
    """returns the lateral distance (how many frets away) this note is from another note on the fretboard. Used to determine whether or not the note should be on the same string, or a different string. E.g. it is extremely difficult to go from the 3rd fret to the 9th fret on the E string, so it would be better to play the 3rd fret on the E string, then the 4th fret on the A string."""
    if TAB_MAP[note1].string == TAB_MAP[note2].string:
        highest_fret = max(TAB_MAP[note1].fret, TAB_MAP[note2].fret)
        lowest_fret = min(TAB_MAP[note1].fret, TAB_MAP[note2].fret)
        return highest_fret - lowest_fret

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


