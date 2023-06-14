from os import get_terminal_size
from math import floor

TUNINGS = {
        # standard tunings
        "E standard": "EADGBe",
        "Eb standard": "", 
        "D# standard": "",
        "D standard": "DGCFAd",
        "Db standard": "",
        "C# standard": "",
        "C standard": "C...",
        "B standard": "BEADGbe",
        "Ab standard": "",
        "A standard": "ADGCFad",
        "A# standard": "",
        
        # drop tunings
        "Drop D": "DAdGBE",
        "Drop A": "AEAGBe"
        }

class Note:
    def __init__(self, string: str, fret: int):
        self.string = string
        self.fret = fret

class Chord:
    def __init__(self, notes: dict):
        self.notes = notes

    def __len__(self) -> int:
        return(len(self.notes.keys()))
    
    def __str__(self) -> str:
        representation = ""
        for string in self.notes.keys():
            fret = self.notes[string]
            representation += f"{string}|-{fret}-\n"
        representation = representation[:len(representation)-1]
        return(representation)
    
    def __iter__(self):
        for string in self.notes.keys():
            yield(string)

    def __getitem__(self, item: str) -> int:
        if item in self.notes.keys():
            return(self.notes[item])
        else:
            return(None)

    def generate_chord(staff, string: str, fret: int, kind: str):
        if not string in staff.tuning:
            return(None)
        if kind == "power":
            start_index = staff.tuning.index(string)
            strings = staff.tuning[start_index : start_index -3 : -1]
            _map = {string: fret}
            for x in range(1, len(strings)): 
                _map[strings[x]] = fret + 2
        return(Chord(_map))
            

# The Staff class is a single one of those blocks
# listing the tuning and several notes. It uses arrays to
# ensure uniform size and easy placement of notes
class Staff:
    def __init__(self, tuning: str):
        if tuning in TUNINGS.keys():
            self.tuning = TUNINGS[tuning]
        else:
            self.tuning = tuning
        # reverse the tuning so that it appears
        # from bottom to top on the staff
        self.tuning = self.tuning[::-1]
        self.string_map = dict()
        for string in self.tuning:
            self.string_map[string] = ["-"] * 48
        self.head = 0

    def __str__(self): 
        representation = ""
        for string in self.string_map.keys():
            frets = "".join(self.string_map[string])
            representation += f"{string}|{frets}\n"
        # shave off final \n
        representation = representation[0 : len(representation)-1]
        return(representation)
    
    def find_longest_string(self) -> str:
        longest_string = self.tuning[0]
        stripped_string_map = dict()
        for string in self.string_map.keys():
            string_with_just_notes = [fret for fret
                                      in self.string_map[string]
                                      if fret != "-"] 
            stripped_string_map[string] = string_with_just_notes

        for string in stripped_string_map.keys():
            if len(stripped_string_map[string]) > len(stripped_string_map[longest_string]):
                longest_string = string
        return(string)
                
    def find_nearest_position(self, string: str) -> int:
        if string in self.tuning:
            position = 0
            frets = self.string_map[string][self.head:]
            for fret in frets:
                if fret == "-" and frets[position - 1] == "-":
                    return(self.head + position)
                else:
                    position += 1
            return(self.head + position)

    def __correct_imbalance(self) -> None:
        lengths: dict = {
                        string : len("".join(self.string_map[string]))
                        for (string, frets) in zip(self.string_map.keys(), self.string_map.values())
                        }
        max_length = max(lengths.values())
        imbalanced_strings = [string for string in lengths.keys()
                              if lengths[string] < max_length]
        
        if len(imbalanced_strings) == 0:
            return

        for string in imbalanced_strings: 
            self.string_map[string].insert(self.head - 1, "-")

    def add_note_instance(self, note, position: int = None) -> None:
        if not note.string in self.tuning:
            return
        
        if position == None:
           position = self.find_nearest_position(note.string)

        self.string_map[note.string][position] = str(note.fret)
        self.head = self.find_nearest_position(note.string)
        self.__correct_imbalance()
    
    def add_note(self, string: str, fret: int, position: int = None) -> None:
        if not string in self.tuning:
            return
        
        if position == None:
            position = self.find_nearest_position(string)
        
        fret = str(fret)
        self.string_map[string][position] = fret
        self.head = self.find_nearest_position(string)
        self.__correct_imbalance()
    
    def _chord_can_be_played(self, chord):
        for string in chord:
            if not string in self.tuning:
                return(False)
        return(True)

    def add_chord(self, chord, position: int = None) -> None:
        if not self._chord_can_be_played(chord):
            return
        
        nearest_positions = []
        for string in chord:
            nearest_positions.append(self.find_nearest_position(string))
        nearest_position = max(nearest_positions)
        
        for string in chord:
            fret = chord[string]
            self.string_map[string][nearest_position] = str(fret) 
            self.head = self.find_nearest_position(string)
        self.__correct_imbalance()

    def __add__(self, other):
        if type(other) == Note:
            self.add_note_instance(other)

        if type(other) == Chord:
            self.add_chord(other)
        self.__correct_imbalance()
        return(self)
class Tab:
    def __init__(self,  title: str = "Untitled",
                        staves = []
                ):
        self.title = title
        self.staves = staves
    
    def add_staff(self, staff) -> None:
        self.staves.append(staff)

    def _calculate_displayable_staves(self):
        columns = get_terminal_size().columns
        quotient = floor(columns / 56)
        return(quotient)
    
    def _concatenate_staves(self, staves: list) -> str:
        # just join the strings of the lines in the dictionary
        # and add a space after

        representation = ""
        joined_strings = dict()
        for string in staves[0].string_map:
            joined_string = []
            for x in range(0, len(staves)):
                joined_string += staves[x].string_map[string]
                # later use \t as delimiter
                if x < (len(staves) - 1):
                    joined_string.append(f"\t{string}|")
            joined_strings[string] = joined_string

        for string in joined_strings:
            frets = "".join(joined_strings[string])
            representation += f"{string}|{frets}\n"
        return(representation)
 
    def __str__(self) -> str:
        representation = ""
        displayable_staves = self._calculate_displayable_staves()
        for x in range(0, len(self.staves), displayable_staves):
            if x + displayable_staves < len(self.staves):
                concatenated = self._concatenate_staves(self.staves[x:x + displayable_staves])
            else:
                concatenated = self._concatenate_staves(self.staves[x:])
            representation += f"{concatenated}\n"
        return(representation)
