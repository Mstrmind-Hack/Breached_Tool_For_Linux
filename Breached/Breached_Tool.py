#Libraries
import os                                             #System commands
import time                                           #Allows us to add timed pause and sleep sessions
import json                                           #Allows us to work with json 
import requests                                       #Allows us to send request to the 2 api and web
import animation                                      #My animation file
import Banner1                                        #Our Banner logo
from simple_colors import *                           #This helps with colors 
from API_KEY import API_KEY                           #This calls The API_KEY File and imports the key to this program                                                         
from requests.structures import CaseInsensitiveDict   #Needed for the headers for our second API

#If false the tool does not work

active = True

while active:
    
    print(yellow("\n\tSelect from the Choices Below",['bright','underlined']))    
    print(magenta("\n\t[ 1] Was my E-mail Breached?",['bright']))
    print(magenta("\t[ 2] Was my Username Breached?",['bright']))
    print(blue("\t[-q] Quit",['bright']))
    
    pick = input(red("\n\t[brchd2][menu] >> ", ['bold', 'bright']))
    os.system('clear')
    
    if pick == '-q':
        os.system('clear')
        
        print(green("\n\tExiting...", ['bright']))
        print("\n")
        
        time.sleep(1) #sleep for 2 seconds
        
        os.system('clear')
        
        break

##---------------------------------EMAIL VERIFICATION PORTION-------------------------------------#    

    if pick == '1':
        os.system('clear')

        print(blue("\n\t###################################", ['bright']))
        print(green("\t     Enter Your E-Mail Address",['bold', 'bright']))
        print(blue("\t###################################", ['bright']))

        print(yellow("\n\t [-q] Quit", ['bright']))

        message = input(red("\n\t [brchd2][Email Input] >> ", ['bold', 'bright']))

        if message == '-q':
            os.system('clear')
            
            print(green("\n\tExiting...", ['bright']))
            print("\n")
            
            time.sleep(1) #sleep for 1 seconds
            
            os.system('clear')
            
            break
        else:
            False
        
        os.system('clear')

        print(blue("\n\t###################################", ['bright']))
        print(green("\t     Verify E-Mail Address",['bold', 'bright']))
        print(blue("\t###################################", ['bright']))
             
        print(cyan(f"\n\t [!] E-mail:", ['bright']))
        print(yellow(f"\t\t--> {message}?", ['bright']))
        print(green(f"\n\t [!] Is this correct? [y / n / -q]", ['bright']))
        
        act1 = input(red("\n\n\t[brchd2][Email Verify] >> ", ['bold', 'bright']))
        
       ##---------------------------------FIRST API NUMBER OF BREACHES AND MOST RECENT TIME-------------------------------------#

        if act1 == 'y':          
           os.system('clear')
           
           print(green("\n\t Searching...", ['blink', 'bright']))
                    
           response = requests.get(f"https://portal.spycloud.com/endpoint/enriched-stats/{message}")
           
           os.system('clear')
           
        ##---------API 1 STATUS CHECKER---------##
           
           #res = response.status_code
           
           #print(green(f"\t\t\t      {res}"))

        ##---------END of API 1 STATUS CHECKER---------##

        ##---------Response Key and Variable---------##
           
           package = response.json()           
           
           package_records = package["you"]['records']
           
           package_discovered = package["you"]['discovered']

           package_discover_units = package["you"]['discovered_unit']

        ##---------Response Key Printting ---------##

           package_str_r = json.dumps(package_records, indent = 2)

           package_str_d = json.dumps(package_discovered, indent = 2)

           package_str_du = json.dumps(package_discover_units, indent = 2)

           print(red("\n\t Searching...This Might Take Some Time...",['bright','blink']))

        ##---------------------------------SECOND API EMAIL LOCATOR PORTION-------------------------------------#
          
           url = "https://leak-lookup.com/api/search"

           headers = CaseInsensitiveDict()
           
           headers["Content-Type"] = "application/x-www-form-urlencoded"


        ##--Go to URL https://leak-lookup.com/api/search and create a username/password--##

        ##-------Here we imput our AIP key V--------##
           

           data = f"key={API_KEY}&type=email_address&query={message}"

           response = requests.get(url, headers=headers, data=data)

           r_variable = response.json()

           print(green("\n\t Searching...", ['blink', 'bright']))

           os.system('clear')

           print(blue("\n\t##################################################", ['bright']))
           print(green(f"\t     Results For: {message}",['bold', 'bright']))
           print(blue("\t##################################################", ['bright']))

           ##--- PRINTING RESULTS From First API ---##

           print(green(f"\n\t [!] Number of Breaches:", ['bright']))
           print(red(f"\t\t --> {package_str_r}", ['bright']))
           print(green(f"\n\t [!] The Most Recent Breach Occurred: ", ['bright']))
           print(red(f"\t\t --> {package_discovered} {package_str_du} ago", ['bright']))

           ##--- PRINTING RESULTS From Second API ---##
        
           print(green(f"\n\t [!] Some Web Locations Where: {message} Was Breached", ['bright']))
           
           for item in r_variable['message']:
                if item:
                    print(red(f"\t\t --> {item}", ['bright']))
                else:
                    False          
           print(blue("\t================= END OF RESULTS ==================", ['bright'])) 
  
        elif act1 == 'n':
            os.system('clear')       
       
        elif act1 == '-q':
            os.system('clear')
            
            print(green("\n\tExiting...", ['bright']))
            print("\n")
           
            time.sleep(1) #sleep for 3 seconds
            
            os.system('clear')
            
            break
        
        else:
            print(red(f"\n\t[!] Input: '{act1}' is not recognized. Please try again.", ['bright']))

   ##--------------------------------- BREACHED USERNAME SEARCH PORTION -------------------------------------#
    
    if pick == '2':
      os.system('clear')

      print(blue("\n\t###################################", ['bright']))
      print(green("\t     Enter A Username:",['bold', 'bright']))
      print(blue("\t###################################", ['bright']))

      message1 = input(red("\n\n\t[brchd2][Username] >> ", ['bold', 'bright']))

      print(green("\n\t Searching...", ['blink', 'bright']))
      
      os.system('clear')

      print(red("\n\t Searching...This Might Take Some Time...",['bright','blink']))

      url = "https://leak-lookup.com/api/search"

      headers = CaseInsensitiveDict()
      
      headers["Content-Type"] = "application/x-www-form-urlencoded"

      data = f"key={API_KEY}&type=username&query={message1}"

      response = requests.get(url, headers=headers, data=data)

      r_variable = response.json()

      os.system('clear')
     
      print(blue("\t ######################################################", ['bright']))         
      print(green(f"\t\t\tRESULTS Found for {message1}", ['bright']))
      print(blue("\t ######################################################", ['bright']))

      print(green(f"\n\t [!] Some Websites Where the Username: {message1} Was Breached.", ['bright']))

      for item in r_variable['message']:
        if item:
            print(red(f"\t\t --> {item}", ['bold','bright']))
        else:
            False          
      
      print(blue("\t================= END OF RESULTS ==================", ['bright']))      

    else:    
        False
                    

####_____________________________END________________________________________________________####
