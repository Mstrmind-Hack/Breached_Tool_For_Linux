#Libraries
import animation                                      #My animation file
import Banner1                                        #My logo
import os                                             #System commands
import requests                                       #Allows us to send request to the 2 api and web
from pprint import pprint                             #This helps print outputs nice (pretty print)    
from simple_colors import *                           #This helps with colors                                                    
from requests.structures import CaseInsensitiveDict   #Needed for the headers or our second API


#IF false the tool does not work

active = True

while active:
    
    print(yellow("\n\tSelect from the Choices Below (Quit = q)"))
    
    print(blue("\n\t[1] - Was my E-mail Breached?"))
    
    print(blue("\n\t[2] - Was my Username Breached?"))
    
    #This API Key is for the second website, it finds breached locations

    API_KEY = "" #<============= API Key for leak-loopup goes here
    
    pick = input(green("\n\tSelect: 1 or 2? "))
    
    if pick == 'q':
        
        os.system('clear')
        
        print(yellow("\n\tGoodBye!!!"))
        
        print("\n")

        break 

    ##---------------------------------EMAIL VERIFICATION PORTION-------------------------------------#    

    if pick == '1':
        
        os.system('clear')

        message = input(green("\n\n\tEnter Your E-mail address: "))
        
        note = print(yellow("\n\t Enter 'q' to quit"))
        
        print(yellow(f"\n\t Verify E-mail, Is this correct?"))
        
        print(green(f"\n\t E-mail: {message}"))
       
        print("\t\t________________________")
        
        act1 = input(green( "\n\t (y / n)? "))

        
       ##---------------------------------FIRTS API NUMBER OF BREACHES AND MOST RECENT TIME-------------------------------------#


        if act1 == 'y':
           
           os.system('clear')
           
           print(green("\n\tSearching..."))
                    
           response = requests.get(f"https://portal.spycloud.com/endpoint/enriched-stats/{message}")
           
           os.system('clear')
           
           print(yellow("\t ######################################################"))
           
           print(green(f"\t\tRESULTS Found for {message}"))

           ##---API STATUS CHECKER---##
           
           #res = response.status_code
           
           #print(green(f"\t\t\t      {res}"))
 
           print(yellow("\t ######################################################"))
           
           pretty = response.json()           
           
           print(yellow("\n\tNumber of Breach Records   |    Last Breach Discovered"))
           
          
           print(blue("\n======================================================================================")) 

           print(green(f"[!] Findings!: {pretty['you']}"))

           print(blue("======================================================================================"))
       
           print(red("\n\n More Searching..."))
           
          ###ANOTHER API BELOW THIS COMMENT###


          ##---------------------------------SECOND API EMAIL LOCATOR PORTION-------------------------------------#

          
           url = "https://leak-lookup.com/api/search"

           headers = CaseInsensitiveDict()
           
           headers["Content-Type"] = "application/x-www-form-urlencoded"


           ##--Go to URL https://leak-lookup.com/api/search and create a username/password--##

           ##-------Here we imput our AIP key V--------##
           

           data = f"key={API_KEY}&type=email_address&query={message}"

           response = requests.get(url, headers=headers, data=data)

           r_variable = response.json()
          

           print(blue("\n\n======================================================================================"))

           print(green(f"[!] Findings!: These Are Some Web Locations Where: {message} Was Breached"))

           print("\n")
           
           pprint(r_variable['message'], indent=25)

           print(blue("======================================================================================"))
           
           print("\n")

           break
       
        if act1 == 'q':
            
            os.system('clear')
            
            print("\n\tGoodBye!!!")

            print("\n")
            
            break


   ##---------------------------------EMAIL VERIFICATION SECOND PORTION-------------------------------------#

    
    if pick == '2':
      
      os.system('clear')

      message1 = input(green("\n\n\tEnter A Username: "))
      
      os.system('clear')

      print(green("\n\tSearching..."))

      url = "https://leak-lookup.com/api/search"

      headers = CaseInsensitiveDict()
      
      headers["Content-Type"] = "application/x-www-form-urlencoded"


     ####---------------------------------USERNAME PORTION-------------------------------------####

      ##--Go to URL https://leak-lookup.com/api/search and create a username/password--##

      ##-------Here we imput our AIP key V--------##


      data = f"key={API_KEY}&type=username&query={message1}"

      response = requests.get(url, headers=headers, data=data)

      r_variable = response.json()

      os.system('clear')
      
     
      print(yellow("\t ######################################################"))
           
      print(green(f"\t\t\tRESULTS Found for {message1}"))
      
      print(yellow("\t ######################################################"))
      
     
      print(blue("======================================================================================"))

      print(yellow(f"\tThese Are Some Websites on Which the Username: {message1} Was Breached."))

      print("\n")

      pprint(r_variable['message'], indent=25)   
      
      print(blue("======================================================================================"))

      print("\n")

      break

    else:
        
        os.system('clear')
        
        print(red("\n\t----------Select The Correct Choice and Try Again----------"))             

####_____________________________END________________________________________________________####
