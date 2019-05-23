import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

def vocabulary(word):
	data = json.load(open("data.json"))
	word = word.lower()
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	else:
		return False	
'''
	elif len(get_close_matches(word, data.keys())) > 0:
		action = input("Did you mean %s instead? [y or n]:" % get_close_matches(word, data.keys())[0])
		if (action == "y"):
			return data[get_close_matches(word, data.keys())[0]]
		elif (action == "n"):
			return ("The word doesn't exist, yet.")
		else: 
			return ("We don't understand your entry, Apologies.")
	else:
		return ("The word doesn't exist, please double check it.")
'''
