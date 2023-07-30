# Playstore-auto-ratings-with-multiple-account
Playstore auto ratings with multiple account using localhost

"𝙏𝙝𝙚𝙨𝙚 𝙨𝙘𝙧𝙞𝙥𝙩𝙨 𝙮𝙤𝙪 𝙙𝙞𝙙𝙣'𝙩 𝙛𝙞𝙣𝙙 𝙞𝙣 𝙖𝙣𝙮 𝘼𝙄"

𝙉𝙤𝙩𝙚:𝘿𝙞𝙙𝙣'𝙩 𝙘𝙤𝙥𝙮-𝙥𝙖𝙨𝙩𝙚 𝙘𝙤𝙙𝙚 𝙖𝙜𝙖𝙞𝙣 𝙖𝙣𝙙 𝙖𝙜𝙖𝙞𝙣 𝙎𝙤𝙢𝙚 𝘾𝙝𝙖𝙣𝙜𝙚𝙨 𝘼𝙧𝙚 𝙏𝙝𝙚𝙧𝙚.

## "If you know proxy rotation, then please fork it".

https://www.youtube.com/watch?v=FVumnHy5Tzo&t=1s&ab_channel=HelloWorld

#Watch up to 3 minutes and 46 seconds, and then remain in the remaining part copying the part of the script and save it as l.py. The script is used to automatically like a particular YouTube video with multiple accounts

First, open Chrome file location and bypass the location restriction using an extension such as Touch VPN. In my case, the Chrome location(use start in: path) is

C:\Users\Hp\AppData\Local\Google\Chrome\Application

Next, in the command prompt, navigate to the Chrome directory using the command cd C:\Users\Hp\AppData\Local\Google\Chrome\Application

Then,

use the command

chrome.exe --remote-debugging-port=9222 --user-data-dir="enter your localhost path here"

to open Chrome with remote debugging enabled. In my case, the command was

chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\Hp\Desktop\Bots\Chromedriver\Localhost"

then new terminal in that folder and enter playstore.py

## in code replace 24 and 39 line with with app name and text you want to submit replace in below code also where its asked.

After opening Chrome, paste the following two lines of code from the script into the command prompt and hit enter. This will open the Play Store in Chrome, automatically rate, and submit

After completing one process, switch to another account and repeat the same process. If you need to perform this script with more accounts, simply add the code at the end to enable logging in with another account

Finally, in the command prompt, enter "pip install Random" and hit enter to install the necessary library.

👉Note:-

👉If you have the latest version of Selenium, the code may not run

👉open cmd and enter pip uninstall selenium

And enter

pip install selenium==4.2.0

and hit enter

and

python -c "import selenium; print(selenium.version)"

𝙏𝙝𝙞𝙨 𝙞𝙣𝙛𝙤𝙧𝙢𝙖𝙩𝙞𝙤𝙣 𝙞𝙨 𝙤𝙣𝙡𝙮 𝙛𝙤𝙧 𝙚𝙙𝙪𝙘𝙖𝙩𝙞𝙤𝙣al 𝙥𝙪𝙧𝙥𝙤𝙨𝙚 𝙖𝙣𝙙 𝙬𝙚 𝙖𝙧𝙚 𝙣𝙤𝙩 𝙧𝙚𝙨𝙥𝙤𝙣𝙨𝙞𝙗𝙡𝙚 𝙛𝙤𝙧 𝙖𝙣𝙮 𝙠𝙞𝙣𝙙 𝙤𝙛 𝙞𝙡𝙡𝙚𝙜𝙖𝙡 𝙖𝙘𝙩𝙞𝙫𝙞𝙩𝙮 𝙙𝙤𝙣𝙚 𝙗𝙮 𝙩𝙝𝙞𝙨 𝙩𝙤𝙤𝙡.
