import transcriber
import unittest
import os
#this unit test case will test if the file passed the transcriber.py is in the correct directory, a string, or empty and not a string

class TestSum(unittest.TestCase):
    def test_pass(self):
        data = "test.wav"
        expected = ['E5', 'D#5', 'E5', 'D#5', 'E5', 'B4', 'D5', 'C5', 'A4', 'C4', 'F4', 'A4', 'B4', 'B5', 'E4', 'G#4', 'B4', 'C5']
        output = transcriber.transcribe(data)
        self.assertEqual(transcriber.transcribe(data), expected, f'Output is {transcriber.transcribe(data)} rather than {expected}')
    def test_empty(self):
        data = ""
        expected = []
        output = transcriber.transcribe(data)
        self.assertEqual(transcriber.transcribe(data), expected, f'Output is {transcriber.transcribe(data)} rather than {expected}')
    def test_isNotString(self):
        data = 5
        expected = "Input is not String! Enter file name as string in .wav format"
        output = transcriber.transcribe(data)
        self.assertEqual(transcriber.transcribe(data), expected, f"Output is {transcriber.transcribe(data)} rather than {expected}")
    def test_notWav(self):
        data = "test.mp3"
        expected = "Incorrect file type! This program accepts files of .wav format."
        output = output = transcriber.transcribe(data)
        self.assertEqual(transcriber.transcribe(data), expected, f"Output is {transcriber.transcribe(data)} rather than {expected}")
    def test_fileNotFound(self):
        data = "something.wav"
        expected = "Error! Could not find File in dirctory"
        output = transcriber.transcribe(data)
        self.assertEqual(transcriber.transcribe(data), expected, f"Output is {transcriber.transcribe(data)} rather than {expected}")
        os.system('cls' if os.name=='nt' else 'clear')


if __name__ == '__main__':
    import xmlrunner

    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        failfast=False,
        buffer=False,
        catchbreak=False)
    
        
    

    

