import pretty_midi
import os


Notes={40:'E2' , 41:'F2', 42:'F#2' , 43:'G2', 44:'G#2' , 45:'A2', 46:'A#2', 47:'B2' , 48:'C3', 49:'C#3', 50:'D3', 51:'D#3',
        52:'E3', 53:'F3', 54:'F#3', 55:'G3', 56:'G#3', 57:'A3', 58:'A#3', 59:'B3', 60:'C4', 61:'C#4', 62:'D4', 63:'D#4',
        64:'E4', 65:'F4', 66:'F#4', 67:'G4', 68:'G#4', 69:'A4', 70:'A#4', 71:'B4', 72:'C5', 73:'C#5', 74:'D5', 75:'D#5',
        76:'E5',  77:'F5', 78:'F#5', 79:'G5', 80:'G#5', 81:'A5', 82:'A#5', 83:'B5', 84:'C6', 85:'C#6', 86:'D6', 87:'D#6',
        88:'E6', 89:'F6', 90:'F#6', 91:'G6', 92:'G#6', 93:'A6', 94:'A#6', 95:'B6'}


l = []
midi_data = pretty_midi.PrettyMIDI('blackbird.mid')
print("duration:",midi_data.get_end_time())
print("{}".format(pretty_midi.Note))
print(f'{"note":>10} {"start":>10} {"end":>10}')
for instrument in midi_data.instruments:
    print("instrument:", instrument.program)
    for note in instrument.notes:
        l.append(note.pitch)
filepath = os.path.join('RawNotes', 'RawNotes.txt')
if not os.path.exists('RawNotes'):
    os.makedirs('RawNotes')
file = open(filepath, "+w")
for item in Notes:
    if item in Notes:
        file.write(Notes[item] + " ")
        #print(Notes[item])
    else:
        pass

        
