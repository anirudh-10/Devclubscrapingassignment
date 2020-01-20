
import bs4
from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup
import os
from os import path
import requests 
f1=open("input.txt","r")
l=f1.readlines()
f1.close()
startmonth,startyear=l[0].split()
endmonth,endyear=l[1].split()
L=l[2].split()
if (startmonth[0:3]=="jan"):
	sm=1

elif(startmonth[0:3]=="feb"):
	sm=2
elif(startmonth[0:3]=="mar"):
	sm=3	
elif(startmonth[0:3]=="apr"):
	sm=4
elif(startmonth[0:3]=="may"):
	sm=5
elif(startmonth[0:3]=="jun"):
	sm=6
elif(startmonth[0:3]=="jul"):
	sm=7
elif(startmonth[0:3]=="aug"):
	sm=8
elif(startmonth[0:3]=="sep"):
	sm=9
elif(startmonth[0:3]=="oct"):
	sm=10
elif(startmonth[0:3]=="nov"):
	sm=11
elif(startmonth[0:3]=="dec"):
	sm=12
if (endmonth[0:3]=="jan"):
	em=1
elif(endmonth[0:3]=="feb"):
	em=2
elif(endmonth[0:3]=="mar"):
	em=3	
elif(endmonth[0:3]=="apr"):
	em=4
elif(endmonth[0:3]=="may"):
	em=5
elif(endmonth[0:3]=="jun"):
	em=6
elif(endmonth[0:3]=="jul"):
	em=7
elif(endmonth[0:3]=="aug"):
	em=8
elif(endmonth[0:3]=="sep"):
	em=9
elif(endmonth[0:3]=="oct"):
	em=10
elif(endmonth[0:3]=="nov"):
	em=11
elif(endmonth[0:3]=="dec"):
	em=12
		

sy=int(startyear)
ey=int(endyear)
while(sy<=ey):
	if(sy==ey):
		if(sm>em):
			exit()

	if(sm==1):
		m=""
	elif(sm<=9):
		m="/0"+str(sm)
	else:
		m="/"+ str(sm)
	if(sy==2020):
		n=""
	else:
		n=str("/")+str(sy)		
	my_url = 'http://explosm.net/comics/archive' + n + m
	u_client = uReq(my_url)
	page_html =u_client.read()
	u_client.close()
	page_soup=soup(page_html , "html.parser")	
	containers= page_soup.findAll("div",{"class":"row collapse"})
	date=page_soup.findAll("div",{"id":"comic-author"})
		
	for i in range(len(containers)):
		if(sm==1):
			currentmonth="january"
		elif(sm==2):
			currentmonth="february"
		elif(sm==3):
			currentmonth="march"
		elif(sm==4):
			currentmonth="april"
		elif(sm==5):
			currentmonth="may"
		elif(sm==6):
			currentmonth="june"
		elif(sm==7):
			currentmonth="july"
		elif(sm==8):
			currentmonth="august"
		elif(sm==9):
			currentmonth="september"
		elif(sm==10):
			currentmonth="october"
		elif(sm==11):
			currentmonth="november"
		elif(sm==12):
			currentmonth="december"											
		container=containers[i]
		dat=date[i]
		my_url='http://explosm.net'+container.div.a["href"]
		u_client = uReq(my_url)
		page_html =u_client.read()
		u_client.close()
		page_soup=soup(page_html , "html.parser")
		conts=page_soup.findAll("div",{"id":"comic-wrap"})
		imgurl=conts[0].img["src"]	
		monthdate=date[i].contents[0][1:]
		currentyear=date[i].contents[0][1:5]
		authorname=date[i].contents[2][4:8]
		if authorname in L:
			if(path.exists(currentyear==False)):
				os.mkdir(currentyear)
			if(path.exists(currentyear +"/"+currentmonth)==False):
				os.mkdir(currentyear + "/"+currentmonth)
			f=requests.get(imgurl)
			f1=open(currentyear +"/"+currentmonth+"/" + monthdate +"-"+authorname+".png","wb" )
			f1.write(f.content)
			f1.close()
	sm+=1
	if(sm==13):
		sm=1
		sy+=1	

