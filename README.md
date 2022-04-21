# Email-Recon-For-Linux

**This tool will help you Discover if your E-mail Address or Username was involved in a data breach**

**The tool will also show you the amount of breaches (if any), the most resent breach (in terms of days/weeks/years), and some of the websites that your E-mail/Username was breached (other individuals might have the same username as you on a different site you are not a part off)**

![banner1](https://user-images.githubusercontent.com/104036615/164146591-46791c12-e742-46ab-925f-e7620011b263.png)


**Step 1)** Clone the tool to your machine (Kali, Arch, or any Linux Distro). For windows check: "https://github.com/Mstrmind-Hack/Email-Recon-For-Windows10/"

        >>git clone https://github.com/Mstrmind-Hack/Email-Recon.git
       
**Step 2)** Change directories to the Email-Recon Directory

        >>cd Email_Recon

**Step 3)** Install the tool requirements.

        >>pip install -r requirements.txt
       
**Step 4)** Visit: https://leak-lookup.com/account/register and create a free **username and password** to access your **API KEY**.

**Step 5)** Log-in to leak-lookup.com and optain your free API key. (Only 10 Searches allowed per day! Read their documentation!)

**Step 6)** Open E_Recon_Tool.py in a text editor and insert your API key in _**line 24**_ Between the quotation marks _**""**_ and save the file (See image below).

![Screenshot (25)](https://user-images.githubusercontent.com/104036615/164343846-ea1a1f4c-25ce-4b2f-9cd7-cd2b4079f97c.jpg)

**Step 7)** Run the tool with: 

         >>python3 E_Recon_Tool.py
         OR
         >>python E_Recon_Tool.py

**Step 8)** Follow the prompts! It's that easy!

![banner](https://user-images.githubusercontent.com/104036615/164146375-a389cc37-4ad2-43bd-aac2-0a46d537d610.png)

![banner3](https://user-images.githubusercontent.com/104036615/164147248-8e8edc9c-51bb-4c0e-a2f7-9f34566fa654.png)

