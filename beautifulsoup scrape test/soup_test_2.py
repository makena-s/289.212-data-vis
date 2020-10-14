from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_subgroups_of_the_order_Coleoptera'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

buglist = []
namecounter = 0
limit = 10

#----- get links
#wholelist = soup.find('li')
#
#for page in wholelist.find_all('a'):
#    buglist.append(page['href'])
#print(buglist)
#
#txt_file = open('buglinks.txt', 'w')
#for line in buglist:
#     txt_file.write(line)
#     txt_file.write('\n')
#txt_file.close()
#-----

#----- get names of links
#for name in wholelist.find_all('a'):
#    buglist.append(name.text)
#    namecounter += 1
#    print(name)
#
#print(buglist)
#print(namecounter)
#
#txt_file = open('buglist.txt', 'w')
#for line in buglist:
#     txt_file.write(line)
#     txt_file.write('\n')
#txt_file.close()
#-----

print('YEEHAW! DONE!')