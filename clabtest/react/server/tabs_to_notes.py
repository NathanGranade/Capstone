from sys import argv
from itertools import chain

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
    for x in range(len(modified_list)):
        # index 0 is always the open-string note in modified_list
        # (see separate_open_notes_from_fret_positions() method)
        open_note = modified_list[x][0]
        
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

if len(argv) < 2:
    exit()

file_contents = get_file_contents(argv[1])

preprocessed_file_contents = separate_open_notes_from_fret_positions(file_contents)

unprocessed_tab_dictionary = get_unprocessed_tab_dictionary(preprocessed_file_contents)

for key in unprocessed_tab_dictionary.keys():
    print(f"{key}: {unprocessed_tab_dictionary[key]}")
