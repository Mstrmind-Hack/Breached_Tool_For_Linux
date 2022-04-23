# Breached? Tool For Linux

**This tool will help you Discover if your E-mail Address or Username was involved in a data breach.**

**The tool will also show you the number of breaches (if any), the most recent breach (in terms of days/weeks/years), and some of the websites on which your E-mail/Username was breached (Keep in mind, other individuals might have the same username as you on sites you're not associated with).**

![banner](https://user-images.githubusercontent.com/104036615/164873023-3e8d85e0-7c25-427f-9f6d-aa4c7db92eda.png)

**Step 1)** Clone the tool to your machine (Kali, Arch, or any Linux Distro). For windows check: "https://github.com/Mstrmind-Hack/Email-Recon-For-Windows10/"

        >>git clone https://github.com/Mstrmind-Hack/Breached_Tool_For_Linux.git
       
**Step 2)** Change directories to the Breached Directory

        >>cd Breached

**Step 3)** Install the tool requirements.

        >>pip install -r requirements.txt
       
**Step 4)** Visit: https://leak-lookup.com/account/register and create a free **username and password** to access your **FREE API KEY**.

**Step 5)** Log-in to leak-lookup.com and optain your free API key. (Only 10 Searches allowed per day! Read their documentation!)

**Step 6)** Open Breached_Tool.py in a text editor and insert your API key in _**line 27**_ Between the quotation marks _**""**_ and save the file (See image below).

![KEY](https://user-images.githubusercontent.com/104036615/164873305-eccb8663-bfab-49b4-ae9d-552def09e8a7.png)

**Step 7)** Run the tool with: 

         >>python3 Breached_Tool.py
         OR
         >>python Breached_Tool.py

**Step 8)** Follow the prompts! It's that easy!

![banner1](https://user-images.githubusercontent.com/104036615/164873074-65cd8b82-827a-47ce-907e-cf6495be83d7.png)

![banner3](https://user-images.githubusercontent.com/104036615/164873192-2e16ebff-c4d7-4e4f-92f8-7ab8a263fc3e.png)

