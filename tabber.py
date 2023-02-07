from transcriber import *

# list of notes by string
Estring = ['E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2', 'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3', 'C4', 'C#4', 'D4', 'D#4', 'E4']
Astring = ['A2', 'A#2', 'B2', 'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4']
Dstring = ['D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4', 'C5', 'C#5', 'D5']
Gstring = ['G3', 'G#3', 'A3', 'A#3', 'B3', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4', 'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5']
Bstring = ['B3', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4', 'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5']
estring = ['E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4', 'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5', 'C6', 'C#6', 'D6', 'D#6', 'E6']

EstringTab = []
AstringTab = []
DstringTab = []
GstringTab = []
BstringTab = []
estringTab = []

def tab(notes):
    for i in notes:
        if i in estring:
            for index, j in enumerate(estring):
                if i == j:
                    estringTab.append(str(index))
                    BstringTab.append('--')
                    GstringTab.append('--')
                    DstringTab.append('--')
                    AstringTab.append('--')
                    EstringTab.append('--')
        else:
            estringTab.append('--')

            if i in Bstring:
                for index, j in enumerate(Bstring):
                    if i == j:
                        BstringTab.append(str(index))
                        estringTab.append('--')
                        GstringTab.append('--')
                        DstringTab.append('--')
                        AstringTab.append('--')
                        EstringTab.append('--')
            else:
                BstringTab.append('--')

                if i in Gstring:
                    for index, j in enumerate(Gstring):
                        if i == j:
                            GstringTab.append(str(index))
                            BstringTab.append('--')
                            estringTab.append('--')
                            DstringTab.append('--')
                            AstringTab.append('--')
                            EstringTab.append('--')
                else:
                    GstringTab.append('--')

                    if i in Dstring:
                        for index, j in enumerate(Dstring):
                            if i == j:
                                DstringTab.append(str(index))
                                BstringTab.append('--')
                                GstringTab.append('--')
                                estringTab.append('--')
                                AstringTab.append('--')
                                EstringTab.append('--')
                    else:
                        DstringTab.append('--')

                        if i in Astring:
                            for index, j in enumerate(Astring):
                                if i == j:
                                    AstringTab.append(str(index))
                                    BstringTab.append('--')
                                    GstringTab.append('--')
                                    DstringTab.append('--')
                                    estringTab.append('--')
                                    EstringTab.append('--')
                        else:
                            AstringTab.append('--')

                            if i in Estring:
                                for index, j in enumerate(Estring):
                                    if i == j:
                                        EstringTab.append(str(index))
                                        BstringTab.append('--')
                                        GstringTab.append('--')
                                        DstringTab.append('--')
                                        AstringTab.append('--')
                                        estringTab.append('--')
                            else:
                                EstringTab.append('--')

notes = transcribe("test.wav")
tab(notes)

print('-'.join(estringTab))
print('-'.join(BstringTab))
print('-'.join(GstringTab))
print('-'.join(DstringTab))
print('-'.join(AstringTab))
print('-'.join(EstringTab))
