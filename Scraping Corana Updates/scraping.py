import requests
from bs4 import BeautifulSoup

url = "https://www.mygov.in/covid-19"
r = requests.get(url)
s = BeautifulSoup(r.text,"html.parser")
data = s.find_all("div",class_ = "information_row")

print("Total Cases: ",data[0].text.strip())
#print("Total Deaths: ",data[1].text.strip())
#print("Total Recovered: ",data[3].text.strip())