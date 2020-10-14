# 1. create a new folder

# 2. open your terminal and cd to that folder

# 3. setup a python venv and install beautifulsoup4 and requests:
#    pip install beautifulsoup4
#    pip install requests

# 4. add the following code to a new file named generate_link_list.py

from bs4 import BeautifulSoup
import requests

limit = 10  # retrieve the first 10 links
url = 'https://en.wikipedia.org/wiki/List_of_works_by_Vincent_van_Gogh'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
links = []
links_list = []
error_log = []

for link in soup.select('.wikitable .image'):
    links.append(link['href'])

for media_page in links[0:limit]:
    req = requests.get('https://en.wikipedia.org' + media_page)
    soup = BeautifulSoup(req.text, 'html.parser')
    img_div = soup.find('div', {'class': 'mw-filepage-resolutioninfo'})  # you can change this for different size images
    try:
        img_path = 'https:' + img_div.find('a')['href']
        links_list.append(img_path)
        print(img_path)
    except:
        failed_msg = "couldn't add link for: " + media_page
        error_log.append(failed_msg)
        print(failed_msg)

txt_file = open('download.txt', 'w')
for line in links_list:
     txt_file.write(line)
     txt_file.write('\n')
txt_file.close()

error_file = open('errors.txt', 'w')
for line in error_log:
     error_file.write(line)
     error_file.write('\n')
error_file.close()

# 5. run the script using: python3 generate_link_list.py

# 6. once complete, the download.txt file will contain all of the links; check the error_log to see what failed

# if you want to download the images, use: xargs -n 1 curl -O < download.txt

# beautifulsoup documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/