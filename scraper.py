

from bs4 import BeautifulSoup
import requests
import datetime
import csv



time = datetime.datetime.now()
ts = str(time.year)+"-"+str(time.month)+"-"+str(time.day)
csv_file = open('mtt_reviews_'+ts+'.csv','w', newline='',encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Customer','Date','Review'])

lst=[]
for i in range(1,24):
	lst.append('https://www.consumeraffairs.com/travel/makemytrip.html?page='+str(i))
for lis in lst:
	source = requests.get(lis).text
	soup = BeautifulSoup(source,'lxml')
	''
	for mdiv in soup.find_all('div',class_="rvw js-rvw"):
		Author = mdiv.find('strong',class_="rvw-aut__inf-nm").text
		date = mdiv.find('span',class_="ca-txt-cpt ca-txt--clr-gray").text.split(":")[1]
		Review = mdiv.find('div',class_="rvw-bd ca-txt-bd-2")
		rev=Review.find_all('p')[1].text

		print(Author,date,rev)
		csv_writer.writerow([Author,date,rev])
		print()

csv_file.close()
