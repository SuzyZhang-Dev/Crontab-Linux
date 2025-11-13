📄 README – RSS News Fetcher with Crontab & Web Interface

1. Overview

This project demonstrates how to use Python, crontab, HTML, CSS, and JavaScript to automatically fetch news from an external RSS feed (Yle.fi) and display them on a web page hosted on a Linux virtual machine.

The Python script fetches the 10 latest news headlines from an RSS feed and saves them to a text file inside the user’s public_html directory.
A scheduled cron job runs the script regularly.
The index.html page reads the text file using JavaScript (fetch()) and displays the news in a formatted table.

2. Folder Structure
```
~/public_html/
│── index.html
│── style.css
│── script.js
│── yle_fi_rss.txt     ← generated automatically by cron + Python
```

Python script is located in:
```
~/fetch_rss.py
``` 

3. Python Script (fetch_rss.py)
## Description
	•	Fetches RSS feed from Yle Kotimaa category
	•	Extracts the latest 10 news items
	•	Saves timestamp, title, and link to a text file
	•	Overwrites previous content to keep the file clean

4. Crontab Configuration
## Description
The cron job runs the Python script every 5 minutes to keep the news updated.

### Edit crontab
Run:
```
crontab -e
```
Add this line
```
*/5 * * * * /usr/bin/python3 /home/student/fetch_rss.py
```

#### Make sure:
	•	Python path (/usr/bin/python3) is correct
	•	Your username replaces student if different
	•	Script has execute permission:

```
chmod +x ~/fetch_rss.py
```


5. How the System Works
	1.	Cron triggers the Python script every 5 minutes
	2.	Script fetches RSS feed from Yle.fi
	3.	Script generates ~/public_html/yle_fi_rss.txt
	4.	Browser opens index.html
	5.	JavaScript reads the text file via fetch()
	6.	Data is formatted into a table
	7.	Updated news appear automatically

6. Requirements
	•	Linux VM
	•	Apache or similar web server supporting public_html
	•	Python 3
	•	feedparser library
  •	Working crontab service
```
pip install feedparser --user
```

7. Example URL
```
http://<yourip>/~<yourVMuser>/index.html
```

