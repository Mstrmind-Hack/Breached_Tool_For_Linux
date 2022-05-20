# Breached? Tool For Linux
![ezgif com-gif-maker(1)](https://user-images.githubusercontent.com/104036615/169430789-27f6638d-7106-43ae-b065-b266c5396523.gif)

**UPDATED VERSION 2!**

**This tool will help you Discover if your E-mail Address or Username was involved in a data breach.**

**The tool will also show you the number of breaches (if any), the most recent breach (in terms of days/weeks/years), and some of the websites on which your E-mail/Username was breached (Keep in mind, other individuals might have the same username as you on sites you're not associated with).**

**Step 1)** Clone the tool to your machine (Kali, Arch, or any Linux Distro). For windows check: "https://github.com/Mstrmind-Hack/Breached-For-Windows10/"

        >>git clone https://github.com/Mstrmind-Hack/Breached_Tool_For_Linux.git
       
**Step 2)** Change directories to the Breached Directory

        >>cd Breached

**Step 3)** Install the tool requirements.

        >>pip install -r requirements.txt
       
**Step 4)** Visit: https://leak-lookup.com/account/register and create a free **username and password** to access your **FREE API KEY**.

**Step 5)** Log-in to leak-lookup.com and optain your free API key. (Only 10 Searches allowed per day! Read their documentation!)

**Step 6)** Open API_KEY.py in a text editor and insert your API key in _**line 4**_ Between the quotation marks _**""**_ and save the file (See image below).

![api](https://user-images.githubusercontent.com/104036615/167968288-63798af3-7796-47a1-a77c-4e22a78ea899.png)

**Step 7)** Run the tool with: 

         >>python3 Breached_Tool.py
         OR
         >>python Breached_Tool.py

**Step 8)** Follow the prompts! It's that easy!

| API | Key Needed?|
|-----|------|
|1) portal.spycloud.com|No|
|2) leak-lookup.com| Yes|


