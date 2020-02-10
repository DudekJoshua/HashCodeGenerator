import hashlib
import os
# from colorama import Fore, Back, Style
from ansiEscapes import *

def isInputValid(inputValue, validInput=[]):
	for i in range(len(validInput)):
		if validInput[i] == inputValue:
			return True
	return False

def invalidInput(strVarToAssignInput, prompt):
	print("%s%sInvalid option; try again%s" % (style.BOLD, fgndColor.RED, style.RESET_ALL))
	strVarToAssignInput = input(prompt)
	return strVarToAssignInput

def internalErr():
	print("%s%sAn internal error occured!%s" % (style.BOLD, fgndColor.RED, style.RESET_ALL))
	print("%sPlease contact %smultips2020@gmail.com%s" % (fgndColor.YELLOW, fgndColor.BLUE, style.RESET_ALL))

sha1hash = hashlib.sha1()
choiceValidInputs = ["1", "2"]
hashTypeValidInputs = ["1", "2", "3"]

welcome = '''
%s%sWelcome to hash generator!%s

%s[1] %sgenerate a hash code from input
%s[2] %squit%s
''' % (style.BOLD, fgndColor.BLUE, style.RESET_ALL, fgndColor.YELLOW, fgndColor.CYAN, fgndColor.YELLOW, fgndColor.CYAN, style.RESET_ALL)

hashTypeSelec = '''
%s[1] %sSHA1/SHA256
%s[2] %sSHA512
%s[3] %sreturn to welcome page
''' % (fgndColor.YELLOW, style.RESET_ALL, fgndColor.YELLOW, style.RESET_ALL, fgndColor.YELLOW, style.RESET_ALL)

os.system("clear")

print(welcome)
choice = input("\nWhat do you want to do? ")

while isInputValid(choice, choiceValidInputs):
	if choice == "1":
		os.system("clear")
		print(hashTypeSelec)
		hashType = input("\nWhat hash type do you want? ")
		while not isInputValid(hashType, hashTypeValidInputs):
			hashType = invalidInput(hashType, "What hash type do you want? ")
		while isInputValid(hashType, hashTypeValidInputs):
			if hashType == "1":
				os.system("clear")
				pass
			elif hashType == "2":
				os.system("clear")
				pass
			elif hashType == "3":
				os.system("clear")
				print(welcome)
				choice = input("\nWhat do you want to do? ")
				pass
	elif choice == "2":
		reallyQuit = input("Do you really want to quit? (y/n) ").lower()
		if reallyQuit == "y":
			print("\nGoodbye!\n")
			os.system("clear")
			quit()
		elif reallyQuit == "n":
			print(welcome)
			choice = input("\nWhat do you want to do? ")

while not isInputValid(choice, choiceValidInputs):
	choice = invalidInput(choice, "What do you want to do? ")

