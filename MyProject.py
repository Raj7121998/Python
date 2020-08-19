import pyttsx3
import os

pyttsx3.speak("Hey ! Welcome to the tool, Tell me how can i help you")

while True:
	print("chat with me with your requirements : "  , end='')
	p = input()

	if (("run" in p) or ("launch" in p) or ("execute" in p))  and (("chrome" in p) or ("browser" in p)):
	  pyttsx3.speak("Thanks For Your Input")
	  os.system("chrome")

	elif (("run" in p) or ("launch" in p) or ("execute" in p)) and  (("notepad" in p) or ("editor" in p) ) :
	  pyttsx3.speak("Thanks For Your Input")
	  os.system("notepad")

	elif (("run" in p) or ("launch" in p) or ("execute" in p))  and (("player" in p) or ("media" in p)):
	  pyttsx3.speak("Thanks For Your Input")
	  os.system("wmplayer")

	elif (("run" in p) or ("launch" in p) or ("execute" in p))  and (("paint" in p) or ("mspaint" in p)):
	  pyttsx3.speak("Thanks For Your Input")
	  os.system("mspaint")

	elif  (("exit" in p)  or ("quit" in p) or ("close" in p)) and ("tool" in p):
	  pyttsx3.speak("Thank You! Visit Again")
	  break

	else:
	  pyttsx3.speak("Sorry! Data Unavailable")
	  print("dont support")

