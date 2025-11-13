import feedparser
import os
from datetime import datetime

# fetch RSS feed from Yle.fi kotimaa sector and write the latest 10 entries to a file
RSS_FEED_URL = "https://yle.fi/rss/t/18-34837/fi"

feed = feedparser.parse(RSS_FEED_URL);
home = os.environ['HOME']
output_file_path = home + "/public_html/yle_fi_rss.txt"

with open(output_file_path, "w", encoding="utf-8") as f:
  for entry in feed.entries[:10]:
    title = entry.title.replace("\n"," ");
    link = entry.link;
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S");
    f.write(f"{time};{title};{link}\n");



