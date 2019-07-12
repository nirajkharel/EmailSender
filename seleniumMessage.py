#! python3
# platform = Ubuntu
# Browser = Firefox Developer Edition
# seleniumMessage.py - sends emails by crawling itself.

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import sys

#  Enter your email and password.
user_email = "your_email"
user_password = "your_passwod"

if len(sys.argv) >= 3:
	# For decoration on the shell
	# Includes colors, fonts, sizes
	BLUE, RED, WHITE, YELLOW, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[32m', '\033[0m'


	sys.stdout.write(RED + """    
		███████╗███╗   ███╗ █████╗ ██╗██╗         
		██╔════╝████╗ ████║██╔══██╗██║██║         
		█████╗  ██╔████╔██║███████║██║██║         
		██╔══╝  ██║╚██╔╝██║██╔══██║██║██║         
		███████╗██║ ╚═╝ ██║██║  ██║██║███████╗    
		╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    		                                                                                                                                 
	"""  + END + BLUE +
	'\n' + 'Email sender'.format(RED, END).center(69) +
	'\n' + 'Made by: {}NUMB | NIRAJ'.format(YELLOW, RED, YELLOW, BLUE).center(76) +
	'\n' + 'Version: {}1.0{}\n'.format(YELLOW, END).center(80) + '\n')

	# hide the browser
	options = Options()
	options.add_argument('--headless')

	# Open the browser in background
	email_id = sys.argv[1]
	messages = ' '.join(sys.argv[2:])	
	browser = webdriver.Firefox( options = options)
	browser.get('https://www.gmail.com')

	# Find the text field for user email and send you stored in previous variable
	userEmail = browser.find_element_by_id("identifierId")
	userEmail.send_keys(user_email)

	# Click next button
	button_next = browser.find_element_by_id("identifierNext")
	button_next.click()

	sys.stdout.write(RED + " " * 20 + "Authenticating your email and password!")

	# sleep allows you to load your page completely if internet is slow
	time.sleep(5)

	# Find text field for user password and send keys on it.
	passwordElem = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/span/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
	passwordElem.send_keys(user_password)

	next_button = browser.find_element_by_id("passwordNext")
	next_button.click()

	time.sleep(5)
	
	# Compose the message at gmail page
	composeMessage = browser.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div")
	composeMessage.click()

	time.sleep(5)

	# Send keys for receiver email address through command line argument.
	emailElem = browser.find_element_by_xpath('//*[@id=":pu"]')
	emailElem.send_keys(email_id)

	sys.stdout.write(RED + "\n\n" + " " * 20 + "Finding your client: " + sys.argv[1])

	time.sleep(5)

	# Send messages
	messageBox = browser.find_element_by_xpath('//*[@id=":qh"]')
	messageBox.send_keys(messages)	

	sys.stdout.write(RED + "\n\n" + " " * 20 + "Sending message : " + ' '.join(sys.argv[2:]))

	time.sleep(5)

	# Click send button
	send_button = browser.find_element_by_xpath('//*[@id=":p2"]')
	send_button.click()

	sys.stdout.write(RED + "\n\n" + " " * 20 + "Message sent successfully\n\n.")
	

else:
	print("\n" + " " * 10 + "Usage:\n\t\t python3 <filename> <email address> <message>\n")
