import pyttsx3 
import os
import numpy
pyttsx3.speak("welcome to my world!!")
initial_command=['start', 'open', 'execute', 'run']
notepad = ['notepad', 'text editor', 'text writer', 'text']
browser = ['chrome', 'chrome browser', 'chromium', 'google chrome', 'web browser']
media = ['window media player',' media player' , 'video player', ' media']
terminate_command =['exit', 'end', 'terminate', 'close', 'stop']
while True:
	pyttsx3.speak("Enter application name you want to open:")
	print("Enter application name :", end='')
	x = input()
	if ((initial_command[0] in x) or (initial_command[1] in x) or (initial_command[2] in x) or  (initial_command[3] in x)):

		if ((notepad[0] in x) or (notepad[1] in x) or (notepad[2] in x) or (notepad[3] in x))  :
			os.system("start notepad")
			pyttsx3.speak("welcome to notepad")
		elif ((browser[0] in x) or (browser[1] in x) or  (browser[2] in x) or (browser[3] in x) or (browser[4] in x) or(browser[5] in x)) :
			os.system("start chrome yahoo.com")
			pyttsx3.speak("Welcome to chrome")
		elif ((media[0] in x) or (media[1] in x) or  (media[2] in x) or (media[3] in x)):
			os.system("start wmplayer")
			pyttsx3.speak("Welcome to Windows media Player")

	elif ((terminate_command[0] in x) or (terminate_command[1] in x) or (terminate_command[2] in x) or  
	(terminate_command[3] in x)or  (terminate_command[4] in x)):
		os.system("exit")
		pyttsx3.speak("Thank you, have a nice day")
	else:
		print("File Doesn't support")
		pyttsx3.speak("File doesn't support")
