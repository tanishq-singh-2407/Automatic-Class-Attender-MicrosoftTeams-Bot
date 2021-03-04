# Automatic Class Attender MicrosoftTeams Bot
* This is a bot that automate the process of attending the online classes automatically.
---
## What problem does this bot solve .?!
* After submitting your next class details like class name, teacher's name, class start time, and lastly class end time. This bot automatically open your browser and make the login
(Do not remember) then after 60 second it opens the calendar and shift to day view from there it searches for the class by class name and teacher's name and it wait for time class
time and at the given time it joins the class, also before joining the class it make sure that your webcam and mic is turned off, and then at the given end time the bot leaves the class
and lastly after 20 seconds it closes the browser.

* This help the user to save time rather just sitting in the class and using social media.
* This is a better or modern way for bunking the class, as we know modern problems require
modern solution.
---

# How to setup, accourding to your needs.?
#### 1. Download the zip file, and then extract it.
![Zip download image](https://github.com/tanishq-singh-2301/test/blob/master/MicrosoftTeams-Bot/download.PNG)
#### 2. Find the version of your chrome browser (Setting > About Chrome)
#### 3. [Download](https://chromedriver.chromium.org/downloads) the chromedriver.exe file accourding to your browser version and paste the chromedriver.exe file in the C:/ drive, like this
![pasting the chromedriver.exe file in C:/drive image](https://github.com/tanishq-singh-2301/test/blob/master/MicrosoftTeams-Bot/setup-chromedriver.PNG)
#### 4. Setting up the main.py accourding to your needs.
* Enter your email id inside single inverted commas. (29th line)
````python
userName = 'ENTER YOUR EMAIL ID' # for example userName = 'example123@example.com'
````
* Enter your webhook url. (30th line)
````python
webhookUrl = 'ENTER YOUR WEBHOOK URL TOKEN'
````
### Discord Message (in realtime as the bot works)

| <img src="https://github.com/tanishq-singh-2301/test/blob/master/MicrosoftTeams-Bot/dis-msg-1.PNG" alt="Discord message image" width="65%" /> | <img src="https://github.com/tanishq-singh-2301/test/blob/master/MicrosoftTeams-Bot/dis-msg-2.jpg" alt="Discord message image" width="65%"/>
| --- | --- |
* If you don't have any webhook url neither you have a discord account.
* Then you ethier make a discord account or comment sendMessage(): code (from 35th line to 50th line), like this

    * Before commenting

    ````python
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
    ````
    * After commenting

    ````python
    def sendMessage(currentTask, body, nextTask):
    #    webhook = DiscordWebhook(url = webhookUrl, username = "Microsoft Teams")
    #
    #    embed = DiscordEmbed(
    #                            title = currentTask,
    #                            description = body,
    #                            color = 0x546e7a
    #    )
    #    embed.set_author(
    #                        name = "By Tanishq Singh",
    #                        icon_url = "https://avatars.githubusercontent.com/u/76192403?s=460&u=b8fade49d1999d6a19e14326c31ee24f79b5d6c4&v=4",
    #    )
    #    embed.set_footer(text = nextTask)
    #    embed.set_timestamp()
    #    webhook.add_embed(embed)
    #
    #    response = webhook.execute()
    ````

* Enter your password inside single inverted commas. (31th line)
````python
userPassword = 'ENTER YOUR PASSWORD' # for example userPassword = 'Example123'
````
---
### Software installation
````windows
pip install selenium
pip install discord-webhook
pip install schedule
pip install discord.py
````
---
### Running the program
````windows
python main.py
````
---
