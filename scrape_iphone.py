import requests
import time
from bs4 import BeautifulSoup

number_of_pages_to_scrape=int(input("Enter the number of pages to scrape from flipkart"))
for i in range(number_of_pages_to_scrape):

    time.sleep(2)
    url=f"https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i+1}"
    content=requests.get(url)
    htmlContent=content.content
    soup=BeautifulSoup(htmlContent,'html.parser')
    containers=soup.find_all('div',{'class':'bhgxx2 col-12-12'})

    with open('abcde.csv', "a", encoding="utf-8") as f:
        headers="ProductName,Price,Ratings\n"
        f.write(headers)
        for i in range(3,27):
            product_name=containers[i].find('div',{'class':'_3wU53n'}).text
            print(product_name)
            time.sleep(0.5)
            price=containers[i].find('div',{'class':'_1vC4OE _2rQ-NK'}).text
            print(price)
            time.sleep(0.5)
            ratings=containers[i].find('span',{'class':'_38sUEc'}).text.split()[0]
            print(ratings)
            time.sleep(0.5)
            f.write(product_name.replace(",","|") + "," + price.replace(",","")[1::] + "," + ratings.replace(",","") + "\n")
            time.sleep(1)
