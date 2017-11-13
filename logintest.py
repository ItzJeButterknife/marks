import requests
from bs4 import BeautifulSoup
import time
import smtplib
from lxml import html

marks = []
payload = {
    "ctl00$ContentPlaceHolder1$Username$input": "--",
    "ctl00$ContentPlaceHolder1$Password$input": "--",
}

def CheckChange(tweet):
    if mark in marks:
        print("No change found.")
        print(mark)
        marks.pop(0)
    else:
        print("It changed!")

while True:
    session = requests.session()
    login = requests.get("https://metameer.itslearning.com")
    result = session.get(login)

    tree = html.fromstring(result.text)
    result = session.post(
        login,
        data = payload,
        headers = dict(referer=login)
    )

    #page = requests.get("https://metameer.itslearning.com/index.aspx")
    #soup = BeautifulSoup(page.content, 'html.parser')
    #info = soup.find_all(class_="ptaVakGem")
    #print (info)
