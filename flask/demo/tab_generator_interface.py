from sys import argv
import tab_generator

argc = len(argv)

def read_notes(filename: str):
    """
    reads the notes from 
    
    keywords arguments
    filename -- the name/path of the file that contains the notes
                read from the transcriber application.
    """
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    for x in range(0, len(lines)):
        lines[x] = lines[x][:len(lines[x])-1]
    notes = []
    for line in lines:
        split_line = line.split()
        for note in split_line:
            notes.append(note)
    return(notes)
    
def get_batch(notes):
    """
    breaks a list of notes into a segment containing up to 15 notes. Returns
    the segment as well as what remains of the note list without the segment.
    
    keyword arguments
    notes -- a list containing the tab generator's internal representation
             for notes.
    """
    if len(notes) >= 15:
        segment = notes[0:15]
        remainder = notes[15:]
    else:
        segment = notes[0:len(notes)]
        remainder = []
    return(segment, remainder)
    
if argc > 1:
    for arg in argv[1:]:
        # read the contents of the file passed to the program
        # this file should contain note representations
        notes = read_notes(arg)
        print(notes)
        
        # the format of notes in the notes list should be for
        # the transcriber, which is not how notes are represented
        # by the tab generator. So convert the notes to the
        # internal representation of the generator, using the
        # parse_transcriber_note method
        generator_compatible_notes = []
        for note in notes:
            generator_compatible_notes.append(tab_generator.parse_transcriber_note(note))
        for note in generator_compatible_notes:
            print(str(note))
        # generate several tab_dictionary instances containing at most
        # 15 notes so as to make the overall tab broken up into small
        # and easily digestable segments, like how a human would write
        # a tab
        while len(generator_compatible_notes) > 0:
            segment, generator_compatible_notes = get_batch(generator_compatible_notes)
            tab_dictionary = tab_generator.generate_tab_dictionary(segment)
            tab = tab_generator.generate_tab(tab_dictionary)
            print(tab)
            print()
        