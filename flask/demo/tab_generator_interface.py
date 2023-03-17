from sys import argv
import tab_generator
from tunings import generate_tunings_map

argc = len(argv)

def generate_output_filename(input_name: str):
    split_name = input_name.split(".")
    split_base_name = split_name[:len(split_name)-1]
    base_name = ""
    for part in split_base_name:
        base_name += part
    
    # if this character is at the start of the
    # input file name, it will not be able to
    # create the output file. "Error: access denied"
    if base_name[0] == "\\":
        base_name = base_name[1:]
    return(base_name)

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
    # note that using 15 as the batch size was determined arbitrarily.
    # It just so happens that using 15 results in nicely sized
    # tabs, but any number would do. 
    if len(notes) >= 15:
        segment = notes[0:15]
        remainder = notes[15:]
    else:
        segment = notes[0:len(notes)]
        remainder = []
    return(segment, remainder)

def parse_arguments():
    """
    reads the arguments from the command line and returns them in a dictionary
    where the key-value pairs are (setting, value)
    """
    # you must provide at least a context and a file
    # python tab_generator_interface.py generate_tab notes_file.txt tuning="Drop D"
    #                                   ^            ^              ^
    #                                   context      file           parameters
    if len(argv) < 3:
        print("Insufficient arguments provided.")
        return(None)
    
    # first argument is always the context -- what you want to do
    context = argv[1]
    
    # second arugment is always the file you want to work with
    file = argv[2]
    
    # create a dictionary mapping a setting to a value
    arguments = {"context": context, "file": file}
    for x in range(3, len(argv)):
        arg = argv[x]
        if "=" in arg:
            split_arg = arg.split("=")
            key = split_arg[0]
            value = split_arg[1]
            arguments[key] = value
    return(arguments)

if argc >= 3:
    arguments = parse_arguments()
    # if insufficient arguments given, do not execute.
    # parse_arguments() will contextualize the error with a print statement
    if arguments == None:
        exit()
    
    DEBUG = False
    if "DEBUG" in arguments.keys():
        DEBUG = arguments["DEBUG"]
        if DEBUG in ["true", "on", "True", "TRUE", "ON"]:
            DEBUG = True
    
    CONTEXT_MAP = {
        "generate_tab": None,
        "get_tuning": None,
        "is_valid_tuning": None,
        "get_tunings": None
    }
    
    if arguments["context"] == "generate_tab":
        with open(f"RawNotes/RawNotes-tab.txt", "w") as f:
            # read the contents of the file passed to the program
            # this file should contain note representations
            notes = read_notes(arguments["file"])
            
            if DEBUG:
                print(notes)
            
            # the format of notes in the notes list should be for
            # the transcriber, which is not how notes are represented
            # by the tab generator. So convert the notes to the
            # internal representation of the generator, using the
            # parse_transcriber_note method
            generator_compatible_notes = []
            for note in notes:
                generator_compatible_notes.append(tab_generator.parse_transcriber_note(note))
            
            if DEBUG:
                for note in generator_compatible_notes:
                    print(str(note))
                
            # determine the tuning of the song -- setup
            tunings = generate_tunings_map()
            valid_tunings = tab_generator.determine_all_tunings(generator_compatible_notes, tunings)
            
            # determine the tuning of the song -- decision making
            # (1) if arguments were supplied to target a specific tuning
            #     AND the song can be played in that tuning, then use this tuning
            #     when generating the tab
            if ("tuning" in arguments.keys()) and (arguments["tuning"] in valid_tunings):
                tuning = arguments["tuning"]
            # (2) if no arguments were supplied to target a specific tuning
            #     OR a tuning was supplied, but the song cannot be played
            #     in that tuning, then automatically determine a tuning
            #     and generate the tab with that tuning
            else:
                tuning = tab_generator.determine_tuning(generator_compatible_notes, tunings)
            
            if DEBUG:
                print(f"Tuning is {tuning}")
                print("Other valid tunings are:")
                for option in valid_tunings:
                    print(f"\t{option}")
            
            # generate several tab_dictionary instances containing at most
            # 15 notes so as to make the overall tab broken up into small
            # and easily digestable segments, like how a human would write
            # a tab
            while len(generator_compatible_notes) > 0:
                segment, generator_compatible_notes = get_batch(generator_compatible_notes)
                tab_dictionary = tab_generator.generate_tab_dictionary(segment, tuning)
                tab = tab_generator.generate_tab(tab_dictionary, tuning)
                f.write(f"{tab}\n")
            f.close()
