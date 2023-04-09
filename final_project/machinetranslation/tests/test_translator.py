'''
theses are the unit tests for translator.py's functions
'''

import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    '''
    tests the english_to_french function 
    '''

    def test_null(self):
        '''
        tests for null imput
        '''

        self.assertEqual(english_to_french(None), None)

    def test_hello(self):
        '''
        checks that 'Hello' translates to 'Bonjour'
        '''

        self.assertEqual(english_to_french("Hello"), "Bonjour")

class TestFrenchToEnglish(unittest.TestCase):
    '''
    tests the french_to_english function
    '''

    def test_null(self):
        '''
        tests for null imput
        '''

        self.assertEqual(french_to_english(None), None)

    def test_hello(self):
        '''
        checks that 'Bonjour' translates to 'Hello'
        '''

        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()
