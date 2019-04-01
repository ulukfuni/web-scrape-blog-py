from bs4 import BeautifulSoup
from requests import get
from flask import Flask

app = Flask(__name__)
@app.route('/')
def helloWorld():
    print('Hello, Scrapers!')

@app.route('/scrape')
def scrape():
    url = 'https://www.basketball-reference.com/players/w/wadedw01.html'
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.findAll('div', class_='stats_pullout'))

