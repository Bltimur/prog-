import requests

url = "https://rozetka.com.ua/mobile-phones/c80003/"

user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 "
header = { " User-Agent": user }
session = requests.Session()


response = session.get(url, headers=header)

if response.status_code == 200:
    soup = BeautifulSoup(response.tet, features"lxml")


all_products = soup.find_all(name:"li",  class_="all_products = soup.find_all('li', class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")
")
    for product in all_products:
