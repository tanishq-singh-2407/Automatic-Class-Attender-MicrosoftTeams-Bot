from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from discord_webhook import DiscordWebhook, DiscordEmbed
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import schedule
import re
import time
import sys
from datetime import datetime

options = Options()
options.add_argument("start-maximized")
options.add_argument("--start-maximized")

options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.notifications": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.geolocation": 0
  })

driver = None

URL = "https://teams.microsoft.com"

userName = 'ENTER YOUR EMAIL ID'
webhookUrl = 'ENTER YOUR WEBHOOK URL TOKEN'
userPassword = 'ENTER YOUR PASSWORD'


def sendMessage(currentTask, body, nextTask):
    webhook = DiscordWebhook(url = webhookUrl, username = "Microsoft Teams")

    embed = DiscordEmbed(
                            title = currentTask,
                            description = body,
                            color = 0x546e7a
    )
    embed.set_author(
                        name = "By Tanishq Singh",
                        icon_url = "https://avatars.githubusercontent.com/u/76192403?s=460&u=b8fade49d1999d6a19e14326c31ee24f79b5d6c4&v=4",
    )
    embed.set_footer(text = nextTask)
    embed.set_timestamp()
    webhook.add_embed(embed)

    response = webhook.execute()

def validate_input(regex,inp):
	if not re.match(regex,inp):
		return False
	return True

# Adding class
def addClasses():

    # Input class name
    className = input("\n\n\nEnter class name : ")

    # Input subject teacher name
    teacherName = input('\nEnter subject teacher name : ')

    # Input class start time
    startTime = input("\nEnter " + className + " class start time in 24 hour format (HH:MM) : ")

    # Re-entering class start time
    while not(validate_input("\d\d:\d\d",startTime)):
        print("\nInvalid input, try again")
        startTime = input("Enter " + className + " class start time in 24 hour format (HH:MM) : ")

    # Input class end time
    endTime = input("\nEnter " + className + " class end time in 24 hour format (HH:MM) : ")

    # Re-entering class end time
    while not(validate_input("\d\d:\d\d",endTime)):
        print("\nInvalid input, try again")
        endTime = input("Enter " + className + " class end time in 24 hour format (HH:MM) : ")

    # Options -> weather to start or quit
    options = input('\n\n\nChoose : \n\n     1 : Start \n     2 : Quit \n\nEnter : ')

    # If choose start
    if options == '1':
        sendMessage('The bot is started', 'Class : ' + className + "\nTeacher's Name : " + teacherName + '\nStart Time : ' + startTime + '\nEnd Time   : ' + endTime, 'Logging started')
        # Processing the tast
        startBrowser(className,teacherName,startTime,endTime)

    # If choose quit
    elif options == '2':
        # Bye bye tata khatam
        print('\nThank you for using ; )')

# Leaving class
def leaveClass(className):
    global driver

    driver.find_element_by_class_name("ts-calling-screen").click()


    driver.find_element_by_xpath('//*[@id="teams-app-bar"]/ul/li[3]').click()
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="hangup-button"]').click()

    print('\nClass leaved')
    # Going back to home page
    # Going to calendar page
    time.sleep(10)
    sendMessage('Class Leaved Status', 'The ' + className + ' class has been leaved successfully.', 'Quitting the browser')
    calendarButton = driver.find_element_by_xpath('//*[@id="app-bar-ef56c0de-36fc-4ef8-b417-3d82ba9d073c"]')
    calendarButton.click()

    driver.quit()
    sendMessage('Browser Quitted Status', 'The browser has been quitted successfully', 'Waiting for the program to end')

    waitingForTheTime('END_THE_PROGRAM','END_THE_PROGRAM','00:00','00:00')


# Did the class end.?!
def didClassEnd(className,teacherName,startTime,endTime):
    hm = "%H:%M"

    # Finding the class time
    classTime = datetime.strptime(endTime,hm) - datetime.strptime(startTime,hm)

    # Waiting for the class to end
    time.sleep(classTime.seconds)

    # Leaving class
    print('\nLeaving the class')
    leaveClass(className)

# Waiting for the class
def waitingForTheTime(className,teacherName,startTime,endTime):
    schedule.every().day.at(startTime).do(joinClass,className,teacherName,startTime,endTime)

    _running = 1
    # Loop so that the scheduling task
    # keeps on running all time.
    while _running == 1:

        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(0.5)
        print('Waiting..')

        if className == 'END_THE_PROGRAM' and teacherName == 'END_THE_PROGRAM' and startTime == '00:00' and endTime == '00:00':
            _running = 0

    print('Schedule loop breaked')
    sendMessage('Schedule loop breaked', 'The program has been successfully ended.', '-- Noting')

# Joining the class
def joinClass(className,teacherName,startTime,endTime):
    global driver

    # Clicking the join button
    print('Joining the class')
    joinButton = driver.find_element_by_xpath('/html/body/div[8]/div/div/div/div[3]/div/div/div[1]/div[2]/div[3]/button[1]')
    joinButton.click()

    # Checking if webcam and micphone is off
    time.sleep(1)
    print('\nTurning off the web cam and mic')
    webcam = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]')
    if(webcam.get_attribute('title')=='Turn camera off'):
        webcam.click()
        time.sleep(1)

    microphone = driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]')
    if(microphone.get_attribute('title')=='Mute microphone'):
        microphone.click()

    # Joining the class
    print('\nJoining the class')
    joinNowbutton = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    joinNowbutton.click()

    sendMessage('Class Joined Status', 'The ' + className + ' class has been joined successfully.', 'Waiting for the class to get over')
    # Did the class end.?!
    didClassEnd(className,teacherName,startTime,endTime)

# Searching for classes
def searchingForClasses(className,teacherName,startTime,endTime):
    global driver

    # Classes available
    classesAvailable = driver.find_elements_by_class_name("node_modules--msteams-bridges-components-calendar-grid-dist-es-src-renderers-calendar-multi-day-renderer-calendar-multi-day-renderer__eventCard--3NBeS")

    # Searching
    for i in classesAvailable:
        # If searched the class by class name and teacher name
        if className.lower() in i.get_attribute('innerHTML').lower() and teacherName.lower() in i.get_attribute('innerHTML').lower():
            # Printing searched
            print(className, 'class searched')
            i.click()

            # Joining class
            sendMessage('Class searched', 'The respective ' + className + ' class has been searched, and now waiting for ' + startTime + ', to join the class.', 'Waiting for ' + startTime)
            print('\nWaiting for the class time')
            waitingForTheTime(className,teacherName,startTime,endTime)

            # breaking the loop
            break

# Switching To Day Schedule
def switchingToDaySchedule(className,teacherName,startTime,endTime):
    global driver

    for i in range(101):
        sys.stdout.write('\r')
        sys.stdout.write("[%-100s] %d%%" % ('='*i, 1*i))
        sys.stdout.flush()
        time.sleep(0.6)

    calendarButton = driver.find_element_by_xpath('//*[@id="app-bar-ef56c0de-36fc-4ef8-b417-3d82ba9d073c"]')
    calendarButton.click()

    time.sleep(15)
    switchingToDayTasks = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/div/calendar-bridge/div/div/div[2]/div/div/div/div/div[2]/div[2]/button')
    switchingToDayTasks.click()

    time.sleep(10)
    daySelected = driver.find_element_by_xpath('//*[@id="id__16-menu"]/div/ul/li[1]/button')
    daySelected.click()



    # Searching for classes
    print('\nSearching for classes')
    searchingForClasses(className,teacherName,startTime,endTime)

# Login program
def login(className,teacherName,startTime,endTime):
    global driver

    # Entering email id
    time.sleep(2)
    print('\nEntering email id')
    enteringEmailId = driver.find_element_by_xpath('//*[@id="i0116"]')
    enteringEmailId.click()
    enteringEmailId.send_keys(userName)

    # Going fowrard
    print('\nGoing fowrard')
    time.sleep(5)
    nextButtonForPasswordPage = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
    nextButtonForPasswordPage.click()

    # Entering password
    print('\nEntering password')
    time.sleep(5)
    enteringPassword = driver.find_element_by_xpath('//*[@id="i0118"]')
    enteringPassword.click()
    enteringPassword.send_keys(userPassword)

    # Remenber the login.?!
    print('\nRemenber the login.?!')
    time.sleep(2)
    nextButtonForRememberingPage = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
    nextButtonForRememberingPage.click()

    # Going forward towards home page
    print('\nGoing forward towards home page')
    time.sleep(2)
    nextButtonForHomePage = driver.find_element_by_xpath('//*[@id="idBtn_Back"]')
    nextButtonForHomePage.click()

    sendMessage('Login task', 'Login successful\n\nEmail Id     : ' + userName + '\nPassword  : ' + userPassword + '\n', '\nSwitching to day view in calendar')
    # Switching to day schedule
    print('\nSwitching to day schedule')
    switchingToDaySchedule(className,teacherName,startTime,endTime)


# Starting the browser
def startBrowser(className,teacherName,startTime,endTime):
    global driver

    print('\nOpening Browser')
    # Driver == Chrome
    driver = webdriver.Chrome("C:/chromedriver.exe", chrome_options = options)

    # Opening teams
    driver.get(URL)

    # Login
    print('\nLoging')
    login(className,teacherName,startTime,endTime)


# Starting point of the code
if __name__ == '__main__':
    # Adding just one class
    addClasses()
