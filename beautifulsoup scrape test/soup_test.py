from bs4 import BeautifulSoup
import requests

# to get the names of the different suborders

url = 'https://en.wikipedia.org/wiki/List_of_subgroups_of_the_order_Coleoptera'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')



#results = soup.find('h1')
#
#print(results.text)
#print('YEEHAW! done!')


orders = []
suborders = []
superfamilies = []
families = []
counter = 0

wholelist = soup.find('li')

for order in wholelist.find('li'):
    superfamilies.append(order.find('a'))
print(superfamilies)


#--------------
#findorders = soup.find('li') # get everything under order item
#for order in findorders.find('a'): # find 
#    orders.append(order)
#print(orders)
#
#
#findsuborders = findorders.find('li')
#
#print(findorders.find('li','Suborders'))
#
#for suborder in findsuborders.find('a'):
#    suborders.append(suborder)
#
#print(suborders)
#print(len(findsuborders.find_all('li')))
#
#for i in range(len(findsuborders.find_all('li'))): # only print how many items there are in the category??
#    counter += 1
#print(counter)
#----------------

#finallist = []
#
#for listitem in soup.select('ul'):
#    finallist.append('dog')

#wholelist = soup.find('ul')
#listOrder = wholelist.find_all('li')
#
#for ul in listOrder:
#    for li in ul.findAll('li'):
#        for a in li.find('a'):
#            print(a)
            
#if None in (li):
#    continue

#listOrder = wholelist.find('b')
#listOrderName = wholelist.find('a')
#listSuborder = listOrder.find('ul')
#listSuborderItem = listSuborder.find('li')
#listSuborderItemName = listSuborderItem.find('b')

#print(listOrder.text + ", " + listOrderName.text)
#print(listSuborderItemName.text)
# print(finallist)

#print(listOrder)
print('YEEHAW! DONE!')



#links = []
#
#for link in soup.select('.wikitable .image'):
#    links.append(link['href'])
#
#links_list = []
#
#for media_page in links:
#    req = requests.get('https://en.wikipedia.org' + media_page)
#    soup = BeautifulSoup(req.text, 'html.parser')
#    img_div = soup.find('div', {'class': 'mw-filepage-resolutioninfo'})  # you can change this for different size images
#    img_path = 'https:' + img_div.find('a')['href']
#    links_list.append(img_path)
#    print(img_path)
#
#txt_file = open('download.txt', 'w')
# 
#for line in links_list:
#     txt_file.write(line)
#     txt_file.write('\n')
# 
#txt_file.close()