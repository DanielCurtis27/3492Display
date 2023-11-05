import discord
import os
import time
import re
import art
import random
import asyncio
from colorama import Fore, Style
import pygame

client = discord.Client(intents=discord.Intents.all())

pygame.mixer.init()
pygame.mixer.music.load("buzzer.mp3")

#colors for the ascii art
class colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

#art used for the program
warning = '                                           ██                                          \n                                          ██░░██                                        \n                                        ██░░░░░░██                                  \n                                      ██░░░░░░░░░░██                                    \n                                      ██░░░░░░░░░░██                                    \n                                    ██░░░░░░░░░░░░░░██                                  \n                                  ██░░░░░░██████░░░░░░██                                \n                                  ██░░░░░░██████░░░░░░██                                \n                                ██░░░░░░░░██████░░░░░░░░██                              \n                                ██░░░░░░░░██████░░░░░░░░██                              \n                              ██░░░░░░░░░░██████░░░░░░░░░░██                            \n                            ██░░░░░░░░░░░░██████░░░░░░░░░░░░██                          \n                            ██░░░░░░░░░░░░██████░░░░░░░░░░░░██                          \n                          ██░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░██                        \n                          ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                        \n                        ██░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░██                      \n                        ██░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░██                      \n                      ██░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░██                    \n                      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                    \n                        ██████████████████████████████████████████                      \n                                                              '
checkmark = open('checkmark.txt', 'r')
screensaver1 = open('screensaver1.txt', 'r')
screensaver2 = open('screensaver2.txt', 'r')
screensaver3 = open('screensaver3.txt', 'r')
###


def screensaver_art():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    
    print('awaiting update...')

    randomd = random.randint(1, 5)
    
    match int(randomd):
        case 1:
            art.tprint('3492')
        case 2:
            print(f"{colors.YELLOW} {screensaver1.read()} {colors.ENDC}")
        case 3:
            print(f"{colors.BLUE} {screensaver2.read()} {colors.ENDC}")
        case 4:
            print(f"{Fore.YELLOW}{art.text2art('Orange','standard')}{Style.RESET_ALL}{art.text2art('&','standard')}{Fore.BLUE}{art.text2art('Blue','standard')}{Style.RESET_ALL}")
        case _:
            print(f"{colors.BLUE} {screensaver3.read()} {colors.ENDC}")
        


#initialization feedback
@client.event
async def on_ready():
    
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

    print('online')
    print(f"{colors.GREEN} {checkmark.read()} {colors.ENDC}")
    
    time.sleep(5)

    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    

@client.event
async def on_message(message):


    #find the message from the slack bot
    if str(message.channel) == 'upcoming-matches':
        if str(message.author.id) == '606618843959394324': #change to the slack bot
            
            if os.name == 'nt':
                os.system('cls')
            elif os.name == 'posix':
                os.system('clear')

            color = ''
            gametype = ''
            state = ''
            matchnumber = ''
            matchpos = ''

            #gives what the bot says
            manipmess = str(message.content)

            #this tells you what type of match it is (Qualification or Playoff)
            if 'Qualification' in manipmess:

                gametype = 'Qualification'

                matchnumber = re.search('Qualification [0-9]+', manipmess).group(0)

                if re.search('red [0-9]+', manipmess) != None:
                    matchpos = re.search('red [0-9]+', manipmess).group(0)
                elif re.search('blue [0-9]+', manipmess) != None:
                    matchpos = re.search('blue [0-9]+', manipmess).group(0)
            else:

                gametype = 'Playoff'

                matchnumber = re.search('Playoff [0-9]+', manipmess).group(0)

                if 'red' in manipmess:
                    matchpos = re.search('red alliance', manipmess).group(0)
                elif 'blue' in manipmess:
                    matchpos = re.search('blue alliance', manipmess).group(0)
                

            #team color
            if 'red' in manipmess:
                color = 'Red'
            elif 'blue' in manipmess:
                color = 'Blue'

            #state (how urgent will be indicated with an ascii warning sign)
            if 'Now queuing' in manipmess:
                state='Queuing'

            elif 'on deck' in manipmess:
                state='On Deck'

            if gametype != '' and state != '':
                if color != '': 
                    print("  {}  ||  {}  ||  {}  ".format(matchnumber,matchpos,state))
                else:
                    print("  {}  ||  {}  ".format(matchnumber,state))
                if state == 'Queuing':
                    print(f"{colors.YELLOW} {warning} {colors.ENDC}")

                    q = art.text2art('QUEUING', sep='\n                     ')
                    m = art.text2art(str(matchpos), sep='\n                     ')

                    print(f"                    {colors.YELLOW} {q} {colors.ENDC}")

                    if color == 'Red':
                        print(f"                    {colors.RED} {m} {colors.ENDC}")
                    else:
                        print(f"                    {colors.BLUE} {m} {colors.ENDC}")

                    pygame.mixer.music.play()
                    
                    await asyncio.sleep(240)
                    screensaver_art() 
                elif state == 'On Deck':
                    print(f"{colors.RED} {warning} {colors.ENDC}")

                    o = art.text2art('ON DECK', sep='\n                     ')
                    m = art.text2art(str(matchpos), sep='\n                     ')

                    print(f"                    {colors.RED} {o} {colors.ENDC}")

                    if color == 'Red':
                        print(f"                    {colors.RED} {m} {colors.ENDC}")
                    else:
                        print(f"                    {colors.BLUE} {m} {colors.ENDC}")
                    #add double horn
                    pygame.mixer.music.play()
                    await asyncio.sleep(3)
                    pygame.mixer.music.play()

                    await asyncio.sleep(240)
                    screensaver_art() 



#bot token
client.run('')




