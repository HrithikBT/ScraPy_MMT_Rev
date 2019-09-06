

from bs4 import BeautifulSoup
import requests
import datetime
import csv
import re


time = datetime.datetime.now()
ts = str(time.year)+"-"+str(time.month)+"-"+str(time.day)
csv_file = open('mtt_reviews_tripadv.csv','w', newline='',encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Customer','location','Review'])

lst=[]
for i in range(0,29):
	lst.append('https://www.tripadvisor.in/ShowTopic-g293860-i511-k1731413-o'+str(i)+'0-Makemytrip_com-India.html')
for lis in lst:
	source = requests.get(lis).text
	soup = BeautifulSoup(source,'lxml')
	''
	for mdiv in soup.find_all('div',class_="post"):
		if(mdiv.find('div',class_="username") is not None):
			Author = mdiv.find('div',class_="username").span.text
			location = mdiv.find('div',class_="location").text
			Review = mdiv.find('div',class_="postBody")
			per=''
			for p in Review.find_all('p'):
				per=per+p.text
			
			p1 = per.split('(ta')[0]
			p2 = per.split(');')[len(per.split(');'))-1]
			per = p1+p2
			print(Author,location,per)
			csv_writer.writerow([Author,location,per])
			print()

csv_file.close()
