import scrape
import credentials
import unittest
import io
import sys

class MyTest(unittest.TestCase):
    def test_nouser(self):
        username = 'rishi'
        x = 0
        for y in credentials.myresult:
            if username == y:
                x=1
        self.assertEqual(x,0)

    username = "k4ni5h"
    def setUp(self):
        query = f"UPDATE user SET scraped = 0, name =  NULL,city=NULL WHERE username = '{self.username}'"
        credentials.mycursor.execute(query)
        credentials.mydb.commit()

    def test_ScrapefirstTime(self):
        scrape.scrape(self.username)
        credentials.mycursor.execute(f"SELECT scraped,name,city FROM user WHERE username ='{self.username}'")
        self.credentials = credentials.mycursor.fetchall()[0]
        self.assertEqual(1, self.credentials[0])

    def test_ScrapedUser(self):
        scrape.scrape(self.username)
        output_text = io.StringIO()
        sys.stdout = output_text
        scrape.scrape(self.username)
        sys.stdout = sys.__stdout__
        self.assertEqual(output_text.getvalue(), 'My name is Kanish and my current city is Roorkee\n')
    
    def tearDown(self):
        query = "UPDATE user SET scraped = 0, name = NULL , city=NULL WHERE username='k4ni5h'"
        credentials.mycursor.execute(query)
        credentials.mydb.commit()

if __name__=='__main__':
    unittest.main()

