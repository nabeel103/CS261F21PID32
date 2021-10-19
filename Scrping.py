from bs4.element import CData
import requests
from bs4 import BeautifulSoup





url = "https://www.pakwheels.com/"

page = requests.get(url)

pageContent  = page.content 

pageContent = BeautifulSoup(pageContent,'html.parser')
# pageContent = pageContent.prettify
# print(pageContent)

#getting main div
mainDiv = pageContent.find_all('div' , id ="browesCTGSlider")
mainDiv = BeautifulSoup(str(mainDiv) , 'html.parser')

#finding the div having vehicle categories
categoryDiv = mainDiv.find('div' , class_ ='carousel-inner')
categoryDiv = BeautifulSoup(str(categoryDiv) , 'html.parser')
# print((categoryDiv))

count = 1

uls = categoryDiv.find_all('ul')

for ul in uls:
    ul = BeautifulSoup(str(ul), 'html.parser')
    lis = ul.find_all('li',class_ = 'col-sm-2')
    for li in lis:
	    # print(li.find_all('a'))
        anchor = li.find('a')
        #loading new page 
        url2 = url+anchor.get('href')
        # print(url2)
        data = requests.get(url2)

        #parsing loaded page
        data = data.content
        data = BeautifulSoup(data, 'html.parser')

        #Finding counting of next page
        nextPageUL = data.find_all('ul' , class_ = 'pagination search-pagi')
        nextPageUL = BeautifulSoup(str(nextPageUL) , 'html.parser')
        endPage = nextPageUL.find('li' , class_ = 'last next')
        lastPage = 0
        if endPage != None:
            endPage = endPage.find('a')
            endPage = endPage.get('href')
            endPage = str(endPage).split("=")
            lastPage = int(endPage[1]) # number of last page
        else:
            lastPage = 1
        
        for i in range(2,lastPage):
            h1 = data.find('h1')
            print(h1)
            #load and parsing
            url3 = url2+"?page="+str(i)
            data = requests.get(url3)
            data = data.content
            data = BeautifulSoup(data, 'html.parser')
            




        print(lastPage)

        count = count + lastPage


print("No = ",count)
