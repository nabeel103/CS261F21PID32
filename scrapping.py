
import requests
from bs4 import BeautifulSoup
import pandas as pd

def saveInCSV(title,city,country,model,meterReading,fuelType,engine,autoManuel,price,identity,contact):
    data = {
        
        'Title': title,
        'City':city,
        'Country':country,
        'Model':model,
        'Meter Reading':meterReading,
        'Fuel Type':fuelType,
        'Engine Capacity':engine,
        'Auto/Manuel':autoManuel,
        'Price':price,
        'Identity':identity,
        'Contact':contact
    }
    dataframe = pd.DataFrame(data)
    # print(dataframe)
    dataframe.to_csv('Scrap.csv',mode='a',index = False, header = False)

def addEntities(data,title,city,country,model,meterReading,fuelType,engine,autoManuel,price,identity,contact):
    uls = data.find_all('ul' , class_ = 'list-unstyled search-results search-results-mid next-prev car-search-results')
    
    for ul in uls:

        lis = (ul.find_all('li', class_ = 'classified-listing'))
        for li in lis:
            
            Title = (li.find('a')).get('title')
            newDiv = li.find('div', class_ = 'col-md-12 grid-date')
            newLi = newDiv.find_all('li')
            City = (newLi[0].text).replace("\n","")
            Country = "Pakistan"
            Model = newLi[1].text 
            reading = newLi[2].text 
            Ftype = newLi[3].text 
            Ecapacity = newLi[4].text 
            a_m = newLi[5].text 
            Price = str(li.find('div',class_='price-details generic-dark-grey').text).replace("\n","")
            button = li.find('button',class_ = 'btn btn-success phone_number_btn pull-right')
            buttonConntent = button.get('data-content')
            buttonConntent = BeautifulSoup(buttonConntent,'html.parser')
            Identity = buttonConntent.find('div',class_ = 'primary-lang').text
            Contact = str(buttonConntent.find('h4').text)

            #add data in lists
            title.append(Title.replace(" ",""))
            city.append(City.replace(" ",""))
            country.append(Country.replace(" ",""))
            model.append(Model.replace(" ",""))
            meterReading.append(reading.replace(" ",""))
            fuelType.append(Ftype.replace(" ",""))
            engine.append(Ecapacity.replace(" ",""))
            autoManuel.append(a_m.replace(" ",""))
            price.append(Price.replace(" ",""))
            identity.append(Identity.replace(" ",""))
            contact.append(Contact.replace(",","/"))
            
        
            
    
    

#lists
title = []
city = []
country = []
model = []
meterReading = []
fuelType = []
engine = []
autoManuel = []
price = []
identity =[]
contact = []


url = "https://www.pakwheels.com/"
# url = "https://www.pakwheels.com/576"

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
            addEntities(data,title,city,country,model,meterReading,fuelType,engine,autoManuel,price,identity,contact)
            saveInCSV(title,city,country,model,meterReading,fuelType,engine,autoManuel,price,identity,contact)
            title = []
            city = []
            country = []
            model = []
            meterReading = []
            fuelType = []
            engine = []
            autoManuel = []
            price = []
            identity =[]
            contact = []

            print(i)
        
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
