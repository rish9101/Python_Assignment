import requests
from bs4 import BeautifulSoup
from contextlib import closing
import classes
import credentials

def scrape(username):


	query = f"SELECT scraped,name,city FROM user WHERE username= {username}"
	credentials.mycursor.execute(query)

	scraped = credentials.mycursor.fetchall()

	for user_info in scraped:
		if user_info[0] == 1:
			for user_info in scraped:
				name = x[1]
				city = x[2]
			p1 = classes.Person(name,city)
			p1.show()

		else:
			r=requests.get('https://en-gb.facebook.com/'+username)
			x=r.content

			html = BeautifulSoup(x,'html.parser')

			favourites = {}

			i = 0
			l1 = []
			for div in html.findAll('div',{'class':'labelContainer'}):
				l1.append(div.text.strip())
			for div in html.findAll('div',{'class':'mediaPageName'}):
				favourites[l1[i]]=div.text.strip()
				i = i+1
			
			name = ""
			for a in html.findAll('a',{'class':'_2nlw _2nlv'}):
				name = a.text.strip()
			
			city={}
			strc = "current"

			for span in html.findAll('span',{'class':'_2iel _50f7'}):
				city[strc]=span.text.strip()
				strc = "hometown"

			current_city = city["current"]
			work = []
			for div in html.findAll('div',{'class':'_2lzr _50f5 _50f7'}):
				work.append(div.text.strip())

			if bool(favourites):
				for item in favourites:
					print(f"{item}+   :+{favourites[item]}")
			else:
				print("There are no favourites")

			print(name)

			print(current_city)

			if bool(work) and (current_city != ""):
				p1= classes.Person(name,current_city,work)
				print(p1.name)
				print("Object created")

			else:
				username = classes.Person(name)
				print("Not created")

					query2 = f"UPDATE user SET scraped = 1,name= {name}, city={city} WHERE username={username}"
					credentials.mycursor.execute(query2)
					print(credentials.mycursor.execute(query2))
					credentials.mydb.commit()