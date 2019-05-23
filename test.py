import pytest
import translation	
import simple_cv
import dict_json

'''
Simple pytest file for checking the correctness of main methods.
'''
def test_1():
	'''
	translation.translate() Test 1.
	This test proves correctness of Google translation function.
	'''
	initial_word = 'собака'
	answer = 'dog'
	assert translation.translate(initial_word, 'eng', 'ru') == answer, "test failed"

def test_2():
	'''
	translation.translate() Test 2.
	This test proves correctness of Google translation function.
	'''
	initial_word = 'dog'
	answer = 'собака'
	assert translation.translate(initial_word, 'ru', 'eng') == answer, "test failed"


def test_3():
	'''
	simple_cv.get_image_text() Test.
	This test proves correctness of OCR PyTesseract image reading.
	'''
	path = '/home/biowar/IPZProject7103/TelegramBot/Test_image2.jpg'
	answer = 'Яблучний сік'
	assert answer in simple_cv.get_image_text(path, lang='ukr') , "test failed"

def test_4():
	'''
	dict_json.vocabulary() Test.
	Simple test for getting data from json.
	'''
	initial_word = 'dog'
	answer = ['A common four-legged animal, especially kept by people as a pet or to hunt or guard things.', 'A dull, unattractive girl or woman.', 'An iron for holding wood in a fireplace.']
	assert dict_json.vocabulary('dog') == answer, "test failed"
