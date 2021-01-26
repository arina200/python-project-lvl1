#!/usr/bin/env python
import prompt
def user_welcome():
	print("Welcome to the Brain Games!")
	name = prompt.string('May I have your name? ')
	print('Hello' + ', ' + name + '!')
def main():
	user_welcome()
if __name__ == '__main__':
    main()
